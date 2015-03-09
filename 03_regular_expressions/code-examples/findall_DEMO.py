import re

email = 'email codezoners-2@mydomain.com for help or contact@mydomain.com'

## find all email addresses
match = re.findall(r'_________', email)

for m in match:
	print m
