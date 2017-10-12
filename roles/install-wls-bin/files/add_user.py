#!/usr/bin/python
import os, sys

t3url=sys.argv[1]
wlsAdminUser=sys.argv[2]
wlsAdminPassword=sys.argv[3]
wlsUser=sys.argv[4]
wlsPassword=sys.argv[5]

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

def createUser(authenticator, userName, password, description):
  print ("Creating user " + userName)
  if authenticator.userExists(userName):
    print ("User "+userName+" already exists.")
  else:
    print ("User "+userName+" does not exist.")
    authenticator.createUser(userName, password, description)
    print("User "+userName+" created.")

connect(wlsAdminUser,wlsAdminPassword,'t3://'+t3url)
# Get Realm and Authenticator
realm = getRealm()
authenticator = getAuthenticator(realm)
createUser(authenticator, wlsUser, wlsPassword)
disconnect();
exit()