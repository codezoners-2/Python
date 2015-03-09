import re

myString = 'I am in codezoner for life, hurrayyyyyyyyyyyyy!!!'

## Search for everything after codezoner
match = re.search(r'codezoner\w*', myString)
if match: print 'example 1 -> I found: ', match.group()
else: print 'example 1 -> not found'

## match all 'hurray' independent of excitement
match = re.search(r'hurr\w*', myString)
if match: print 'example 2 -> I found: ', match.group()
else: print 'example 2 -> not found'

## Search for words starting with 'code'
match = re.search(r'___________', myString)
if match: print 'example 3 -> I found: ', match.group()
else: print 'example 3 -> not found'

## Find the word after the 'I' but only if it's the beginning of the sentence
## no matter how much space there is between it and the next word (but at least 1)
match = re.search(r'___________', myString)
if match: print 'example 4 -> I found: ', match.group()
else: print 'example 4 -> not found'
