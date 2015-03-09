import os
import logic

keyword = ''
fullWorksOfShakespeare = {}

def setup():
    size(500,700)
    background(0)
    stroke(0)
    fill(255,0,0)    
    listOfFiles = os.listdir("data")
    global fullWorksOfShakespeare
    fullWorksOfShakespeare = logic.filesToDict(listOfFiles)

def draw():
    pass
    
def updateResults(keyword):
    background(0)
    results = logic.freqAnalyzer(fullWorksOfShakespeare, keyword)
    spacing = height/len(results)

    for i, (opusName, freq) in enumerate(results.items()):
        mappedFreq = map(freq, min(results.values()), max(results.values()), 0, width)
        fill(255,0,0)
        rect(0, spacing*i, mappedFreq, spacing)
        fill(255)
        text(opusName, 10, spacing*i+15)
        text("(" + str(freq) + ")", 20 + textWidth(opusName), spacing*i+15)
        text(keyword, width - (textWidth(keyword)+10), 15) 

def keyPressed():
    global keyword
    if key==ENTER:
        keyword = ''
    elif (key>='a' and key<='z') or key==' ':
        keyword += key
        updateResults(keyword)
