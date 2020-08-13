import xml.etree.ElementTree
import os

###########################################
### Resources files path 

configFileName = "fastlane/config.xml"
fastlaneFastFilePath = ""
###########################################


def getCompanyName():
	return getSingleParameter('companyname')


def getKeystorePassword():
	return getSingleParameter('keystorepassword')



#############################################
### Utils
def getSingleParameter(parameterName):
	e = xml.etree.ElementTree.parse(configFileName).getroot()
	return e.find(parameterName).text

def SetSingleParameter(parameterName, parameterValue):
	e = xml.etree.ElementTree.parse(configFileName)
	e.find(parameterName).text = parameterValue
	e.write(configFileName)
#############################################