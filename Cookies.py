#!/usr/bin/python

import urllib2

url = "https://www.google.com"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
cookies = response.info()['Set-Cookie']
content = response.read()
response.close()
print(cookies)

print(content)