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
    myField = metadata.Field('Account',field)
    myField.insert()
    #pprint(vars(myField))
    allFields.append(myField)
  return allFields

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
