#! /usr/bin/python
from xml.dom import minidom

class Field():
  
  def __init__(self, xmlData):
    self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('defaultValue'):
      if xmlData.getElementsByTagName('defaultValue')[0].firstChild.nodeValue == 'true':
        self.defaultValue = True
      else:
        self.defaultValue = False
    if xmlData.getElementsByTagName('description'):
      self.description = xmlData.getElementsByTagName('description')[0].firstChild.nodeValue
    else:
      self.description = u''
    if xmlData.getElementsByTagName('externalId'):
      if xmlData.getElementsByTagName('externalId')[0].firstChild.nodeValue == 'true':
        self.externalId = True
      else:
        self.externalId = False
    if xmlData.getElementsByTagName('label'):
      self.label = xmlData.getElementsByTagName('label')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('trackFeedHistory'):
      if xmlData.getElementsByTagName('trackFeedHistory')[0].firstChild.nodeValue == 'true':
        self.trackFeedHistory = True
      else:
        self.trackFeedHistory = False
    if xmlData.getElementsByTagName('trackHistory'):
      if xmlData.getElementsByTagName('trackHistory')[0].firstChild.nodeValue == 'true':
        self.trackHistory = True
      else:
        self.trackHistory = False
    if xmlData.getElementsByTagName('type'):
      self.sftype = xmlData.getElementsByTagName('type')[0].firstChild.nodeValue
    if xmlData.getElementsByTagName('picklist'):
      self.picklist = self.Picklist(xmlData.getElementsByTagName('picklist')[0])

  def __str__(self):
    return self.fullName + '-' + self.sftype + '-' + self.description

  class Picklist():

    def __init__(self, xmlData):
      self.picklistValues = []
      if xmlData.getElementsByTagName('controllingField'):
        self.controllingField = xmlData.getElementsByTagName('controllingField')[0].firstChild.nodeValue
      if xmlData.getElementsByTagName('sorted'):
        if xmlData.getElementsByTagName('sorted')[0].firstChild.nodeValue == 'true':
          self.sfsorted = True
        else:
          self.sfsorted = False
      for picklistValue in xmlData.getElementsByTagName('picklistValues'):
        self.picklistValues.append(self.PicklistValue(picklistValue))

    def __str__(self):
      return u';'.join([unicode(x) for x in self.picklistValues]).encode('utf8')

    def __repr__(self):
      return u';'.join([unicode(x) for x in self.picklistValues]).encode('utf8')

    class PicklistValue():

      def __init__(self, xmlData):
        self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
        if xmlData.getElementsByTagName('default')[0].firstChild.nodeValue == 'true':
          self.default = True
        else: 
          self.default = False

      def __str__(self):
        return self.fullName
      def __repr__(self):
        return self.fullName

