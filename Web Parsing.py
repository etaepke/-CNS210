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

#counter = 0

#for version in all_versions:
    #if i in version.select(".release-date"):
        #print(i.get_text())
            
        #text = input("\n Select the Python version you would like to download...")
        #print("Python" + text + " selected")
#counter = 0

for version in all_versions:
    for i in version.select(".release-date"):
            if i.get_text() == text:
                #print("save date!")
            releaseVersion = version.select(".release-version")
            releaseDate = version.select(".release-date")
            print(release.select(".release-version"))
            #for j in version.select(".release-version"):
                #print(j.get_text())
            print(version.select(".release-version").get_text())
                print(i.get_text())

#counter = 1
#while counter < len(soup):
    #releaseDate = driver.find_element_by_xpath("/html/body/div/div[3]/div/section/div[1]/ol/li["+str(counter)+"]/span[@class='release-date']/a").text

    #if "Python " + text  == releaseDate:
        #print("Release date found! Downloading file.")

        #driver.get("https://www.python.org/ftp/python/"+str(text)+"/Python-"+str(text)+".tgz")
        #break
    #else:
        #counter += 1