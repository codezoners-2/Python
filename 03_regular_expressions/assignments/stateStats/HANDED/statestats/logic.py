import re
import os

# returns state name from string			
def extractStateName(aString):
	'''
	write tests here
	
	'''
	return 0
		
# returns state abbreviation from string
def extractStateAbbr(aString):
	'''
	write tests here
	
	'''
	return 0

# returns state population from string
def extractStateStats(aString):
	'''
	write tests here
	
	'''
	return 0


# takes a list of strings and returns a dictionary
# which contains the relevant state data
def linesToDict(myList):
	'''
	write tests here
	
	'''
	return 0


# reads a file and returns a list
def fileToList(filename):
	'''
	write tests here
	
	'''
	return 0


def getMaxValue(aDict):
	'''
	>>> getMaxValue({'vm': ['vermont', 100], 'ak': ['alaska', 5]})
	100
	
	'''
	maxValue = 0
	for state in aDict.values():
		if state[1]>maxValue:
			maxValue=state[1]
	return maxValue

def getMinValue(aDict):
	'''
	write tests here: see getMaxValue above
	
	'''
	return 0

# main function is called only when program is run
# from command line
def main():
	print "*** POPULATION DATA ***"
	fileWithPath = os.path.join("data", "population.html")
	myDict = linesToDict(fileToList(fileWithPath))
	if myDict:
		for e in myDict: print '{0:5} {1:18} {2}'.format(e, myDict[e][0], myDict[e][1])
	
	print 
	print "*** LAND SIZE DATA ***"	
	fileWithPath = os.path.join("data", "landsize.html")
	myDict = linesToDict(fileToList(fileWithPath))
	if myDict:
		for e in myDict: print '{0:5} {1:18} {2}'.format(e, myDict[e][0], myDict[e][1])
	
if __name__ == "__main__":
	main()
