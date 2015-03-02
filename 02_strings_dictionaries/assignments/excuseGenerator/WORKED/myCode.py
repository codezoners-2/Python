# STEP 2
def fileToString(filename):
	"""
	>>> print fileToString("testRead.txt")
	one
	two
	
	"""
	return open(filename).read().strip()
	
# STEP 3
def stringToDict(string):
	"""
	>>> print stringToDict(fileToString('testDict.txt')) ==	{'student_name': 'Robert', 'teacher_name': 'Smith'}
	True

	"""
	return {s.split(":")[0]:s.split(":")[1] for s in string.split()}


# STEP 4
#template = fileToString("excuseTemplate.txt")
#dataDict = stringToDict(fileToString("simpleData.txt"))
#finalText = template.format(**dataDict)

# STEP 5
