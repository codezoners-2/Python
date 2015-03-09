# State stats improved!

In this assignment you're asked to make your previous code a bit more efficient by using the group functionality of regex together with find all. Follow these steps:

1. Open up the new logic.py file I have provided. You'll notice it's quite similar to the old code, but with some important differences. I've removed all the functions that were getting out the state abbreviation, state name, statistics separately. We are going to write one function that will do all that. I have replaced the `filesToList(filename)` function with a `fileToString(filename)`. This function now just opens the html file and copies all of its contents to a string. We are then going to pass this to `extractData(aString)` to do all the work in one beautiful function.

2. Writing the `extractData()` function. Follow these steps:
  * write a test **first**. Now this function will take the whole contents of the file and should be able to process and return the structured results. Give to it a string extract from the file that contains at least two states, so that we're sure we're processing everything.
  * we still need a test for the empty string using the `is None` in case the string contains no matches
  * once both tests fail, your ready to write code. Start by creating an empty dictionary called `resultsDict`
  * write a pattern with with brackets that will be able to match the groups of characters you need. You can use IDLE, or a separate file to test mini test programs. Start first by still using the `re.search()` command to make sure you are at least matching one pattern correctly.
  * after you match the first pattern, replace `re.search()` with `re.findall()` and store the return value to `matchesList`. What structure does `matchesList` store at this point? Think about it!
  * if `matchesList is not None`:
    * loop over the matchesList and for all matches called `match`:
      * store the first element of the tuple, after making it capitalized in a variable called `abbr`
      * store the second element of the tuple in a variable called `stateName`
      * store the third element of the tuple in a variable called `number`, after using `replace()` to remove the commas and after turning it into a `float` and then into an `int` in order to get rid of the decimal point.
      * add an entry in `resultsDict` with key `abbr` and corresponding value the list containing `stateName` and `number` (in that order)
    * return `resultsDict`
  * `else: return None`

