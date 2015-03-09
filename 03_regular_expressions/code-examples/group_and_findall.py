import re

email = ''' email codezoners-2@mydomain.com for help or contact@mydomain.com'''

## find all email addresses
match = re.findall(r'([\w-]+)@([\w.]+)', email)

for m in match:		# results come back as a list of tuples
	print m		    # a single tuple
