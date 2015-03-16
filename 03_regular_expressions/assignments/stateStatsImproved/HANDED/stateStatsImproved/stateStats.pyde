import logic
state = True
landSizeDict = {}
popDict = {}
dataDict = {}
s = ""
                                
def setup():
    size(950,600)
    background(255)
    global s
    global landSizeDict
    global popDict
    
    s = loadShape("usMap.svg")    
    s.disableStyle()

    fileContents = logic.fileToList('landsize.html')
    landSizeDict = logic.linesToDict(fileContents)

    fileContents = logic.fileToList('population.html')
    popDict = logic.linesToDict(fileContents)

    dataDict = popDict

###############################        
def draw():
    background(255)
    if state: dataDict = landSizeDict
    else: dataDict = popDict

    maxVal = logic.getMaxValue(dataDict)
    minVal = logic.getMinValue(dataDict)      

    stroke(0)
    for stateAbbr in dataDict.keys():
        stateShape = s.getChild(stateAbbr)
        stateColorR = map(dataDict[stateAbbr][1], minVal, maxVal/3, 0, 255)
        stateColorB = map(dataDict[stateAbbr][1], minVal, maxVal/3, 255, 0)
        fill(stateColorR, 0, stateColorB)
        shape(stateShape)

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
