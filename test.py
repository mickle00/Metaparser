#! /usr/bin/python

import parse
from pprint import pprint

a = parse.example()

print '\n\n\n\n\n'
##pprint(vars(a[2].picklist))

for i in a:
  if hasattr(i, 'picklist'):
    try: 
      if i.picklist.controllingField:
        print str(i) + 'CONTROLLING FIELD',
        print(i.picklist.controllingField)
    except:
      pass
