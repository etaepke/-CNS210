#!/usr/bin/python

from HTMLParser import HTMLParser
import urllib2

class myParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print(tag)
        if (tag == "input"):
            print("Found an input ", tag)
            print(attrs)

url = "http://3.17.10.219/forms/index.html"
request = urllib2.Request(url)
handle = urllib2.urlopen(request)
parser = myParser()
parser.feed(handle.read())