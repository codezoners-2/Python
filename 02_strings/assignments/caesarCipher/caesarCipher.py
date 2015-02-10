alphabet = "abcdefghijklmnopqrstuvwxyz"
secretMessage = "Help me Obi Wan Kenobi, you're my only hope!"

#####################
# PART A
def caesarCipher(string, shift):
	result = ""
	for c in string:
		position = alphabet.find(c)
		if position > -1:
			position = position + shift
			position = position % len(alphabet)
			result = result + alphabet[position]
		else: result += c
	return result

print caesarCipher(secretMessage, 26)

#the following line should shift all letters by one position
# and print: "Ifmq nf Pcj Xbo Lfopcj, zpv'sf nz pomz ipqf!"
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
