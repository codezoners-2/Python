import re
import os

# returns state name from string			
def extractData(aString):
	'''	
	>>> s = "hello"
	>>> extractData(s)
	
	'''
	return 0

# reads a file and returns a list
def fileToString(filename):
	'''
	>>> fileToString('dummyFile.txt')
	'one\\ntwo\\n'
	'''
	f = open(filename)
	contentsList = f.read()
	f.close()
	return contentsList


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
	>>> getMinValue({'vm': ['vermont', 100], 'ak': ['alaska', 5]})
	5
	
	'''
	minValue = 100000000
	for state in aDict.values():
		if state[1]<minValue:
			minValue=state[1]
	return minValue

# main function is called only when program is run
# from command line
def main():
	print "*** POPULATION DATA ***"
	fileWithPath = os.path.join("data", "population.html")
	myDict = extractData(fileToString(fileWithPath))
	if myDict:
		for e in myDict: print '{0:5} {1:18} {2}'.format(e, myDict[e][0], myDict[e][1])
	
	print 
	print "*** LAND SIZE DATA ***"	
	fileWithPath = os.path.join("data", "landsize.html")
	myDict = extractData(fileToString(fileWithPath))
	if myDict:
		for e in myDict: print '{0:5} {1:18} {2}'.format(e, myDict[e][0], myDict[e][1])
		
if __name__ == "__main__":
	main()
