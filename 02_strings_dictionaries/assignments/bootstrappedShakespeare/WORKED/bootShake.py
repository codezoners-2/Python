import sys
from logic import *

def main():
	arguments = sys.argv[1:]
	
	if not arguments:
		print "correct usage: bootShake.py [files]"
		sys.exit(1)
	
	query = raw_input("enter search term: " )
		
	fullWorksOfShakespeare = filesToDict(arguments[:-1])
	resultsDict = freqAnalyzer(fullWorksOfShakespeare, query) 

	for title in resultsDict:
		print title + ": " + str(resultsDict[title])
	
	htmlCode = ''
	
	htmlCode += '<h3>searched for: '+ query +'</h3>'
	
	for title in resultsDict.keys():
		freq = resultsDict[title]
		maxFreq = max(resultsDict.values())
		minFreq = min(resultsDict.values())
		fixedTitle = title[title.rfind('/')+1:]
		htmlCode += fixedTitle

		progressBarCode = '''<div class="progress">
		<div class="progress-bar" role="progressbar" aria-valuenow="{now}" aria-valuemin="{minV}" aria-valuemax="{maxV}" style="width: {percent}%;">
		{percent}%
		</div>
		</div>
		'''
		htmlCode += progressBarCode.format(now=freq, minV=minFreq, maxV=maxFreq, percent=freq*100/maxFreq)
	
	f = open('bootstrap.html')
	bootstraptemplate = f.read()
	f.close()
	f = open('results.html', 'w')
	f.write(bootstraptemplate.format(results=htmlCode))
	f.close()
	
if __name__ == "__main__":
	main()
