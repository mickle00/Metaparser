#! /usr/bin/python2.7
from xml.dom import minidom
import glob
import metadata
from pprint import pprint

def parseMetaData(fileLocation):
  xmlDoc = minidom.parse(fileLocation)
  fieldList = xmlDoc.getElementsByTagName('fields')
  allFields = []
  for field in fieldList:
    myField = metadata.Field(field)
    pprint(vars(myField))
    allFields.append(myField)
  return allFields

def example():
  return parseMetaData('examples/Account.object')
