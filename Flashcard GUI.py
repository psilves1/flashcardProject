# Beta Development v1.1

from tkinter import *

master = Tk()
master.title('Flashcard Beta Development V1.1')
master.geometry("500x400")
master.iconbitmap(r'flashcard.ico')

wordList = []
definitionList = []

global wordNum
wordNum = 0

#Functions
def clearFunction(*event):
    word.delete(0, END)  # Clears from the first value to the last one
    definitionEntry.delete(0, END)


def submitFunction(*event):
    wordList.append(word.get())
    definitionList.append(definitionEntry.get())
    clearFunction()


def testFunction(*event,wordNum = wordNum):
    try:
        testWordLabel.config(text=wordList[wordNum])
        testDefinitionLabel.config(text=definitionList[wordNum])
        showDefinitionforTest()
        nextButton.place(x=125, y=200)
        deleteButton.place(x =200, y = 200)
        test.place_forget()
    except IndexError:
        popUpBox("You need to add words before you test!")


def hideDefinition(*event):
    testDefinitionLabel.place_forget()
    hideDefinitionButton.place_forget()
    showDefinitionButton.place(x=10, y=200)


def showDefintion(*event):
    showDefinitionButton.place_forget()
    testDefinitionLabel.place(x=10, y=250)
    hideDefinitionButton.place(x=10, y=200)


def showDefinitionforTest(*event): #This is different from the one above it because this is for when the test button is clicked
    testWordLabel.place(x=10, y=150)
    showDefinitionButton.place(x=10, y=200)


def nextButtonFunction(*event):
    try:
        global wordNum
        testWordLabel.config(text=wordList[wordNum+1])#It does this because the program is already showing the variable at the current wordNum variable so you want to get the next one in the list
        testDefinitionLabel.config(text=definitionList[wordNum+1])
        wordNum += 1
        if(wordNum+1 == len(wordList)):
            wordNum=-1 #It is negative 1 so that when you add 1 to it, the sum is 0, so in the confiq functions above, you can start at the first value
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


def deleteButtonFunction():

    if(len(wordList) >= 2): #It must be greater than 2 so that there is still one left over to display to the user
        print(wordNum, '\n', wordList)
        del wordList[wordNum]
        del definitionList[wordNum]
        print(wordNum, '\n', wordList)
        testFunction() #This function updates the label to the item that took the deleted item's place in the list
    else:
        popUpBox("You cannot delete that!")





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

deleteButton = Button(master, text="Delete", command = deleteButtonFunction)

nextButton = Button(master, text="Next Word", command = nextButtonFunction)






master.mainloop()
