#!/usr/bin/python

import urllib2

proxy = urllib2.ProxyHandler({'http':'127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
handle = urllib2.urlopen('http://neverssl.com')

print(handle.read())