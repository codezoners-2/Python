import re

email = 'email codezoners-2@mydomain.com for help'

## find all usernames + domains
match = re.search(r'______________', email)

if match:
	print 'whole group -> ', match.group()
	print 'first part -> ', match.group(1)
	print 'second part -> ', match.group(2)
else: print 'not found'
