import re

email = '@obama here is my email address codezoners-2@rave.ac.uk for help'

## find email address
match = re.search(r'[\w.\d-]+@[.\w]+', email)

if match: print 'example 1 -> I found: ', match.group()
else: print 'example 1 -> not found'
