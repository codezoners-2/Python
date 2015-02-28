# interactive Shakespeare

Create an interactive application that counts the number of times a string is mentioned in the complete works of shakespeare and maps the results. To begin follow these steps:

1. Open the logic.py file. This file contains all the brains behind our application. This is where the file reading and frequency calculating is taking place.
  * in the `readTemplate(filename)` function start by writing a test **first**. The test should take a list of files (testRead1.txt and testRead2.txt are provided) and return the contents. Make the test fail first and start with the next step. (Hint: you test the file by running the `python -m doctest logic.py` command)
  * write code that reads the files in the `listOfFiles` list. More specifically:
    * create an empty dictionary called `resultsDict`
    * create a for loop which goes over the list of files in the list `listOfFiles` and for each item `filename`...
      * read the contents of the file and store them in a variable
      * close the file
      * save the name of the file (`filename`) and the contents from the previous step
    * return the `retultsDict`

store all the filenames as keys in a dictionary and the contents as corresponding values.
    * return that dictionary
2. Write a function that counts the frequency of a word in each entry in the dictionary.
  * In the `freqAnalyzer(content, keyword)` function start by writing a test **first**. The test could take the output of the previous function as provided in the previous test (that will be the content) and the keyword should be the word "tHree" (H is done in capital on purpose.)
  * Create an empty dictionary to store the results. Call it resultsDict
  * Create a for loop to loop through all the values in the dictionary and use the `count()` function to measure how many times the `keyword` parameter is mentioned inside the value of the specific entry in the dictionary. Make sure you use the `lower()` function in order to make both sides of the `count()` function lowercase so that it ignores capitalization.
  * Add inside the for loop a line that stores the current key of the `content` dictionary and the return value of the `count()` function
  * Return resultsDict dictionary
3. You can already play with your code in the command line. If you type: `python logic.py data/*` in the command line it will ask you for a word and it will return the number of times that word appears in each of the works of Shakespeare in the data folder.
4. Time to work on the front-end using Processing.py. Open the *interactiveShakespeare.pyde* file and complete the steps outlines in there. **Important**: you can write the answer replacing each of the comment lines I have written. You don't need more lines than that.

**BONUS**: Can you think of better ways to visualize the data? Perhaps using other geometric shapes?

**copyright [Theodoros Papatheodorou](contact@artech.cc)**
