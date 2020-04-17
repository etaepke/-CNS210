#!/usr/bin/python

import httplib

#host ="3.17.10.219"
host = "www.google.com"
#host = "www.yahoo.com"
#host = "neverssl.com"

request = httplib.HTTP(host)
request.putrequest("HEAD" , "/")
request.putheader("Host", host)
request.endheaders()

statusCode, statusMsg, headers = request.getreply()
print("Status: ", statusCode)
print(headers)