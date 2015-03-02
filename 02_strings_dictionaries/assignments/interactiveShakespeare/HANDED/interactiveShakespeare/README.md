# interactive Shakespeare

Create an interactive application that counts the number of times a string is mentioned in the complete works of shakespeare and maps the results. To complete this we have separated the front-end from the back-end. Each does what's necessary:
* back-end: we'll write two functions:
    * `filesToDict(listOfFiles)` function that reads all the works of Shakespeare and stores the contents in a dictionary where the keys are the titles of the works and the corresponding values the text of each work
    * `freqAnalyzer(content, keyword)` function that takes a dictionary like the one created in the previous function and creates a new one which contains how many times the `keyword` appearred in each work
* front-end: it's processing.py program that takes the dictionary created from the `freqAnalyzer(content, keyword)` step and visualizes the results

## To begin follow these steps:

1. Open the logic.py file. This file contains all the brains behind our application. This is where the file reading and frequency calculating is taking place.
  * in the `filesToDict(listOfFiles)` function start by writing a test **first**. The test should take a list of filenames (testRead1.txt and testRead2.txt are provided) and return the contents. Make the test fail first and start with the next step. (Hint: you test the file by running the `python -m doctest logic.py` command). **ATTENTION**: since the files have new line characters `\n` you'll have to add these in the string with which you compare. But because we are in doctest mode when we do this comparison you'll need to add two slashes like this: `\\n` when you want to represent a new line character.
  * write code that reads the files in the `listOfFiles` list. Follow these steps, taking into account the indentation:
    * create an empty dictionary called `resultsDict`
    * create a for loop which goes over the list of files in the list `listOfFiles` and for each item `filename`...
      * read the contents of the file `filename` and store them in a variable called `contents`
      * close the file
      * add an entry to the dictionary with a key of `filename` and a value of `contents` (from the previous step)
    * return the `resultsDict`
2. Write a function that counts the frequency of a word in each entry in the dictionary.
  * In the `freqAnalyzer(content, keyword)` function start by writing a test **first**. The test could take the output of the previous function as provided in the previous test (that will be the content) and the keyword should be the word "tHree" (H is done in capital on purpose.)
  * If the test fails you are ready to write the code of the function. Follow these steps paying attention to the indentation provided:
    * create an empty dictionary `resultsDict` to store the results
    * create a for loop for each item `title` in the dictionary's **list of keys** (how do we get the list of all the keys? - Look it up!)
      * for each `key` in the dictionary get the corresponding value and store it in a variable called `text`
      * make the `text` all lower case. (Hint: you can use the `lower()` - look up how it's used!)
      * make sure the `keyword` parameter passed to the function is also lower case by making it so
      * search the `text` for the `keyword` word (Hint: you can use the `count()` function). Store the return value in a variable called `freq`
      * add an entry to the dictionary with a key of `title` and a value of `freq`
    * return the `resultsDict`
3. You can already play with your code in the command line. If you type: `python logic.py data/*` in the command line it will ask you for a word and it will return the number of times that word appears in each of the works of Shakespeare in the data folder.
4. Time to work on the front-end using Processing.py. Open the *interactiveShakespeare.pyde* file and complete the steps outlines in there. **Important**: you can write the answer replacing each of the comment lines I have written. You don't need more lines than that.

**BONUS**: Can you think of better ways to visualize the data? Perhaps using other geometric shapes?

**copyright [Theodoros Papatheodorou](contact@artech.cc)**
