#! /usr/bin/python

import parse
from pprint import pprint
import sqlalchemy

a = parse.parseAll()
#a = parse.parseListView('examples/Account.object')

#for view in a:
#  print(view)
#  for column in view.columns:
#    print '\t' + column.columnName
