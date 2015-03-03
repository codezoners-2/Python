import sys

def filesToDict(listOfFiles):
	'''
	>>> filesToDict(['testRead1.txt','testRead2.txt']) == {'testRead1.txt': 'one\\ntwo\\n', 'testRead2.txt': 'three\\nfour\\nthree\\n'}
	True
	
	'''
	resultsDict = {}
	for filename in listOfFiles:
		fileHandler = open(filename, 'r')
		fileContents = fileHandler.read()
		fileHandler.close()
		resultsDict[filename]=fileContents
	return resultsDict
	
	# alternative, more pythonic solution:
	#return {f: open(f).read() for f in listOfFiles }

def freqAnalyzer(fullWorksDict, keyword):
	'''
	>>> freqAnalyzer({'testRead1.txt': 'one\\ntwo\\n', 'testRead2.txt': 'three\\nfour\\nthree\\n'}, 'tHree') == {'testRead1.txt': 0, 'testRead2.txt': 2}
	True
	
	>>> freqAnalyzer(filesToDict(['testRead1.txt','testRead2.txt']), 'tHree') == {'testRead1.txt': 0, 'testRead2.txt': 2}
	True
	
	'''
	resultsDict = {}
	for title in fullWorksDict.keys():
		text = fullWorksDict[title]
		text = text.lower()
		keyword = keyword.lower()
		freq = text.count(keyword)
		resultsDict[title] = freq
	return resultsDict
	
	# alternative, more pythonic solution:	
	#return {opusName: content.lower().count(keyword.lower()) for opusName, content in fullWorksDict.items()}
	

def main():
	arguments = sys.argv[1:]
	
	if not arguments:
		print "wrong usage"
		sys.exit(1)

	fullWorksOfShakespeare = filesToDict(arguments)
	for opusName, freq in freqAnalyzer(fullWorksOfShakespeare, raw_input("enter keyword: ")).items():
		print opusName + ": " + str(freq)

if __name__ == "__main__":
	main()
