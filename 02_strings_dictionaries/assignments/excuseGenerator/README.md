# Excuse Generator

Use the excuseTemplate.txt file as a template to fill in various bit of data from the data.txt file. Open the *myCode.py* file and follow these steps:

1. manually edit the excuseTemplate.txt file to put the right markers ({0} or {keyword}) to use with the format() method. **Important**: In order for it to work you need to use the same keywords I have used inside the *simpleData.txt* file ({student_name}, {teacher_name}, {diseases}, etc). You'll see a bit later why this is necessary.
2. read the excuse template file:
  * write a function called `fileToString(filename)`
  * write a doctest **first**, passing the string "testRead.txt" to the function and testing against a printout of
  ```
  one
  two
  ```
  Hint: your test could be `print(fileToString("testRead.txt"))`
  * Once you've written the test  (Hint: you test the file by running the `python -m doctest myCode.py` command), write code that opens the file called `filename` for reading, reads all the lines (using `read()` - what does it return? Look it up!)
  * Use the `strip()` function (look it up) in order to remove all the whitespace from the end
  * Return the cleaned up string
3. convert the contents of a string to a dictionary
  * write a function called `stringToDict(string)`
  * write a doctest **first**, passing to the `stringToDict(string)` function the output of the function `fileToString('testDict.txt')` and test whether the equality (==) against a `{'student_name': 'Robert', 'teacher_name': 'Smith'}` returns True
  * write code inside the `stringToDict(string)` function that splits the string into a list of the lines it is made up of. (Hint: you'll need to use the `split()` function.
  * Time to create a dictionary which will contain the data we read from the file. Follow this steps as if they were code and respect the indentation I have provided:
  ```
    # create an empty dictionary called myDict
    # create a for loop and loop over the elements of the list created in the step involving the split() function above
      # for each element in the list use split again this time on ":" and save the result in a variable called row. row contains a list with the left and right part of the lines we split.
      # save the value of the first element of row in a variable called k
      # save the value of the second element of row in a variable called v
      # do myDict[k]=v so that you insert value v for key k in the dictionary      
  ```
  * return the dictionary created
4. Uncomment the lines of this step in order to load the actual file data and to add to the template text the data of *simpleData.txt* file
5. Final touches:
  * read the bootstrap.html file using the `fileToString()` function we previously created and store its contents into a variable called `bootstrap` (which is a string as a result).
  * Open the html file in an editor and search for the {customText} tag. This is where the format function will insert our text. Close the editor.
  * Use the format function along with the `bootstrap` (and the keyword `customText`) to generate a new string that contains the finalized html code along with our custom excuse text. Store the output of the format function in a variable called `result`
  * Open a file called *excuse.html* (make sure you turn on the writing 'w' flag) and write the contents of the `result` variable in it.
  * Open your *excuse.html* file in your browser.

**BONUS**: use the complexData.txt file instead of the simpleData.txt. Lines that have more than one word should be further split at the space and add for that key entry in the dictionary a list of the words. Each time the program is run it picks a random item from the list to generate the page. You can use the `randint()` method to pick one of the choices.

**copyright [Theodoros Papatheodorou](contact@artech.cc)**
