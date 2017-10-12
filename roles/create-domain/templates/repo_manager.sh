#!/bin/bash
set -e

RCU_HOME={{ middleware_common_home }}
RSP=/tmp/rcursp.log
export JAVA_HOME={{ java_home }}
export PATH=$RCU_HOME/bin:$PATH

RCU_ACTION="$1"
CONNECT_STRING="$2"
DB_USER="$3"
SYS_PASSWORD="$4"
SCHEMA_PREFIX="$5"
SCHEMA_PASSWORD="$6"
COMPONENT_LIST="$7"

function f_usage(){
   echo "Usage:"
   echo "$0 drop DB_SERVER:DB_PORT:SID SYS SYS_PASSWORD DEV SCHEMA_PASSWORD COMPONENT_FILE_LIST"
   echo "$0 create DB_SERVER:DB_PORT:SID SYS SYS_PASSWORD DEV SCHEMA_PASSWORD COMPONENT_FILE_LIST"
   exit
}

function f_create() {
   echo "$SYS_PASSWORD" > $RSP
   echo "$SCHEMA_PASSWORD" >> $RSP
   time rcu -silent -createRepository \
   -connectString $CONNECT_STRING \
   -dbUser $DB_USER \
   -dbRole SYSDBA \
   -schemaPrefix $SCHEMA_PREFIX \
   -useSamePasswordForAllSchemaUsers true \
   $( cat $COMPONENT_LIST ) -f < $RSP
}

function f_drop() {
   echo "$SYS_PASSWORD" > $RSP
   time rcu -silent -dropRepository \
   -connectString $CONNECT_STRING \
   -dbUser $DB_USER \
   -dbRole SYSDBA \
   -schemaPrefix $SCHEMA_PREFIX \
   $( cat $COMPONENT_LIST ) -f < $RSP
}

if [ $# -eq 0 ] ; then
  f_usage
fi

case "$1" in
   create)
      f_create
      ;;
   drop)
      f_drop
      ;;
   recreate)
      f_drop
      f_create
      ;;
   *)
      f_usage
      exit 1
esac

rm -f $RSP
