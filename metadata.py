#! /usr/bin/python
from xml.dom import minidom
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Unicode
from sqlalchemy.orm import relationship, backref

#engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('mysql+mysqldb://mikey:playstation@localhost/metadata')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Field(Base):
  __tablename__ = 'fields'
  sObjectField = Column(Unicode(255), primary_key=True)
  sObject= Column(Unicode(255))
  fullName = Column(Unicode(255))
  sftype = Column(Unicode(255))
  description = Column(Unicode(400))
  externalId = Column(Boolean)
  trackFeedHistory = Column(Boolean)
  trackHistory = Column(Boolean)
  label = Column(Unicode(255))

  ### TODO:
  ### Add Fields
  ### --Formula
  ### --FormulaTreatBlanksAs
  ### --ReferenceTo
  ### --RelationshipLabel
  ### --RelationshipName
  ### --Required
  ### --Unique
  ### --DeleteContraint
  ### --Length

  def __init__(self, sObject, xmlData):
    self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
    self.sObjectField = sObject + '.' + self.fullName
    self.sObject = sObject
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
      self.picklist = self.Picklist(self.sObjectField, xmlData.getElementsByTagName('picklist')[0])

  def __str__(self):
    return self.fullName + '-' + self.sftype + '-' + self.description

  def insert(self):
    session = Session()
    ## BRING OBJECTS INTO MEMORY.
    ## Similiar to upserting with merge() call
    session.query(Field).all()
    session.query(Field.Picklist).all()
    session.query(Field.Picklist.PicklistValue).all()
    session.merge(self)
    if hasattr(self, 'picklist'):
      session.merge(self.picklist)
      for picklistValue in self.picklist.picklistValues:
        session.merge(picklistValue)
    session.commit()

  class Picklist(Base):
    __tablename__ = 'picklists'
    picklistId = Column(Unicode(255), primary_key=True)
    controllingField = Column(Unicode(255))
    sfsorted = Column(Boolean)

    field_id = Column(Unicode(255), ForeignKey('fields.sObjectField'))
    field = relationship("Field", backref=backref('picklists'))

    def __init__(self, sObjectField, xmlData):
      self.picklistId = sObjectField
      self.picklistValues = []
      if xmlData.getElementsByTagName('controllingField'):
        self.controllingField = xmlData.getElementsByTagName('controllingField')[0].firstChild.nodeValue
      if xmlData.getElementsByTagName('sorted'):
        if xmlData.getElementsByTagName('sorted')[0].firstChild.nodeValue == 'true':
          self.sfsorted = True
        else:
          self.sfsorted = False
      for picklistValue in xmlData.getElementsByTagName('picklistValues'):
        self.picklistValues.append(self.PicklistValue(sObjectField, picklistValue))

    def __str__(self):
      #return u';'.join([unicode(x) for x in self.picklistValues]).encode('utf8')
      return ';'.join([unicode(x) for x in self.picklistValues])

    def __repr__(self):
      return u';'.join([unicode(x) for x in self.picklistValues])

    class PicklistValue(Base):
      __tablename__ = 'picklist_values'
      picklistValueId = Column(Unicode(255), primary_key=True)
      fullName = Column(Unicode(255))
      default = Column(Boolean)

      picklist_id = Column(Unicode(255), ForeignKey('picklists.picklistId'))
      picklist = relationship("Picklist", backref=backref('picklistValues'))

      def __init__(self, sObjectField, xmlData):
        self.fullName = xmlData.getElementsByTagName('fullName')[0].firstChild.nodeValue
        self.picklistValueId = sObjectField + '-' + self.fullName
        if xmlData.getElementsByTagName('default')[0].firstChild.nodeValue == 'true':
          self.default = True
        else: 
          self.default = False

      def __str__(self):
        return self.fullName
      def __repr__(self):
        return self.fullName

Base.metadata.create_all(engine)
