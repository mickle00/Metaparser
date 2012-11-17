#! /usr/bin/python
from xml.dom import minidom

class Field():
  class Picklist():
    controllingField = ''
    picklistValues = []
    sfsorted = False

    def __init__(self, xmlData):
      pass
      ##self.controllingField = xmlData.getElementsByTagName('controllingField')[0].firstChild.nodeValue
      ##self.sfsorted = xmlData.getElementsByTagName('sfsorted')[0].firstChild.nodeValue
      ##for item in xmlData.getElementsByTagName('picklistValues'):
      ##  print item.firstChild.nodeValue


    class PicklistValue():
      fullName = ''
      default = False

      def __init__(self, xmlData):
        self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
        self.default = xmlData.getElementsByTagName('default')[0].firstChild.nodeValue


  fullName = ''
  defaultValue = False
  description = ''
  externalId = False
  label = ''
  trackFeedHistory = False
  trackHistory = False
  sftype = ''
  picklist = []
  
  def __init__(self, xmlData):
    self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('defaultValue'):
      self.defaultValue = xmlData.getElementsByTagName('defaultValue')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('description'):
      self.description = xmlData.getElementsByTagName('description')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('externalId'):
      self.externalId = xmlData.getElementsByTagName('externalId')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('label'):
      self.label = xmlData.getElementsByTagName('label')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('trackFeedHistory'):
      self.trackFeedHistory = xmlData.getElementsByTagName('trackFeedHistory')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('trackHistory'):
      self.trackHistory = xmlData.getElementsByTagName('trackHistory')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('type'):
      self.sftype = xmlData.getElementsByTagName('type')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('picklist'):
      print 'THIS IS IT: '
      print str(xmlData)
      print str(xmlData.getElementsByTagName('picklist')[0].getElementsByTagName('picklistValues')[0].getElementsByTagName('fullName')[0].firstChild.nodeValue) ##[0].firstChild.nodeValue)
      ##self.picklist = self.Picklist(xmlData.getElementsByTagName('picklist')[0].firstChild.nodeValue)

  def __str__(self):
    return self.fullName + '-' + self.description
