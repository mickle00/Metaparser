#! /usr/bin/python2.7
from xml.dom import minidom
import glob

def cleanSObject(fileLocation):
  xmlDoc = minidom.parse(fileLocation)
  cleanFileName = fileLocation.replace('.object', '.schema')
  print cleanFileName
  newFile = open(cleanFileName, 'w')
  fieldList = xmlDoc.getElementsByTagName('fields')
  for field in fieldList:
    fieldName = field.getElementsByTagName('fullName')[0].firstChild.nodeValue
    fieldType = field.getElementsByTagName('type')[0].firstChild.nodeValue
    outputText = fieldName + ' - ' + fieldType + '\n'
    newFile.write(outputText)
  newFile.close()

def doCleaning():
  sObjects = glob.glob('src/objects/*.object')
  print sObjects
  for fileName in sObjects:
    cleanSObject(fileName)
