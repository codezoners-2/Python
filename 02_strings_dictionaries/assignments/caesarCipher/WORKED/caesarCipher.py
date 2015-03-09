alphabet = "abcdefghijklmnopqrstuvwxyz"

secretMessage = "Help me Obi Wan Kenobi, you're my only hope!"

#===========================================================
#simplified encoding only
def caesarCipherEncodeOnly(string, shift):
	result = ""
	for c in string:
		position = alphabet.find(c.lower())
		if position > -1:
			position = position + shift
			position = position % len(alphabet)
			if c.isupper(): result = result + alphabet[position].upper()
			else: result = result + alphabet[position]
		else: result += c
	return result

print caesarCipherEncodeOnly(secretMessage, 1)

#============================================================
#bidirectional Caesar (encode/decode)
def caesarCipherBi(string, shift, direction):
	newString = ""
	for c in string:
		position = alphabet.find(c.lower())
		if position > -1:
			if direction: position = position + shift
			else: position = position - shift
			position = position % len(alphabet)
			if c.isupper(): newString = newString + alphabet[position].upper()
			else: newString = newString + alphabet[position]
		else: newString += c
	return newString

print caesarCipherBi(caesarCipherBi(secretMessage, 1, True), 1, False)

#============================================================
#simplified Caesar (encode/decode) - using CAPS as part of alphabet

alphabetCAPS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesarCipherBiCapitals(string, shift, direction):
	newString = ""
	for c in string:
		position = alphabetCAPS.find(c)
		if position > -1:
			if direction: position = position + shift
			else: position = position - shift
			position = position % len(alphabetCAPS)
			newString = newString + alphabetCAPS[position]
		else: newString += c
	return newString

print caesarCipherBiCapitals(secretMessage, 20, True)
