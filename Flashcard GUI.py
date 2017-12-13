# Beta Development v1.1

from tkinter import *

master = Tk()
master.title('Flashcard Beta Development V1.1')
master.geometry("500x400")
master.iconbitmap(r'flashcard.ico')

wordList = []
definitionList = []

global numOfTestClicks
numOfTestClicks = 0

global wordNum
wordNum = 0


def clearFunction(event):
    word.delete(0, END)  # Clears from the first value to the last one
    definition.delete(0, END)


def clearForSubmitFunction():
    word.delete(0, END)
    definition.delete(0, END)


def submitFunction(event):
    wordList.append(word.get())
    definitionList.append(definition.get())
    clearForSubmitFunction()


def testFunction(event):
    global wordNum
    testWordLabel.config(text=wordList[wordNum])
    testDefinitionLabel.config(text=definitionList[wordNum])
    global numOfTestClicks
    if (numOfTestClicks == 0):
        showDefinitionforTest()
    numOfTestClicks += 1
    wordNum += 1
    nextButton.place(x=125, y=200)
    test.place_forget()


def hideDefinition(event):
    testDefinitionLabel.place_forget()
    hideDefinitionButton.place_forget()
    showDefinitionButton.place(x=10, y=200)


def showDefintion(event):
    showDefinitionButton.place_forget()
    testDefinitionLabel.place(x=10, y=250)
    hideDefinitionButton.place(x=10, y=200)


def showDefinitionforTest():
    testWordLabel.place(x=10, y=150)
    showDefinitionButton.place(x=10, y=200)


def nextButtonFunction(event):
    global wordNum
    testWordLabel.config(text=wordList[wordNum])
    testDefinitionLabel.config(text=definitionList[wordNum])
    wordNum += 1
    if (wordNum == len(wordList)):
        wordNum = 0

#def deleteButtonFunction(event):


direction = Label(master, text="Welcome to my Flashcard application.")
direction.place(x=10, y=10)

wordLabel = Label(master, text="Word:")
wordLabel.place(x=40, y=50)

word = Entry(master)
word.place(x=80, y=50)

definitionLabel = Label(master, text="Definition:")
definitionLabel.place(x=17.3, y=75)  # X is a weird number so that the ends of WordLabel and Definition label are equal

definition = Entry(master)
definition.place(x=80, y=75)

submit = Button(master, text="Submit")
submit.bind('<Button-1>', submitFunction)
submit.bind('<Return>', submitFunction)
submit.place(x=35, y=100)

clear = Button(master, text="Clear")
clear.bind('<Button-1>', clearFunction)
clear.place(x=95, y=100)

test = Button(master, text="Test")
test.bind('<Button-1>', testFunction)
test.place(x=150, y=100)

testWordLabel = Label(master, text="W")

testDefinitionLabel = Label(master, text='D')

hideDefinitionButton = Button(master, text="Hide Definition")
hideDefinitionButton.bind('<Button-1>', hideDefinition)

showDefinitionButton = Button(master, text="Show Definition")
showDefinitionButton.bind('<Button-1>', showDefintion)

nextButton = Button(master, text="Next Word")
nextButton.bind('<Button-1>', nextButtonFunction)

master.mainloop()
