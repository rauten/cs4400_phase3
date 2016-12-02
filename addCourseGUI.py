from tkinter import *

rootWin = Tk()
rootWin.title("CS 4400 Add a Project")

smallFrame = Frame(rootWin)
smallFrame.grid(row=0, column=0)
titleReg = Label(smallFrame,text="Add a Course", padx= 45, pady=10, font=16)
titleReg.grid(row=0, column= 1, sticky = W)

courseNumberEntry = Entry(smallFrame, width=30)
courseNumberEntry.grid(row=1, column=1, sticky=W, pady=5)
courseNumberLabel = Label(smallFrame, text="Course Number:")
courseNumberLabel.grid(row=1, column=0, sticky=E, padx=5, pady=5)

courseNameEntry = Entry(smallFrame, width=50)
courseNameEntry.grid(row=2, column=1, sticky=W, pady=5)
courseNameLabel = Label(smallFrame, text="Course Name:")
courseNameLabel.grid(row=2, column=0, sticky=E, padx=5, pady=5)

instructorEntry = Entry(smallFrame, width=50)
instructorEntry.grid(row=3, column=1, sticky=W, pady=5)
instructorLabel = Label(smallFrame, text="Instructor:")
instructorLabel.grid(row=3, column=0, sticky=E, padx=5, pady=5)

Label(smallFrame, text = "Designation:").grid(row = 4, column = 0, sticky=E, padx = 5, pady = 5)
designationChoices = StringVar(smallFrame)
designation = {'Pizza','Lasagne','Fries','Fish','Potatoe'}
designationChoices.set('None')
popupMenu = OptionMenu(smallFrame, designationChoices, *designation)
popupMenu.grid(row = 4, column =1, sticky = W)

Label(smallFrame, text = "Category: ").grid(row = 5, column = 0, sticky=E, padx = 5, pady = 5)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(smallFrame, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 10)
C2 = Checkbutton(smallFrame, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 10)
C1.grid(row = 5, column = 1, sticky = W)
C2.grid(row = 6, column = 1, sticky = W)

addNewCategory = Label(smallFrame, text = "Add a New Category", font = "Helvetica 10 underline")
addNewCategory.grid(row = 7, column = 1, sticky= W, padx = 10, pady = 2)

numStudentsLabel = Label(smallFrame, text="Estimated # of Students:")
numStudentsLabel.grid(row=9, column=0, sticky=E, padx=5, pady=5)
numStudentsEntry = Entry(smallFrame, width=50)
numStudentsEntry.grid(row=9, column=1, sticky=W, pady=5)

backButton = Button(smallFrame, text="Back", width=10, bg="white")
backButton.grid(row=13, column=0, sticky = E, pady = 20)

submitButton = Button(smallFrame, text="Submit", width=10, bg="white")
submitButton.grid(row=13, column=1, sticky = E, pady = 20, padx = 100)

rootWin.mainloop()