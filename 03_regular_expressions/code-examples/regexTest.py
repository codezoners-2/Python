import re

myString = '''I love python'''

patt = 'love \w\w\w\w\w\w'

match = re.search(patt, myString)

if match:
	print match.group()
else:
	print "I found no matches"
