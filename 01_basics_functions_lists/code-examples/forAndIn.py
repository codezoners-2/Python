########### Looping through a numbers list ########### 
myList = [5, 10, 19, 26]
sum = 0
for number in myList:
	sum += number
print sum

print "------------"

########### While loop ###########
sum = 0
i = 0
while i < len(myList):
	sum += myList[i]
	i+=1
print sum

print "------------"

########### Checking for list membership ########### 
myOtherList = ["Athens", "Berlin", "London", "Krakow"]
if "Athens" in myOtherList:
	print "Athens is in myOtherList"

print "------------"

########### Range ###########
for i in range(5):
	print i
