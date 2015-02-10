alphabet = "abcdefghijklmnopqrstuvwxyz"
secretMessage = "Help me Obi Wan Kenobi, you're my only hope!"

def myFunc():
	pass
	if 1=1:
		

myFunc()

#####################
# PART A
# define a function caesarCipher that takes 2 parameters called: string, shift
	# create an empty string to store the results - call it "result"
	# create a for loop that loops through all characters ("c") in the parameter "string"
		# search for the lower-cased "c" in the alphabet using the find command and store the outcome in a variable called "position"
		# if "position" is > -1 (ie. character "c" exists in the string "alphabet") then...
			# add the number equal to the one stored in "shift" to the variable "position"- to actually do the encryption
			# do a modulus with the length of the alphabet in order to start from the beginning once you pass the end of the "alphabet" list
			# if character "c" is upper case then...
				# add the character at location "position" in the "alphabet" string to the "results" string, but turn it to upper case first
			# (SWITCH DRIVER/NAVIGATOR ROLES HERE and for the rest of the exercise)
			# otherwise (if it is lower case) just simply add it to the "result" string
		# else if the character does not exist (position==-1) add it unprocessed to the "result" list. This adds the "?" and the spaces.
	# return "result"

#the following line should shift all letters by one position
# and print: "Hfmq nf Ocj Wbo Kfopcj, zpv'sf nz pomz ipqf!"
# print caesarCipher(secretMessage, 1)

######################
# PART B
# Once you are done with the encryption, add a decryption ability.
# The code is pretty much the same. All you'll need to do is add 
# functionality for doing the opposite. Here are some hints:
# * Add a 3rd variable called "direction" in the function's definition.
# * Pass a True or False value as a "direction" parameter when you call the function
# * When it's "True" you'll ADD "shift" to the "position" variable
# * When it's "False" you'll SUBTRACT "shift" from the "position" variable

# this command should return your original string:
# print caesarCipher(caesarCipher(secretMessage, 1, True), 1, False)
