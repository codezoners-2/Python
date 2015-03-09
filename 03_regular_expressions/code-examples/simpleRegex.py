import re

myString = 'I love python'
match = re.search(r'love \w\w\w\w\w\w', myString)
if match:                  
	print 'I found: ', match.group()
else:
	print 'not found'
