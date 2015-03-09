import sys
from logic import *

def main():
	arguments = sys.argv[1:]
	
	if not arguments:
		print "correct usage: logic.py [files]"
		sys.exit(1)
	
	#ask the user for a string, save it in a variable called query (hint: use raw_input())
		
	fullWorksOfShakespeare = filesToDict(arguments[:-1])
	resultsDict = freqAnalyzer(fullWorksOfShakespeare, query) 

	for title in resultsDict.keys():
		print title + ": " + str(resultsDict[title])
	
	#initialize an empty string called htmlCode
	
	#add to the htmlCode variable a level 3 heading with the text "searched for: " followed by the contents of the query variable
	
	#loop over the keys/title in the resultsDict and for each key/title:
		#store in a variable called 'freq' the frequency with which the query appeared in the contents of the title
		#store in a variable called 'maxFreq' the maximum frequency on the whole dictionary (hint: use the max() function on resultsDict.values())
		#store in a variable called 'minFreq' the minimum frequency on the whole dictionary (hint: use the min() function on resultsDict.values())
		#get rid of the text before the '\' (hint: you can use rfind() to locate the last '\' and then use slicing to keep the remaing string, store the result in a variable called 'fixedTitle'
		#add the fixedTitle to the htmlCode variable
		#add the necessary lines for adding a progress bar. Go the bootstrap page and see what is required. You'll discover that you have to use the current value (freq), max value, min value, all of which you have calculated above. Add that html code string to the htmlCode variable replacing the correct values in the required positions. (Hint: you can use the format() function for that) (Hint2: you can calculate the corresponding percentage for the progress bar by doing this when using format()--> percent=freq*100/maxFreq

	
	#open the file called bootstrap.html
	#read the contents of the file using the read() function, store them in a variable called bootTemplate
	#close the file
	#open a file called results.html in write mode
	#write the contents of the bootTemplate while applying the format function to it in order to replace the {results} withe the htmlCode contents
	#close the file

###BONUS###
# instead of creating graphs can you create a table with the values SORTED?
# use the http://getbootstrap.com/components/#panels-tables structure as a guide.
	
if __name__ == "__main__":
	main()
