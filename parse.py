#! /usr/bin/python2.7
from xml.dom import minidom
import glob
import metadata
from pprint import pprint
import os.path

def parseMetaData(fileLocation):
  xmlDoc = minidom.parse(fileLocation)
  fieldList = xmlDoc.getElementsByTagName('fields')
  allFields = []
  for field in fieldList:
    sObject = sObjectNameFromFile(fileLocation)
    myField = metadata.Field(sObject,field)
    myField.insert()
    #pprint(vars(myField))
    allFields.append(myField)
  return allFields

def parseListView(fileLocation):
  xmlDoc = minidom.parse(fileLocation)
  listViewList = xmlDoc.getElementsByTagName('listViews')
  allListViews = []
  for listView in listViewList:
    sObject = sObjectNameFromFile(fileLocation)
    myListView = metadata.ListView(sObject,listView)
    myListView.insert()
    allListViews.append(myListView)
  return allListViews

def sObjectNameFromFile(fileLocation):
  return os.path.basename(fileLocation).replace('.object','')

def parseAll():
  sObjects = glob.glob('examples/*.object')
  for fileName in sObjects:
    parseMetaData(fileName)
    parseListView(fileName)

def example():
  parseMetaData('examples/Account.object')
  #print metadata.engine.execute("select count(*) from fields").scalar()
  session = metadata.Session()
  ##query = session.query(metadata.Field).all()
  ##for field in query:
  ##  print field
  ##
  ##query = metadata.engine.execute("select count(*) from picklists").scalar()
  query = session.query(metadata.Field.Picklist).all()
  for field in query:
    print unicode(field)
##
 ## query = session.query(metadata.Field.Picklist.PicklistValue).all()
 ## for field in query:
 ##   print field
