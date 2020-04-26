#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import urllib


result = requests.get('https://python.org/downloads')
src = result.content
soup = BeautifulSoup(src, 'html.parser')
all_versions = soup.select('.list-row-container li')

for item in soup.find_all("ol",{"class":"list-row-container menu"}):
    number = item.find("span", {"class":"release-number"})
    trash = number.find_all("a").text
    print(trash)

##for version in all_versions:
    ##for i in version.select(".release-date"):
       ##print(i.get_text())

##text = input("\nType in the Python release date you'd like to download, then press ENTER. (Example: April 6, 2013) ")
##print("You wanted to download Python released on " + text + ". Checking for that release date...")
            
        #text = input("\n Select the Python version you would like to download...")
        #print("Python" + text + " selected")
##for version in all_versions:
    ##if i in version.select(".release-date"):
        ##print(i.get_text())

#print("Begin download")

#urllib.urlretrieve("https://www.python.org/ftp/python/2.7.4/python-2.7.4.msi", "eric-Python-version2.7.4.exe")

#print("Completed")
