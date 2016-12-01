from tkinter import *

from tkinter import messagebox
from tkinter import ttk


import re
import string
import pymysql
import sys
import tkinter.messagebox
import urllib.request
import time
import datetime
import random


class masterGUI:



    def __init__(self, win):
        # Setup
        self.win = win
        self.MainPage()

        # Titles
        self.label1 = Label(self.win, text = "Login")
        self.label1.grid(row = 0, column = 0, columnspan = 2)

        # Initialize labels
        self.usernameLabel = Label(self.win, text = "Username")
        self.passwordLabel = Label(self.win, text = "Password")
        self.usernameLabel.grid(row = 1, column = 0)
        self.passwordLabel.grid(row = 2, column = 0)

        # Initialize entries
        self.usernameEntry = Entry(self.win, width = 20)
        self.usernameEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.passwordEntry = Entry(self.win, width = 20)
        self.passwordEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

        # Initialize buttons
        self.btRegister = Button(self.win, width = 10, text = "Register", padx=5, pady=5, command = self.registerOpen)
        self.btRegister.grid(row = 3, column = 1, sticky=E)
        self.btLogin = Button(self.win, width = 5, padx=5, pady=5, text = "Login", command = self.loginCheck)
        self.btLogin.grid(row = 3, column = 1, sticky=W)


    def registerOpen(self):
        self.win.withdraw()
        self.RegisterPage()


    def Connect(self):
        try:
            self.db = pymysql.connect(host="acacdemic-mysql.cc.gatech.edu",passwd="Z8IHtiyg",user="cs4400_Team_9",db="cs4400_Team_9")
        except:
            messagebox.showinfo("Connection error. Check your Internet Connection and/or code!")


    def RegisterPage(self):
        self.registerPage = Toplevel()

        self.bigFrame = Frame(self.registerPage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        self.titleReg = Label(self.smallFrame,text="New Student Registration", width=30, padx=5, pady=5, fg="blue", font=("Helvetica", 16))
        self.titleReg.grid(row=0, column=1)
        self.usernameReg = Entry(self.smallFrame, width=50)
        self.usernameReg.grid(row=1, column=1, sticky=E, pady=5)
        f1 = Label(self.smallFrame, text="Username:")
        f1.grid(row=1, column=0, sticky=E, padx=5, pady=5)
        f2 = Label(self.smallFrame, text="GT Email Address:")
        f2.grid(row=2, column=0, sticky=E, padx=5, pady=5)
        self.email = Entry(self.smallFrame, width=50)
        self.email.grid(row=2, column=1, sticky=E, pady=5)
        f3 = Label(self.smallFrame, text="Password:")
        f3.grid(row=3, column=0, sticky=E, padx=5, pady=5)
        self.passwordReg = Entry(self.smallFrame, width=50)
        self.passwordReg.grid(row=3, column=1, sticky=E, pady=5)
        f4 = Label(self.smallFrame, text="Confirm Password:")
        f4.grid(row=4, column=0, sticky=E, padx=5, pady=5)
        self.confirmPassword = Entry(self.smallFrame, width=50)
        self.confirmPassword.grid(row=4, column=1, sticky=E, pady=5)

        regButton = Button(self.bigFrame, text="Create", width=10, bg="white", command = self.registerNew(self.usernameReg))
        regButton.grid(row=7, column=0)

    
    def registerNew(self, username): #Pass in username
        self.db = self.Connect()
        self.cursor = self.db.cursor()
        self.SQL_RegisterCheck = "SELECT Username FROM USER WHERE Username = %s", (username)
        existUser = self.cursor.execute(self.SQL_RegisterCheck)

        if self.confirmPassword.get() != self.passwordReg.get() :
            messagebox.showwarning("Error", "Passwords do not match")
        elif username == "":
            messagebox.showwarning("Error", "Please enter a username")
        elif self.passwordReg.get() == "" :
            messagebox.showwarning("Error", "Please enter a password")
        elif existUser > 0:
            messagebox.showwarning("Error", "Username already exists!")
        else:
            self.SQL_RegisterUser = "INSERT INTO STUDENT (Username, GT_Email, Password) VALUES (%s, %s, %s)", (self.passwordReg.get(), self.email.get(), self.passwordReg.get())
            self.cursor.execute(self.SQL_RegisterUser)
            self.mainPageOpen()


    def loginCheck(self):
        self.db2 = self.Connect()

        self.userLogin = self.usernameEntry.get()
        self.passLogin = self.passwordEntry.get()

        try:
            self.cursor = self.db2.cursor()
            self.sql = "SELECT * FROM USER WHERE Username = %s AND Password = %s"
            info = self.cursor.execute(self.sql, (self.userLogin, self.passLogin))
            info2 = self.cursor.fetchall()
            if len(info2 == 0):
                messagebox.showwarning("Error! Data entered not registered username/password combination.")
            else:
                messagebox.showwarning("Success! Login Successful!")
                self.mainPageOpen() #Open the main page
        except:
            print("Error, try new login! Invalid username/password combo.")

    def mainPageOpen(self):
        self.win.withdraw()
        self.MainPage()


    def MainPage(self):
        self.mainPage = Toplevel()

        self.bigFrame = Frame(self.mainPage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        # Title
        self.titleReg = Label(self.smallFrame, text="Main Page", width=30, padx=5, pady=5, fg="blue",
                              font=("Helvetica", 16))
        self.titleReg.grid(row=0, column=1)
        self.title = Entry(self.smallFrame, width=30)
        self.title.grid(row=1, column=1, sticky=W)
        titleLB = Label(self.smallFrame, text="Title")
        titleLB.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # CATEGORY SELECTION
        self.choiceVarOne = StringVar()
        self.choiceVarOne.set("Please Select")
        self.category = OptionMenu(self.smallFrame, self.choiceVarOne, "Computing for good",
                                   "Doing good for your neighborhood", "Reciprocal teaching and learning",
                                   "Urban development", "Adaptive learning")
        self.category.config(width=25)  # Allow the user to see everything
        self.category.grid(row=1, column=3, sticky=W, padx=5)
        categoryLB = Label(self.smallFrame, text="Category")
        categoryLB.grid(row=1, column=2, sticky=W, padx=5)

        # DESIGNATION SELECTION
        self.choiceVar = StringVar()
        self.choiceVar.set("Please Select")
        self.designation = OptionMenu(self.smallFrame, self.choiceVar, "Sustainable Communities", "Community")
        self.designation.grid(row=2, column=1, sticky=W)
        designationLB = Label(self.smallFrame, text="Designation")
        designationLB.grid(row=2, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.choiceVarTwo = StringVar()
        self.choiceVarTwo.set("Please Select")
        self.major = OptionMenu(self.smallFrame, self.choiceVarTwo, "Computer Science", "Mechanical Engineering",
                                "Chemical Engineering")  # Can add more major options here if necessary
        self.major.grid(row=3, column=1, sticky=W)
        majorLB = Label(self.smallFrame, text="Major")
        majorLB.grid(row=3, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.choiceVarThree = StringVar()
        self.choiceVarThree.set("Please Select")
        self.year = OptionMenu(self.smallFrame, self.choiceVarThree, "Freshman", "Sophomore", "Junior", "Senior")
        self.year.grid(row=4, column=1, sticky=W)
        yearLB = Label(self.smallFrame, text="Year")
        yearLB.grid(row=4, column=0, sticky=W, padx=5, pady=30)

        # PROJECT/COURSE SELECTION
        self.projCourseSelection = IntVar()

        self.proj = Radiobutton(self.smallFrame, text="Project", variable=self.projCourseSelection, value=0)
        self.proj.grid(row=3, column=4)
        self.course = Radiobutton(self.smallFrame, text="Course", variable=self.projCourseSelection, value=1)
        self.course.grid(row=3, column=5)
        self.both = Radiobutton(self.smallFrame, text="Both", variable=self.projCourseSelection, value=2)
        self.both.grid(row=3, column=6)

        # Treeview table
        self.table = ttk.Treeview(self.smallFrame, height=15, columns=("Name"), selectmode="extended")
        self.table.grid(row=6, column=0, sticky=W, columnspan=5)
        self.table.heading('#0', text="Name")
        self.table.heading('#1', text="Type")
        self.table.column('#0', stretch=tkinter.YES)
        self.table.column('#1', stretch=tkinter.YES)

        # BUTTONS
        self.applyFilterBtn = Button(self.smallFrame, width=10, text="Apply Filter", command = self.applyFilter)
        self.applyFilterBtn.grid(row=5, column=3, sticky=W)
        self.resetFilterBtn = Button(self.smallFrame, width=10, text="Reset Filter", command=self.clearFilter)
        self.resetFilterBtn.grid(row=5, column=3, sticky=E)


    def applyFilter(self):
        self.db = self.Connect()
        self.cursor = self.db.cursor()

        majorList = []
        yearList = []

        if self.major.get() != "" :
            majorList.append(self.major.get() + " students only")
        else:
            majorList = ["Computer Science students only", "Electrical Engineering students only", "Chemical Engineering students only"]

        if self.year.get() != "" :
            yearList.append(self.year.get() + " only")
        else:
            yearList = ["Freshman only", "Sophomore only", "Junior only", "Senior only"]


        self.SQL_ApplyFilterProject = "SELECT DISTINCT(Project_Name) FROM PROJECT AS P LEFT OUTER JOIN PROJECT_CATEGORY AS PC LEFT OUTER JOIN PROJECT_REQUIREMENTS AS PR" \
                               " ON P.Project_Name = PC.Project_Name AND P.Project_Name = PR.Project_Name" \
                               " WHERE P.Project_Name = CASE WHEN (%s != "") THEN %s ELSE P.Project_Name" \
                               " AND P.Requirement_Name IN (' + ','.join(map(str, majorList)) + ')" \
                               " AND P.Requirement_Name IN (' + ','.join(map(str, yearList)) + ')" \
                               " AND P.Designation_Name = CASE WHEN (%s != "") THEN %s ELSE P.Designation_Name" \
                               " AND P.Category_Name = CASE WHEN (%s != "") THEN %s ELSE P.Category_Name"

        self.SQL_ApplyFilterCourse = "SELECT DISTINCT(Course_Name) FROM COURSE AS C LEFT OUTER JOIN COURSE_CATEGORY AS CC LEFT OUTER JOIN COURSE_REQUIREMENTS AS CR" \
                               " ON C.Course_Name = CC.Course_Name AND C.Course_Name = CR.Course_Name" \
                               " WHERE C.Course_Name = CASE WHEN (%s != "") THEN %s ELSE C.Course_Name" \
                               " AND C.Requirement_Name IN (' + ','.join(map(str, majorList)) + ')" \
                               " AND C.Requirement_Name IN (' + ','.join(map(str, yearList)) + ')" \
                               " AND C.Designation_Name = CASE WHEN (%s != "") THEN %s ELSE C.Designation_Name" \
                               " AND C.Category_Name = CASE WHEN (%s != "") THEN %s ELSE C.Category_Name"


        if self.projCourseSelection.get() == 0 :
            self.cursor.execute(self.SQL_ApplyFilterProject, (self.title.get(), self.title.get(), self.category.get(), self.category.get()))
        elif self.projCourseSelection.get() == 1:
            self.cursor.execute(self.SQL_ApplyFilterCourse, (self.title.get(), self.title.get(), self.category.get(), self.category.get()))

        results = self.cursor.fetchall()

        for row in results:
            self.table.insert('Name', 'end', row[0])
            if self.projCourseSelection.get() == 0 :
                self.table.insert('Type', 'end', "Project")
            else :
                self.table.insert('Type', 'end', "Course")



    def clearFilter(self):
        self.choiceVar.set("Please Select")
        self.choiceVarOne.set("Please Select")
        self.choiceVarTwo.set("Please Select")
        self.choiceVarThree.set("Please Select")
        self.title.delete(0, 'end')


    def openMe(self):
        self.win.withdraw()
        self.MePage()

    def MePage(self):

        self.mePage = Toplevel()

        self.bigFrame = Frame(self.mePage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)


        self.titleLb = Label(self.win, text="Me")
        self.titleLb.grid(row=0, column=2, columnspan=2, padx=150, sticky=N)
        self.editProfileBtn = Button(self.smallFrame, width=1, text="Edit Profile", padx=80,
                                     pady=20)  # Must insert a command here
        self.editProfileBtn.grid(row=1, column=2, sticky=E)
        self.myAppBtn = Button(self.smallFrame, width=1, text="My Application", padx=80,
                               pady=50)  # Also need a command functionality here
        self.myAppBtn.grid(row=2, column=2, sticky=E)
        self.backBtn = Button(self.smallFrame, width=1, text="Back", padx=80)  # Need a command here as well
        self.backBtn.grid(row=3, column=2, stick=E)





win = Tk()
a = masterGUI(win)
win.mainloop()
