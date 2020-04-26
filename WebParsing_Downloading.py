#Imports:
from selenium import webdriver
import urllib.request
from urllib.request import urlretrieve

#Open the browser:
driver = webdriver.Chrome()
driver.get("https://www.python.org/downloads/")
driver.implicitly_wait(60)

#Get the object list:
elements = driver.find_elements_by_xpath("//section/div[2]/ol/li")

#Display the number of Python versions availible for download:
print("There's " + str(len(elements)) + " Python versions available for download.")

#Display all of the Python versions:
counter = 1
while counter < len(elements):
    releaseVersion = driver.find_element_by_xpath("//div[2]/ol/li["+str(counter)+"]/span[@class='release-number']/a").text
    releaseDate = driver.find_element_by_xpath("//div[2]/ol/li["+str(counter)+"]/span[@class='release-date']").text
    print(releaseDate)
    #print(releaseVersion + " - " + releaseDate)
    counter += 1

#Ask the user what release date that whant to download Python from:
releasedVersionOnDateFound = False
versionFound = ""
releasedVersionsOnThatDate = 0
while releasedVersionOnDateFound == False:
	text = input("\nType in a Python Release Date. (Example: April 6, 2013) ")
	print("You wanted to download Python that was released on " + text + ". Checking for Python versions on that date...")
	
	#Find how many Python versions were released at the date the user requested:
	counter = 1
	while counter < len(elements):
		releaseVersion = driver.find_element_by_xpath("//div[2]/ol/li["+str(counter)+"]/span[@class='release-number']/a").text
		releaseDate = driver.find_element_by_xpath("//div[2]/ol/li["+str(counter)+"]/span[@class='release-date']").text
		
		#If the release date matches the user's release date, then display that version:
		if text == releaseDate:
			releasedVersionsOnThatDate += 1
			releasedVersionOnDateFound = True
			versionFound = releaseVersion
			print(releaseVersion+" - "+releaseDate)
		counter += 1

	if releasedVersionsOnThatDate == 0:
		print("\nSorry, there was no version of Python released on that date.")

if releasedVersionsOnThatDate == 1:	
	print("\nThe version of Python released on that date was "+versionFound+". Downloading now.")
	versionFound = versionFound.replace("Python ","")
	#print(versionFound.replace("Python ",""))
	print("https://www.python.org/ftp/python/"+str(versionFound)+"/Python-"+str(versionFound)+".msi")
	#Download selected released version:
	
	#url = "https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz"
	##urllib.request.urlretrieve(url, "eric-Python-version"+str(versionFound)+".exe")
	urllib.request.urlretrieve("https://www.python.org/ftp/python/"+str(versionFound)+"/python-"+str(versionFound)+".exe","eric-Python-version"+str(versionFound)+".exe")
	#https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
if releasedVersionsOnThatDate > 1:
	#counter = 1
	print("There was "+str(releasedVersionsOnThatDate)+" versions of Python released on that date. Type in the Python version you'd like to download, then press ENTER. (Example: 3.7.7)")
	text = input()
	print("You wanted to download Python " + text + ". Checking for that version...")
	
	#Download selected version:
	counter = 1
	while counter < len(elements):
		releaseVersion = driver.find_element_by_xpath("//div[2]/ol/li["+str(counter)+"]/span[@class='release-number']/a").text

		#Loop through the list and find the Python version the user wanted to download:
		if "Python " + text  == releaseVersion:
			print("Release version found! Downloading file.")

			#Download selected released version:
			#urllib.request.urlretrieve("https://www.python.org/ftp/python/2.7.4/python-2.7.4.msi","eric-Python-version2.7.4.exe")
            #urlretrieve("https://www.python.org/ftp/python/"+str(text)+"/Python-"+str(text)+".tgz","eric-Python-version"+str(text)+".exe")
			urllib.request.urlretrieve("https://www.python.org/ftp/python/"+str(text)+"/python-"+str(text)+".msi","eric-Python-version"+str(text)+".exe")			
			print("File downloaded")
			break
		else:
			counter += 1

	if counter == len(elements) and "Python " + text != releaseVersion:
		print("Error, release version not found!")
	
