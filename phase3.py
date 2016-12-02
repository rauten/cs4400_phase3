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

# READ: WHEN NAMING GUIS METHODS, USE CAPS AS SO: def ExampleGUI()
#       WHEN NAMING FUNCTIONS, PLEASE USE CAMEL CASE Ex: fooBar()



class masterGUI:



    def __init__(self, win):
        # Setup
        self.win = win

        self.rows = 3
        self.categoryList = []


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
        self.btRegister = Button(self.win, width = 10, text = "Register", padx=5, pady=5, command = self.RegisterPage)
        self.btRegister.grid(row = 3, column = 1, sticky=E)
        self.btLogin = Button(self.win, width = 5, padx=5, pady=5, text = "Login", command = self.LoginCheck)
        self.btLogin.grid(row = 3, column = 1, sticky=W)

    def showWin(self):
        self.win.deiconify()
        self.registerpage.withdraw()

    def registerOpen(self):
        self.win.withdraw()
        self.RegisterPage()

    def Connect(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu",passwd="Z8IHtiyg",user="cs4400_Team_9",db="cs4400_Team_9")
            self.cursor = self.db.cursor()
        except:
            raise
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


        regButton = Button(self.bigFrame, text="Create", width=10, bg="white", command = self.registerNew)
        regButton.grid(row=7, column=0)

    
    def registerNew(self): #Pass in username
        self.Connect()
        self.cursor = self.db.cursor()
        self.SQL_RegisterCheck = "SELECT Username FROM USER WHERE Username = %s"
        existUser = self.cursor.execute(self.SQL_RegisterCheck,(self.usernameEntry.get()))
        print(existUser)
        null2 = "0"
        if self.confirmPassword.get() != self.passwordReg.get() :
            messagebox.showwarning("Error", "Passwords do not match")
        elif self.usernameReg.get() == "":
            messagebox.showwarning("Error", "Please enter a username")
        elif self.passwordReg.get() == "" :
            messagebox.showwarning("Error", "Please enter a password")
        elif existUser > 0:
            messagebox.showwarning("Error", "Username already exists!")
        else:
            self.SQL_RegisterStudent = "INSERT INTO STUDENT (Username, GT_Email, Password) VALUES (%s, %s, %s)"
            self.cursor.execute(self.SQL_RegisterStudent, (self.usernameReg.get(), self.email.get(), self.passwordReg.get()))
            self.SQL_User = "INSERT INTO USER (Username,Password,isAdmin) VALUES(%s, %s, %s)"
            self.cursor.execute(self.SQL_User, (self.usernameReg.get(), self.passwordReg.get(), null2))
            self.db.commit()
            self.db.close()
            self.mainPageOpen() #Change this to login page


##    def loginCheck(self):
##        self.sql = "SELECT Username,GT_Email,Password FROM STUDENT"
##
##        self.cursor.execute(self.sql)
##        information = self.cursor.fetchall()
##        self.db.close()
##
##        self.uname = self.usernameReg.get()
##        self.passw = self.passwordReg.get()
##        self.passconf = self.cp.get()
##        self.emailconf = self.email.get()
##        null = "0"
##
##        if self.uname == "" or self.passw == "" or self.passconf == "" or self.emailconf == "":
##            messagebox.showwarning("Error!", "Cannot have empty field")
##        elif self.passconf != self.passw:
##            messagebox.showwarning("Error", "Passwords do not match! Try again.")
##        elif "@gatech.edu" not in self.emailconf:
##            messagebox.showwarning("Error!", "Please enter valid email")
##        else:
##            fruit = True
##            for each in information:
##                if self.emailconf in each:
##                    messagebox.showwarning("Error", "Email already in system! Please try again!")
##                elif self.uname in each:
##                    messagebox.showwarning("Error", "Username already in system. Please try again!")
##                    fruit = False
##                if fruit:
##                    self.Connect()
##                    self.sql2 = "INSERT INTO STUDENT(Username, GT_Email, Password, Year, Major_Name) VALUES(%s,%s,%s,%s,%s)"
##                    self.cursor.execute(self.sql2,(self.uname,self.emailconf,self.passw,null,null))
##                    self.db.commit()
##                    self.db.close()
##                    messagebox.showwarning("Successful Registration!", "Please log in!")
##                    self.showWin()
                    
            
    def LoginCheck(self):
        self.Connect()

        self.userLogin = self.usernameEntry.get()
        self.passLogin = self.passwordEntry.get()

        self.cursor = self.db.cursor()
        self.sql = "SELECT * FROM USER WHERE Username = %s AND Password = %s"
        info = self.cursor.execute(self.sql, (self.userLogin, self.passLogin))
        print(info)
            #info2 = self.cursor.fetchall()
        if info == 0:
            messagebox.showwarning("Error! Data entered not registered username/password combination.")
        else:
            messagebox.showwarning("Success! Login Successful!")
            self.mainPageOpen() #Open the main page

    def mainPageOpen(self):
        self.win.withdraw()
        self.MainPage()
        self.sql = "SELECT * FROM USER WHERE Username = %s AND Password = %s"

        try:
            self.cursor.execute(self.sql,(self.userLogin, self.passLogin))
            info2 = self.cursor.fetchall()
            if len(info2==0):
                messagebox.showwarning("Error! Data entered not registered username/password combination.")
            else:
                messagebox.showwarning("Success! Login Successful!")
                self.win.withdraw()
                #self.someFunction
        except:
            print("Error, try new login! Invalid username/password combo.")


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

        # ME PAGE
        self.applyFilterBtn = Button(self.smallFrame, width=10, text="Me", command=self.openMe)
        self.applyFilterBtn.grid(row=0, column=0, sticky=W)

        # CATEGORY SELECTION
        self.categoryFilter = ""
        self.choiceVarOne = StringVar()
        self.choiceVarOne.set("Please Select")
        self.category = OptionMenu(self.smallFrame, self.choiceVarOne, "Computing for good",
                                   "Doing good for your neighborhood", "Reciprocal teaching and learning",
                                   "Urban development", "Adaptive learning", command=self.updateCategory)
        self.category.config(width=25)  # Allow the user to see everything
        self.category.grid(row=1, column=3, sticky=W, padx=5)
        categoryLB = Label(self.smallFrame, text="Category")
        categoryLB.grid(row=1, column=2, sticky=W, padx=5)

        # DESIGNATION SELECTION
        self.designationFilter = ""
        self.choiceVar = StringVar()
        self.choiceVar.set("Please Select")
        self.designation = OptionMenu(self.smallFrame, self.choiceVar, "Sustainable Communities", "Community", command=self.updateDesignation)
        self.designation.grid(row=2, column=1, sticky=W)
        designationLB = Label(self.smallFrame, text="Designation")
        designationLB.grid(row=2, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.majorFilter = ""
        self.choiceVarTwo = StringVar()
        self.choiceVarTwo.set("Please Select")
        self.major = OptionMenu(self.smallFrame, self.choiceVarTwo, "Computer Science", "Mechanical Engineering",
                                "Chemical Engineering", command=self.updateMajor)  # Can add more major options here if necessary
        self.major.grid(row=3, column=1, sticky=W)
        majorLB = Label(self.smallFrame, text="Major")
        majorLB.grid(row=3, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.yearFilter = ""
        self.choiceVarThree = StringVar()
        self.choiceVarThree.set("Please Select")
        self.year = OptionMenu(self.smallFrame, self.choiceVarThree, "Freshman", "Sophomore", "Junior", "Senior", command = self.updateYear)
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
        self.mainPageColumns = ['Name', 'Type']
        self.table = ttk.Treeview(self.smallFrame, height=15, columns=self.mainPageColumns, show = 'headings')
        self.table.grid(row=6, column=0, sticky=W, columnspan=5)
        self.table.heading('#1', text="Name")
        self.table.heading('#2', text="Type")

        # BUTTONS
        self.applyFilterBtn = Button(self.smallFrame, width=10, text="Apply Filter", command = self.applyFilter)
        self.applyFilterBtn.grid(row=5, column=3, sticky=W)
        self.resetFilterBtn = Button(self.smallFrame, width=10, text="Reset Filter", command=self.clearFilter)
        self.resetFilterBtn.grid(row=5, column=3, sticky=E)

    def updateYear(self, value):
        self.yearFilter = value

    def updateCategory(self, value):
        self.categoryFilter = value

    def updateMajor(self, value):
        self.majorFilter = value

    def updateDesignation(self, value):
        self.designationFilter = value

    def applyFilter(self):
        self.Connect()
        self.cursor = self.db.cursor()

        majorList = []
        yearList = []

        requirementsList = ['Freshman only', 'Sophomore only', 'Junior only', 'Senior only', 'CS student only', 'ECE student only', 'ChE student only']

        if self.majorFilter != "" :
            majorList.append(self.majorFilter + " students only")
        else:
            majorList = requirementsList

        if self.yearFilter != "" :
            yearList.append(self.yearFilter + " only")
        else:
            yearList = requirementsList

        self.SQL_ApplyFilterProject = "SELECT DISTINCT(P.Project_Name) FROM PROJECT AS P LEFT OUTER JOIN PROJECT_CATEGORY AS PC ON P.Project_Name = PC.Project_Name" \
                               " LEFT OUTER JOIN PROJECT_REQUIREMENTS AS PR ON P.Project_Name = PR.Project_Name" \
                               " WHERE P.Project_Name = CASE WHEN (%s != '') THEN %s ELSE P.Project_Name END" \
                               " AND EXISTS( SELECT * " \
                                           " FROM PROJECT_REQUIREMENTS AS PRE" \
                                           " WHERE PRE.Project_Name = P.Project_Name AND ((PRE.Requirements IN %s) OR (PRE.Requirements IS NULL AND %s = '')))" \
                               " AND EXISTS( SELECT *" \
                                           " FROM PROJECT_REQUIREMENTS AS PRE" \
                                           " WHERE PRE.Project_Name = P.Project_Name AND ((PRE.Requirements IN %s) OR (PRE.Requirements IS NULL AND %s = '')))" \
                               " AND P.Designation_Name = CASE WHEN (%s != '') THEN %s ELSE P.Designation_Name END" \
                               " AND PC.Category_Name = CASE WHEN (%s != '') THEN %s ELSE PC.Category_Name END "


        self.SQL_ApplyFilterCourse = "SELECT DISTINCT(C.Course_Name) FROM COURSE AS C LEFT OUTER JOIN COURSE_CATEGORY AS CC ON C.Course_Name = CC.Course_Name" \
                               " LEFT OUTER JOIN COURSE_REQUIREMENTS AS CR ON C.Course_Name = CR.Course_Name" \
                               " WHERE C.Course_Name = CASE WHEN (%s != '') THEN %s ELSE C.Course_Name END" \
                               " AND EXISTS( SELECT * " \
                                           " FROM COURSE_REQUIREMENTS AS COR" \
                                           " WHERE COR.Course_Name = C.Course_Name AND ((COR.Requirements IN %s) OR (COR.Requirements IS NULL AND %s = '')))" \
                               " AND EXISTS( SELECT *" \
                                           " FROM COURSE_REQUIREMENTS AS COR" \
                                           " WHERE COR.Course_Name = C.Course_Name AND ((COR.Requirements IN %s) OR (COR.Requirements IS NULL AND %s = '')))" \
                               " AND C.Designation_Name = CASE WHEN (%s != '') THEN %s ELSE C.Designation_Name END" \
                               " AND CC.Category_Name = CASE WHEN (%s != '') THEN %s ELSE CC.Category_Name END "




        if self.projCourseSelection.get() == 0 :
            self.cursor.execute(self.SQL_ApplyFilterProject, (self.title.get(), self.title.get(), majorList, self.majorFilter, yearList, self.yearFilter, self.designationFilter, self.designationFilter, self.categoryFilter, self.categoryFilter))
        elif self.projCourseSelection.get() == 1:
            self.cursor.execute(self.SQL_ApplyFilterCourse, (self.title.get(), self.title.get(), majorList, self.majorFilter, yearList, self.yearFilter, self.designationFilter, self.designationFilter, self.categoryFilter, self.categoryFilter))

        results = self.cursor.fetchall()
        print(results)
        print(results[0][0])

        self.newList = []
        self.currList = []

        if self.projCourseSelection.get() == 0:
            for row in results:
                self.currList = list(row)
                self.currList.append("Project")
                self.newList.append(tuple(self.currList))


        for row in self.newList :
            self.table.insert('', 'end', value = row)




    def clearFilter(self):
        self.choiceVar.set("Please Select")
        self.choiceVarOne.set("Please Select")
        self.choiceVarTwo.set("Please Select")
        self.choiceVarThree.set("Please Select")
        self.title.delete(0, 'end')


    def openMe(self):
        self.mainPage.withdraw()
        self.MePage()

    def MePage(self):

        self.mePage = Toplevel()

        self.bigFrame = Frame(self.mePage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)


        self.titleLb = Label(self.win, text="Me")
        self.titleLb.grid(row=1, column=2, columnspan=2, padx=150, sticky=N)

        self.editProfileBtn = Button(self.smallFrame, width=1, text="Edit Profile", padx=80,
                                     pady=20, command = self.showEditProfilePage)
        self.editProfileBtn.grid(row=2, column=2, sticky=E)
        self.myAppBtn = Button(self.smallFrame, width=1, text="My Application", padx=80,
                               pady=50, command = self.showApplicationPage)
        self.myAppBtn.grid(row=3, column=2, sticky=E)
        self.backBtn = Button(self.smallFrame, width=1, text="Back", padx=80)  # Need a command here as well
        self.backBtn.grid(row=4, column=2, stick=E)


    def showEditProfilePage(self):
        self.mePage.withdraw()
        self.EditProfilePage()



    def EditProfilePage(self):
        self.editProfilePage = Toplevel()

        self.bigFrame = Frame(self.editProfilePage)
        self.bigFrame.grid(row = 1, column = 0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row = 0, column = 0)

        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_GetMajoriEditProf = " SELECT Major_Name, Year" \
                                     " FROM STUDENT " \
                                     " WHERE Username = %s"
        self.cursor.execute(self.SQL_GetMajoriEditProf, (self.usernameEntry.get()))
        results = self.cursor.fetchall()
        defaultMajor = results[0][0]
        defaultYear = results[0][1]

        self.titleLbEditProf = Label(self.smallFrame, text="Edit Profile")
        self.titleLbEditProf.grid(row=0, column=2)

        self.majorEditProfLb = Label(self.smallFrame, text = "Major")
        self.majorEditProfLb.grid(row = 1, column = 0)

        self.defaultMajorEditProf = defaultMajor
        self.defaultMajorEditProfStringVar = StringVar()
        self.defaultMajorEditProfStringVar.set(self.defaultMajorEditProf)
        self.majorEditProf = OptionMenu(self.smallFrame, self.defaultMajorEditProfStringVar, "Computer Science",
                                        "Electrical Engineering", "Chemical Engineering", command=self.updateMajor)
        self.majorEditProf.config(width = 20)
        self.majorEditProf.grid(row=1, column=2)


        self.yearEditProfLb = Label(self.smallFrame, text = "Year")
        self.yearEditProfLb.grid(row = 2, column = 0)

        self.defaultYearEditProf = defaultYear
        self.defaultYearEditProfStringVar = StringVar()
        self.defaultYearEditProfStringVar.set(self.defaultYearEditProf)
        self.yearEditProf = OptionMenu(self.smallFrame, self.defaultYearEditProfStringVar, "Freshman",
                                       "Sopohomore", "Junior", "Senior", command=self.updateYear)
        self.yearEditProf.config(width = 20)
        self.yearEditProf.grid(row=2, column=2)

        self.departmentEditProfLb = Label(self.smallFrame, text = "Department")


        self.backEditProfBtn = Button(self.smallFrame, text = "Back", command = self.editProfile)
        self.backEditProfBtn.grid(row = 3, column = 2)



    def editProfile(self):
        self.Connect()
        self.cursor = self.db.cursor()

        # Update major and year
        self.SQL_EditProfile = " UPDATE STUDENT" \
                               " SET Major_Name = %s, Year = %s" \
                               " WHERE Username = %s"

        # Filters are empty strings if they do not get 'updated' by the user.
        # That is, if the user doesn't edit their major, or year, their major/year will be set to ''
        if self.majorFilter == '':
            self.majorFilter = self.defaultMajorEditProf #Sets the filter to the default (inital) value if nothing is changed
        if self.yearFilter == '':
            self.yearFilter = self.defaultYearEditProf

        # Execute the SQL query
        self.cursor.execute(self.SQL_EditProfile, (self.majorFilter, self.yearFilter, self.usernameEntry.get()))


    def showApplicationPage(self):
        self.mePage.withdraw()
        self.ApplicationPage()

    def ApplicationPage(self):
        self.applicationPage = Toplevel()

        self.bigFrame = Frame(self.applicationPage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_PopulateApps = " SELECT Date, Project_Name, Status" \
                                " FROM APPLY" \
                                " WHERE Username = %s" \
                                " ORDER BY Date, Project_Name, Status"

        self.cursor.execute(self.SQL_PopulateApps, (self.usernameEntry.get()))

        results = self.cursor.fetchall()

        self.myApplicationLb = Label(self.smallFrame, text = "My Application")
        self.myApplicationLb.grid(row = 0, column = 2)

        self.dataColumns = ['Date', 'Project Name', 'Status']
        self.myAppsTreeView = ttk.Treeview(self.smallFrame, columns=self.dataColumns, show = 'headings')
        self.myAppsTreeView.grid(row=6, column=0, sticky=W, columnspan=5)
        self.myAppsTreeView.heading('#1', text="Date")
        self.myAppsTreeView.heading('#2', text="Project Name")
        self.myAppsTreeView.heading('#3', text="Status")

        self.backBtnAppPage = Button(self.smallFrame, text = "Back", command = self.backToMePage)
        self.backBtnAppPage.grid(row = 10, column = 2)

        for row in results:
            self.myAppsTreeView.insert('', 'end', value = row)


    def backToMePage(self):
        self.applicationPage.withdraw()
        self.MePage()

        self.usernameReg = Entry(self.smallFrame, width=50)

    def ViewApplication(self):
        self.viewApplication = Toplevel()
        self.bigFrame = Frame(self.viewApplication)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.viewApplication)
        self.smallFrame.grid(row=0, column=0)

        self.l1 = Label(self.smallFrame, text="Application", width=30, padx=5, pady=5, fg="blue", font=("Helvetica", 16))
        self.l1.grid(row=0, column=1)




win = Tk()
a = masterGUI(win)
win.mainloop()
