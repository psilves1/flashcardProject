# Beta Development v1.1

from tkinter import *

master = Tk()
master.title('Flashcard Beta Development V1.1')
master.geometry("500x400")
master.iconbitmap(r'flashcard.ico')

wordList = []
definitionList = []

wordNum = 0

#Functions
def clearFunction(event = 0):
    word.delete(0, END)  # Clears from the first value to the last one
    definition.delete(0, END)

def submitFunction(event = 0):
    wordList.append(word.get())
    definitionList.append(definition.get())
    clearFunction()

def testFunction(event = 0, wordNum = wordNum):
    try:
        testWordLabel.config(text=wordList[wordNum])
        testDefinitionLabel.config(text=definitionList[wordNum])
        showDefinitionforTest()
        nextButton.place(x=125, y=200)
        test.place_forget()
    except IndexError:
        popUpBox("You need to add words before you test!")

def hideDefinition(event = 0):
    testDefinitionLabel.place_forget()
    hideDefinitionButton.place_forget()
    showDefinitionButton.place(x=10, y=200)

def showDefintion(event = 0):
    showDefinitionButton.place_forget()
    testDefinitionLabel.place(x=10, y=250)
    hideDefinitionButton.place(x=10, y=200)

def showDefinitionforTest(): #This is different from the one above it because this is for when the test button is clicked
    testWordLabel.place(x=10, y=150)
    showDefinitionButton.place(x=10, y=200)

def nextButtonFunction(event = 0, wordNum = wordNum):
    try:
        testWordLabel.config(text=wordList[wordNum])
        testDefinitionLabel.config(text=definitionList[wordNum])
        wordNum += 1
        if (wordNum == len(wordList)):
            wordNum = 0
    except IndexError:
        popUpBox(message="You must add another\n word and definition")

def popUpBox(message = "An Error Occured!"):
    popUp = Toplevel()
    popUp.geometry("220x100")
    popUp.title('')
    warningMessage = Label(popUp, text=message, font=40)
    warningMessage.place(x=5, y=5)
    okButton = Button(popUp, text="OK", command = popUp.destroy)
    okButton.place(x=90, y=70)

#Labels
directionLabel = Label(master, text="Welcome to my Flashcard application.")
directionLabel.place(x=10, y=10)

wordLabel = Label(master, text="Word:")
wordLabel.place(x=40, y=50)

testWordLabel = Label(master)
testDefinitionLabel = Label(master)

definitionLabel = Label(master, text="Definition:")
definitionLabel.place(x=17.3, y=75)  # X is a weird number so that the ends of WordLabel and Definition label are equal

#Entries
definitionEntry = Entry(master)
definitionEntry.place(x=80, y=75)

word = Entry(master)
word.place(x=80, y=50)

#Buttons
submit = Button(master, text="Submit", command = submitFunction)
submit.place(x=35, y=100)

clear = Button(master, text="Clear", command = clearFunction)
clear.place(x=95, y=100)

test = Button(master, text="Test", command = testFunction)
test.place(x=150, y=100)

hideDefinitionButton = Button(master, text="Hide Definition", command = hideDefinition)

showDefinitionButton = Button(master, text="Show Definition", command = showDefintion)

nextButton = Button(master, text="Next Word", command = nextButtonFunction)




master.mainloop()
