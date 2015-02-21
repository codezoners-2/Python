# Excuse Generator

Use the excuseTemplate.txt file as a template to fill in various bit of data from the data.txt file. Steps:

1. manually edit the excuseTemplate.txt file to put the right markers ({0} or {keyword}) to use with the format() method
2. read the excuse template file:
  * write a function called `readTemplate(filename)`
  * write a doctest (FIRST!) passing the string "testRead.txt" to the function and testing against a printout of
  ```
  one
  two
  ```
  * Once you've written the test, write code that opens the file called *filename* for reading, reads all the lines (using `read()` - what does it return? Look it up!)
  * Use the `strip()` function (look it up) in order to remove all the whitespace from the end
  * Return the cleaned up string
3. convert the contents of simpleData.txt to a dictionary
  1. write a function called `dataToDict(filename)`
  2. write a doctest (FIRST!) passing the string *testDict.txt* to the function and testing against a dictionary printout of `{'student_name': 'Robert', 'teacher_name': 'Smith'}`
  3. write code inside the `dataToDict(filename)` function that reads a file using the `readlines()` function (what does `readlines()` return? Look it up!).
  4. Take what `readlines()` returns and convert it to a dictionary by using the `split()` function to separate the string before and after the colon.
  5. return the dictionary created
4. Uncomment the lines of this step in order to load the actual file data and to add to the template text the data of *simpleData.txt* file
5. Final touches:
  1. read the boostrap.html file using the `readTemplate()` function we previously created and store its contents into a variable called `bootstrap` (which is a string as a result).
  2. Open the html file in an editor and search for the {customText} tag. This is where the format function will insert our text. Close the editor.
  3. Use the format function along with the `bootstrap` (and the keyword `customText`) to generate a new string that contains the finalized html code along with our custom excuse text. Store the output of the format function in a variable called `result`
  4. Open a file called *excuse.html* (make sure you turn on the writing 'w' flag) and write the contents of the `result` variable in it.
  5. Open your *excuse.html* file in your browser.

**BONUS**: use the complexData.txt file instead of the simpleData.txt. Lines that have more than one word should be further split at the space and add for that key entry in the dictionary a list of the words. Each time the program is run it picks a random item from the list to generate the page. You can use the `randint()` method to pick one of the choices.

**copyright [Theodoros Papatheodorou](contact@artech.cc)**
