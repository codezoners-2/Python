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
    s = loadShape("usMap.svg")    
    s.disableStyle()

    #1 pass landsize.html to fileToString function from logic and store the results in fileContents
    global landSizeDict
    #2 pass fileContents to extractData from logic and store the results in landSizeDict

    #3 pass population.html to fileToString function from logic and store the results in fileContents
    global popDict
    #4 pass fileContents to extractData from logic and store the results in popDict
    global dataDict
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
        stateColor = map(dataDict[stateAbbr][1], minVal, maxVal/3, 225, 0)
        fill(stateColor, 0, 0)
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
