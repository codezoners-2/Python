## **Quick demo from me**

## State statistics
In this assignment you're asked to write code that opens two html files, reads their contents, extracts the required data and builds a dictionary of structured data so that is can be processed by the front-end. Start by following these steps:

1. Open in a text editor the files *population.html* and *landsize.html*. **Keep them open**. You'll be looking them again and again.

2. Create a function `extractStateName(aString)` which takes a string and returns the full name of a extracted state. Returns `None` if no match is found. Follow these steps:
  * study the data **first**. Take a look at what it is you are trying to extract. What similarities do you see between all the strings? What types of data are going to be the input to your regex?
  * knowing what types of data you are going to be processing, create a test **before** proceeding with code. **Attention**: some states are one word (Nevada), some are more than one (New Hampshire) and some include dots (Washington D.C.). Make tests for each of them. (Hint: you test the file by running the `python -m doctest logic.py` command)
  * You should also make a test for the empty string (simulating a no match). You can test if `is None` (copy-paste this code) returns `True` (just like we were doing dictionary comparisons). So you would have something like this in the test line: ```extractStateName('yourStringHere') is None```
  * Now that all the tests fail, you're ready to code. Open the *simpleRegex.py* example and see how a simple regex operation takes place. Copy that code and instead of the `print()` statements, have the code return the result. How could you deal with the fact that states are not always one word? (Hint: you could use square brackets[]).
  * Once you manage to extract the substring that's needed, you still have the patterns you used to identify where the state is. Since the length of these is standard, you can remove them using a simple slicing operation, and returning its result

3. Create a function `extractStateAbbr(aString)` which takes a string and returns the **capitalized** abbreviation of the state. Returns `None` if no match is found. Follow these steps:
  * study the data **first**. Take a look at what it is you are trying to extract. What similarities do you see between all the strings? You'll be using these similarities to extract the required data.
  * knowing what types of data you are going to be processing, create a test **before** proceeding with code. Make sure the returning value in the test is capitalized.
  * You should also make a test for the empty string (simulating a no match). You can test if `is None` (copy-paste this code) returns `True` (just like we did for `extractStateName(aString)`
  * Now that all the tests fail, you're ready to code. Write a regex that extracts the substring you need.
  * Use slicing to get rid of the surrounding characters and return the capitalized result? How do we capitalize a string?

4. Create a function `extractStateStats(aString)` which takes a string and returns the statistics/number associated with a state. Returns `None` if no match is found. Follow these steps:
  * study the data **first**. Take a look at what it is you are trying to extract. What similarities do you see between all the strings? You'll be using these similarities to extract the required data.
  * create a test **before** proceeding with code. The returning value in this test should be a number (not a string)
  * you should also make a test for the empty string (simulating a no match). Test for `None` as we did above.
  * now that all the tests fail, you're ready to code. Write a regex that extracts the substring you need. Notice the numbers in both files contain commas `,` and that one of the files' numbers contain periods `.`. You'll need to take that into consideration. What could you use?
  * once you number is extracted use slicing to remove the excess characters.
  * Python doesn't deal well with `,`. Before returning the number use the `replace()` function to replace the `,` with an empty string, effectively removing the `,`.
  * convert the resulting, lean string to a float, then to an int (getting rid of the decimal) and return that value

5. Create a function `linesToDict(myList)` which takes a list of strings and returns the data we need in a well structured dictionary.
  * start designing a test **first**. We want this function to take a list of strings, so put **1** example string, in a 1 element **list** in the test and have it expect something like this: `{'CA': ['California', 37253956]}`. What the function should return is a dictionary whose keys are the capitalized state abbreviations and whose values are the full name and statistics of the states in a list of length 2.
  * Once your test fails, start by writhing the code following these steps (pay attention to the indentation):
  * create an empty dictionary `resultsDict`
  * loop over `myList` and for each element `c` in the list
    * call `extractStateAbbr`, passing to it `c` and store the returning value to `abbr`
    * copy-paste this: `if abbr is not None:` (if we actually found a state abbreviation we try getting the other values)
      * call the `extractStateName` passing `c` and store the returning value to `stateName`
      * call the `extractStateStats` passing `c`  and store the returning value to `stateStats`
      * add an entry with key `abbr` in the `resultsDict` with value equal to a list made up of `stateName` and `statePop`
  * return `resultsDict`

6. Create a `fileToList(filename)` function following these steps:
  * start by writing a test **first**. The test should take a file name (*dummyFile.txt* is provided for that reason) and return the contents organized as a **list**. Make the test fail first and start with the next step. **ATTENTION**: since the files have new line characters `\n` you'll have to add these in the returning list of the doctest. But because we are in doctest mode when we do this comparison you'll need to add two slashes like this: `\\n` when you want to represent a new line character.
  * write code that reads the contents of `filename`. In these steps, you'll need to open the file, store the contents in a variable called `contentsList` using the `readlines()` function, close the file and return `contentsList`

6. You can already now run your program in the command line by running `python logic.py` and you'll get a list of all the states and their stats. That's possible because of the `main()` function I have written. Take a look at it.

7. We need to do two more things before we go to the front-end. I have already written a `getMaxValue(aDict)` function. Can you complete (including the test) the `getMinValue(aDict)` function who's definition is provided already?

8. Now open the Processing.py IDE and replace the comments provided with code. You're almost there
