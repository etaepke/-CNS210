#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib2
import urllib

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print(tag)
        if (tag == "input"):
            print("Found an input ", tag)
            print(attrs)

url = "https://www.python.org/downloads"
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())



print("Begin download")

urllib.urlretrieve("https://www.python.org/ftp/python/2.7.4/python-2.7.4.msi", "eric-Python-version2.7.4.exe")

print("Completed")