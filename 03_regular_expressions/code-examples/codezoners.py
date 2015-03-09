import re

myString = 'I am in codezone2'

## Search for pattern 'zone' in string 'I am a codezoner'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'zone', myString)
if match: print 'example 1 -> I found: ', match.group()
else: print 'example 1 -> not found'

## using \w to match any 'word' character [a-z,A-Z,0-9,_]
match = re.search(r'\w\wne', myString)
if match: print 'example 2 -> I found: ', match.group()
else: print 'example 2 -> not found'

## use \d to find the digit too
match = re.search(r'zone\d', myString)
if match: print 'example 3 -> I found: ', match.group()
else: print 'example 3 -> not found'

