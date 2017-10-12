#!/usr/bin/python
import os, sys
# Get variables
wlsAdminServerPort=sys.argv[1]
adminUsername=sys.argv[2]
adminPassword=sys.argv[3]
msName=sys.argv[4]

connect(adminUsername,adminPassword,'t3://localhost:' + wlsAdminServerPort)

# Start Managed Server
# --------------------
try:
	start(msName,'Server')
except:
	dumpStack()

exit()
