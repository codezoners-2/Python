import re
import os

# returns state name from string			
def extractStateName(aString):
	'''
	>>> extractStateName('<a href="http://www.ipl.org/div/stateknow/nv1.html">Nevada</a>')
	'Nevada'

	>>> extractStateName('<a href="http://www.ipl.org/div/stateknow/nh1.html">New Hampshire</a>')
	'New Hampshire'
	
	>>> extractStateName('<a href="http://www.ipl.org/div/stateknow/dc1.html">Washington D.C.</a>')
	'Washington D.C.'
	
	>>> extractStateAbbr('') == None
	True
	
	'''
	pattern = r'html">[\w .]*</a>'
	match = re.search(pattern, aString)
	if match:
		result = match.group()
		return result[6:-4]
	else:
		return None
		
# returns state abbreviation from string
def extractStateAbbr(aString):
	'''
	>>> extractStateAbbr('<a href="http://www.ipl.org/div/stateknow/nv1.html">Nevada</a>')
	'NV'
	
	>>> extractStateAbbr('') == None
	True
	
	'''
	pattern = r'/\w\w1\.html'
	match = re.search(pattern, aString)
	if match:
		result = match.group()
		return result[1:3].upper()
	else:
		return None

# returns state population from string
def extractStateStats(aString):
	'''
	>>> extractStateStats('Nebraska</a></td><td class="sk_popchart">182,634.1</td></tr>')
	182634
	
	>>> extractStateStats('') == None
	True
	
	'''
	pattern = r'chart">[\d,.]*</td></tr>'
	match = re.search(pattern, aString)
	if match:
		result = match.group()
		result = result.replace(",","")
		return int(float(result[7:-10]))
	else:
		return None


# takes a list of strings and returns a dictionary
# which contains the relevant state data
def linesToDict(myList):
	'''
	>>> linesToDict(['/ca1.html">California</a></td><td class="sk_popchart">37,253,956</td></tr>'])
	{'CA': ['California', 37253956]}

	'''
	resultsDict = {}
	#print myList
	for c in myList:
		abbr = extractStateAbbr(c)
	#	print abbr
		if abbr is not None:
			stateName = extractStateName(c)
			stateStats = extractStateStats(c)
			resultsDict[abbr] = [stateName, stateStats]
	#print resultsDict
	return resultsDict


# reads a file and returns a list
def fileToList(filename):
	'''
	>>> fileToList('dummyFile.txt')
	['one\\n', 'two\\n']
	
	'''
	f = open(filename)
	contentsList = f.readlines()
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
