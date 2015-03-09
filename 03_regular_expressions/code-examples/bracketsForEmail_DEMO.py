import re

email = 'email codezoners-2@rave.ac.uk for help'

## find email address
match = re.search(r'[\w.\d-]*@\w*.\w', email)

if match: print 'example 1 -> I found: ', match.group()
else: print 'example 1 -> not found'
