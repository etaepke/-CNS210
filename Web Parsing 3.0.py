#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import urllib


result = requests.get('https://python.org/downloads')
src = result.content
soup = BeautifulSoup(src, 'html.parser')
all_versions = soup.select('.list-row-container li')

for version in all_versions:
    for i in version.select(".release-date"):
       print(i.get_text())

text = input("\nType in the Python release date you'd like to download, then press ENTER. (Example: April 6, 2013) ")
print("You wanted to download Python released on " + text + ". Checking for that release date...")
            
        #text = input("\n Select the Python version you would like to download...")
        #print("Python" + text + " selected")
for version in all_versions:
    if i in version.select(".release-date"):
        releaseVersion = version.select(".release-version")
        releaseDate = version.select(".release-date")
        print(release.select(".release-date"))
        #print(i.get_text())
