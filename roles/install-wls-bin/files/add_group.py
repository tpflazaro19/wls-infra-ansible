#!/usr/bin/python
import os, sys

t3url=sys.argv[1]
wlsAdminUser=sys.argv[2]
wlsAdminPassword=sys.argv[3]
wlsGroup=sys.argv[4]

def getRealm(name=None):
  cd('/')
  if name == None:
    realm = cmo.getSecurityConfiguration().getDefaultRealm()
  else:
    realm = cmo.getSecurityConfiguration().lookupRealm(name)
  return realm

def getAuthenticator(realm, name=None):
  if name == None:
    authenticator = realm.lookupAuthenticationProvider('DefaultAuthenticator')
  else:
    authenticator = realm.lookupAuthenticationProvider(name)
  return authenticator

def createGroup(authenticator, groupName, description):
  print ("Creating group " + groupName)
  if authenticator.groupExists(groupName):
    print ("Group "+groupName+" already exists.")
  else:
    print ("Group "+groupName+" does not exist.")
    authenticator.createGroup(groupName, description)
    print("Group "+groupName+" created.")

connect(wlsAdminUser,wlsAdminPassword,'t3://'+t3url)
# Get Realm and Authenticator
realm = getRealm()
authenticator = getAuthenticator(realm)
createGroup(authenticator, wlsGroup)
disconnect();