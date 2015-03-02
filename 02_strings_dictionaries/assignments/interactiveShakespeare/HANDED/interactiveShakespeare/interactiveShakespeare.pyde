import os
import logic

keyword = ''
fullWorksOfShakespeare = {}

def setup():
    #1. set the size of the canvas to 500,700
    #2. set the background to black
    #3. set the stroke to black
    #4. set the fill to red
    listOfFiles = os.listdir("data") #gets all the filenames inside the data directory and stores them in a list
    #5. call the filesToDict function inside the logic module and store the returning dictionary inside the fullWorksOfShakespeare variable 

def draw():
    pass
    
def updateResults(keyword):
    #6. set the background to black
    #7. call the freqAnalyzer function inside the logic module passing it the fullWorksOfShakespeare dictionary variable and the keyword variable and store it in a variable called results
    #8. calculate the bar width dividing the height by the number of items in the results dictionary (hint: you can use the len command

    for i in range(len(results.items())):
        #9. get the ith key inside the results dictionary and store it in a variable called opusName
        #10. get the ith value inside the results dictionary and store it in a variable called freq
        mappedFreq = map(freq, min(results.values()), max(results.values()), 0, width) #this calculates how long in pixel the bar for each result should be
        #11. set the fill to red
        rect(0, barWidth*i, mappedFreq, barWidth) #draws the rect in the right position and right length
        #12. set the fill to white to prepare for text writing
        text(opusName, 10, barWidth*i+15) #writes the name of Shakespeare's work
        text("(" + str(freq) + ")", 20 + textWidth(opusName), barWidth*i+15) #writes the frequency with which it appeared
        text(keyword, width - (textWidth(keyword)+10), 15)  #prints the keyword on the top right part of the screen
        
#this function adds all letters the user presses inside the 'keyword' variable
#and sends the updated variable to the updateResults() fuction
#when RETURN is pressed the 'keyword' variable is emptied
def keyPressed():
    if key==ENTER:
        keyword = ''
    elif (key>='a' and key<='z') or key==' ':
        keyword += key
        updateResults(keyword)
