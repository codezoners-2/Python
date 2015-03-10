#1 import the logic module
state = True
#2 create an empty landSizeDict
#3 create an empty popDict
#4 create an empty dataDict
s = ""
                                
def setup():
    size(950,600)
    background(255)
    global landSizeDict
    global popDict
    global s
    
    s = loadShape("usMap.svg")    
    s.disableStyle()

    #5 pass landsize.html to fileToList function from logic and store return value in fileContents
    #6 pass fileContents to linesToDict function from logic and store return value in landSizeDict dictionary

    #7 pass population.html to fileToList function from logic and store return value in fileContents
    #8 pass fileContents to linesToDict function from logic and store return value in popDict dictionary

    dataDict = popDict

###############################        
def draw():
    background(255)
    if state: dataDict = landSizeDict
    else: dataDict = popDict

    #9 pass dataDict to getMaxValue from logic and store return value in maxVal
    #10 pass dataDict to getMinValue from logic and store return value in minVal  

    #11 set stroke to black
    #12 for all keys 'stateAbbr' in dataDict:
        stateShape = s.getChild(stateAbbr)
        #13 get the list corresponding to the stateAbbr key in dataDict and store the second element (the number) in dataVal
        stateColor = map(dataVal, minVal, maxVal/3, 225, 0)
        fill(stateColor, 0, 0)
        shape(stateShape)

    #code that prints units/scale at bottom right corner - ignore
    noStroke()
    pushMatrix()
    translate(width-(80*5)-10, height-10)
    text("{:,}".format(int(maxVal)), 0, -5)
    text("{:20,}".format(int(minVal)), (80*5)-100, -5)
    for i in range(80):
        fill(map(i, 0, 80, 0, 225), 0, 0)
        rect(i*5, 0, 5, 20)
    popMatrix()

####################################
def mousePressed():
    global state
    state = not state
    if state==True: dataDict = landSizeDict
    else: dataDict = popDict
