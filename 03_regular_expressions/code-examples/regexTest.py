import re

myString = "I love python!"

patt = r'love \w\w\w\w\w\w'

match = re.search(patt, myString)
