import re

myString = 'I love python'
match = re.search(r'__________________', myString)
if match:                  
	print 'I found: ', match.group()
else:
	print 'not found'
