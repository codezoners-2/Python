
def askQuestion():
	myAnswer = raw_input("The red or the blue pill (r/b)? ")
	
	if myAnswer == 'r' or myAnswer == 'R':
		print "you are brave!"
	else:
		print "chicken!"


askQuestion()
