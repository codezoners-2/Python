def askQuestion(a):
	if a == 'r' or a == 'R':
		print "you are brave!"
	else:
		print "chicken!"

myAnswer = raw_input("The red or the blue pill (r/b)? ")
askQuestion(myAnswer)
