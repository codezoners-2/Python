import sys

def filesToDict(listOfFiles):
	'''
	test by passing a list containing the two test text files and make sure
	that the dictionary returned is the one you expect
	>>> filesToDict(___________________________) == { _____________________________ }
	"what should it return?"
	
	'''
	pass

def freqAnalyzer(content, keyword):
	'''
	pass to it the dictionary from the previous step and the value 'tHree' (preserve the capitalization)
	>>> freqAnalyzer(filesToDict(['testRead1.txt','testRead2.txt']), 'tHree')
	"what should it return?"
	
	'''
	pass


# the following lines are to test that the above work with shakespeare's text
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
