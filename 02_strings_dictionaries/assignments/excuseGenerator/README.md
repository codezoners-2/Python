# Excuse Generator

Use the excuseTemplate.txt file as a template to fill in various bit of data from the data.txt file. Open the *myCode.py* file and follow these steps:

1. manually edit the excuseTemplate.txt file to put the right markers ({0} or {keyword}) to use with the format() method
2. read the excuse template file:
  * write a function called `fileToString(filename)`
  * write a doctest **first**, passing the string "testRead.txt" to the function and testing against a printout of
  ```
  one
  two
  ```
  * Once you've written the test  (Hint: you test the file by running the `python -m doctest logic.py` command), write code that opens the file called `filename` for reading, reads all the lines (using `read()` - what does it return? Look it up!)
  * Use the `strip()` function (look it up) in order to remove all the whitespace from the end
  * Return the cleaned up string
3. convert the contents of a string to a dictionary
  * write a function called `stringToDict(string)`
  * write a doctest **first**, passing to the `stringToDict(string)` function the output of the function `fileToString('testDict.txt')` and test against a dictionary printout of `{'student_name': 'Robert', 'teacher_name': 'Smith'}`
  * write code inside the `stringToDict(string)` function that splits the string into a list of the lines it is made up of. (Hint: you'll need to use the `split()` function.
  * create an empty dictionary and loop over the elements of the list created in the previous step populating the dictionary. You'll need to use `split()` again to split each line at the `:` to take the key and the value for the dictionary
  * return the dictionary created
4. Uncomment the lines of this step in order to load the actual file data and to add to the template text the data of *simpleData.txt* file
5. Final touches:
  * read the boostrap.html file using the `fileToString()` function we previously created and store its contents into a variable called `bootstrap` (which is a string as a result).
  * Open the html file in an editor and search for the {customText} tag. This is where the format function will insert our text. Close the editor.
  * Use the format function along with the `bootstrap` (and the keyword `customText`) to generate a new string that contains the finalized html code along with our custom excuse text. Store the output of the format function in a variable called `result`
  * Open a file called *excuse.html* (make sure you turn on the writing 'w' flag) and write the contents of the `result` variable in it.
  * Open your *excuse.html* file in your browser.

**BONUS**: use the complexData.txt file instead of the simpleData.txt. Lines that have more than one word should be further split at the space and add for that key entry in the dictionary a list of the words. Each time the program is run it picks a random item from the list to generate the page. You can use the `randint()` method to pick one of the choices.

**copyright [Theodoros Papatheodorou](contact@artech.cc)**