from tkinter import *

rootWin = Tk()
rootWin.title("CS 4400 Add a Project")

smallFrame = Frame(rootWin)
smallFrame.grid(row=0, column=0)
titleReg = Label(smallFrame,text="Add a Project", padx= 45, pady=10, font=16)
titleReg.grid(row=0, column= 1, sticky = W)

projectNameEntry = Entry(smallFrame, width=50)
projectNameEntry.grid(row=1, column=1, sticky=W, pady=5)
projectNameLabel = Label(smallFrame, text="Project Name:")
projectNameLabel.grid(row=1, column=0, sticky=E, padx=5, pady=5)

advisorLabel = Label(smallFrame, text="Advisor:")
advisorLabel.grid(row=2, column=0, sticky=E, padx=5, pady=5)
advisorEntry = Entry(smallFrame, width=50)
advisorEntry.grid(row=2, column=1, sticky=W, pady=5)

advisorEmailLabel = Label(smallFrame, text="Advisor Email:")
advisorEmailLabel.grid(row=3, column=0, sticky=E, padx=5, pady=5)
advisorEmailEntry = Entry(smallFrame, width=50)
advisorEmailEntry.grid(row=3, column=1, sticky=W, pady=5)

descriptionLabel = Label(smallFrame, text = "Description:")
descriptionLabel.grid(row = 4, column = 0, sticky = N, padx = 5, pady = 5)
descriptionEntry = Text(smallFrame, wrap = WORD, height = 5, width = 35)
scrollbar = Scrollbar(smallFrame)
scrollbar.grid(row = 4, column = 1, sticky = N + S + E)
descriptionEntry.grid(row = 4, column = 1, sticky = W)
descriptionEntry.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=descriptionEntry.yview)

Label(smallFrame, text = "Category: ").grid(row = 5, column = 0, sticky=E, padx = 5, pady = 5)
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(smallFrame, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=1, width = 10)
C2 = Checkbutton(smallFrame, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=1, width = 10)
C1.grid(row = 5, column = 1, sticky = W)
C2.grid(row = 6, column = 1, sticky = W)

addNewCategory = Label(smallFrame, text = "Add a New Category", font = "Helvetica 10 underline")
addNewCategory.grid(row = 7, column = 1, sticky= W, padx = 10, pady = 2)

Label(smallFrame, text = "Designation:").grid(row = 8, column = 0, sticky=E, padx = 5, pady = 5)
designationChoices = StringVar(smallFrame)
designation = {'Pizza','Lasagne','Fries','Fish','Potatoe'}
designationChoices.set('None')
popupMenu3 = OptionMenu(smallFrame, designationChoices, *designation)
popupMenu3.grid(row = 8, column =1, sticky = W)

numStudentsLabel = Label(smallFrame, text="Estimated # of Students:")
numStudentsLabel.grid(row=9, column=0, sticky=E, padx=5, pady=5)
numStudentsEntry = Entry(smallFrame, width=50)
numStudentsEntry.grid(row=9, column=1, sticky=W, pady=5)

Label(smallFrame, text = "Major Requirement:").grid(row = 10, column = 0, sticky=E, padx = 5, pady = 5)
majorReqChoices = StringVar(smallFrame)
majorReq = {'Pizza','Lasagne','Fries','Fish','Potatoe'}
majorReqChoices.set('None')
popupMenu4 = OptionMenu(smallFrame, majorReqChoices, *majorReq)
popupMenu4.grid(row = 10, column =1, sticky = W)

Label(smallFrame, text = "Year Requirement:").grid(row = 11, column = 0, sticky=E, padx = 5, pady = 5)
yearReqChoices = StringVar(smallFrame)
yearReq = {'Pizza','Lasagne','Fries','Fish','Potatoe'}
yearReqChoices.set('None')
popupMenu5 = OptionMenu(smallFrame, yearReqChoices, *yearReq)
popupMenu5.grid(row = 11, column =1, sticky = W)

Label(smallFrame, text = "Department Requirement:").grid(row = 12, column = 0, sticky=E, padx = 5, pady = 5)
departmentReqChoices = StringVar(smallFrame)
departmentReq = {'Pizza','Lasagne','Fries','Fish','Potatoe'}
departmentReqChoices.set('None')
popupMenu6 = OptionMenu(smallFrame, departmentReqChoices, *departmentReq)
popupMenu6.grid(row = 12, column =1, sticky = W)

backButton = Button(smallFrame, text="Back", width=10, bg="white")
backButton.grid(row=13, column=0, sticky = E, pady = 20)

submitButton = Button(smallFrame, text="Submit", width=10, bg="white")
submitButton.grid(row=13, column=1, sticky = E, pady = 20, padx = 100)

rootWin.mainloop()