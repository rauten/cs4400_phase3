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
        self.label1 = Label(self.win, text="Login")
        self.label1.grid(row=0, column=0, columnspan=2)

        # Initialize labels
        self.usernameLabel = Label(self.win, text="Username")
        self.passwordLabel = Label(self.win, text="Password")
        self.usernameLabel.grid(row=1, column=0)
        self.passwordLabel.grid(row=2, column=0)

        # Initialize entries
        self.usernameEntry = Entry(self.win, width=20)
        self.usernameEntry.grid(row=1, column=1, padx=5, pady=5)
        self.passwordEntry = Entry(self.win, width=20)
        self.passwordEntry.grid(row=2, column=1, padx=5, pady=5)

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
            messagebox.showinfo("Connection error. Check your Internet Connection and/or code!")

    def RegisterPage(self):
        self.registerPage = Toplevel()

        self.bigFrame = Frame(self.registerPage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        self.titleReg = Label(self.smallFrame, text="New Student Registration", width=30, padx=5, pady=5, fg="blue",
                              font=("Helvetica", 16))
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

    def registerNew(self):  # Pass in username
        self.Connect()
        self.cursor = self.db.cursor()
        self.SQL_RegisterCheck = "SELECT Username FROM USER WHERE Username = %s"
        existUser = self.cursor.execute(self.SQL_RegisterCheck,(self.usernameEntry.get()))
        null2 = "0"
        if self.confirmPassword.get() != self.passwordReg.get() :
            messagebox.showwarning("Error", "Passwords do not match")
        elif self.usernameReg.get() == "":
            messagebox.showwarning("Error", "Please enter a username")
        elif self.passwordReg.get() == "":
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
            #info2 = self.cursor.fetchall()
        self.yes=str(1)
        self.adcheck = "SELECT * FROM USER WHERE Username = %s AND Password = %s AND isAdmin= %s"
        admin=self.cursor.execute(self.adcheck, (self.userLogin, self.passLogin,str(1)))

        if info == 0:
            messagebox.showwarning("Error! Data entered not registered username/password combination.")
        elif admin==0:
            messagebox.showwarning("Success! Login Successful!")
            self.mainPageOpen() #Open the main page
        elif admin==1:
            messagebox.showwarning("Success! Login Successful!")
            self.AdminViewFunct()#open functionality page


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

        self.Connect()
        self.cursor = self.db.cursor()


        self.SQL_GetMajors = " SELECT DISTINCT(Major_Name)" \
                             " FROM MAJOR" \

        self.cursor.execute(self.SQL_GetMajors)
        self.majors = self.cursor.fetchall()
        self.majorsList = []
        for item in self.majors:
            self.majorsList.append(item[0])

        self.SQL_GetDesignations = " SELECT Designation_Name" \
                                   " FROM DESIGNATION"

        self.cursor.execute(self.SQL_GetDesignations)
        self.designations = self.cursor.fetchall()
        self.designationsList = []
        for item in self.designations:
            self.designationsList.append(item[0])


        self.SQL_GetCategories = " SELECT Category_Name" \
                                   " FROM CATEGORY"

        self.cursor.execute(self.SQL_GetCategories)
        self.categories = self.cursor.fetchall()
        self.categoriesList = []
        for item in self.categories:
            self.categoriesList.append(item[0])


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
        self.categoriesLBLb = Label(self.smallFrame, text = "Category: ").grid(row = 1, column = 3)
        self.categoriesListBox = Listbox(self.smallFrame, width = 47, height = 7)
        self.categoriesListBox.grid(row = 1, column = 4)
        #self.category.config(width=25)  # Allow the user to see everything
        #self.category.grid(row=1, column=3, sticky=W, padx=5)
        #categoryLB = Label(self.smallFrame, text="Category")
        #categoryLB.grid(row=1, column=2, sticky=W, padx=5)

        # DESIGNATION SELECTION
        self.designationFilter = ""
        self.choiceVar = StringVar()
        self.choiceVar.set("Please Select")
        self.designation = OptionMenu(self.smallFrame, self.choiceVar, *self.designationsList,
                                      command=self.updateDesignation)
        self.designation.grid(row=2, column=1, sticky=W)
        designationLB = Label(self.smallFrame, text="Designation")
        designationLB.grid(row=2, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.majorFilter = ""
        self.choiceVarTwo = StringVar()
        self.choiceVarTwo.set("Please Select")
        self.major = OptionMenu(self.smallFrame, self.choiceVarTwo, *self.majorsList, command=self.updateMajor)  # Can add more major options here if necessary
        self.major.grid(row=3, column=1, sticky=W)
        majorLB = Label(self.smallFrame, text="Major")
        majorLB.grid(row=3, column=0, sticky=W, padx=5)

        # MAJOR SELECTION
        self.yearFilter = ""
        self.choiceVarThree = StringVar()
        self.choiceVarThree.set("Please Select")
        self.year = OptionMenu(self.smallFrame, self.choiceVarThree, "Freshman", "Sophomore", "Junior", "Senior",
                               command=self.updateYear)
        self.year.grid(row=4, column=1, sticky=W)
        yearLB = Label(self.smallFrame, text="Year")
        yearLB.grid(row=4, column=0, sticky=W, padx=5, pady=30)

        # PROJECT/COURSE SELECTION
        self.projCourseSelection = IntVar()

        self.proj = Radiobutton(self.smallFrame, text="Project", variable=self.projCourseSelection, value=0)
        self.proj.grid(row=3, column=5)
        self.course = Radiobutton(self.smallFrame, text="Course", variable=self.projCourseSelection, value=1)
        self.course.grid(row=3, column=6)
        self.both = Radiobutton(self.smallFrame, text="Both", variable=self.projCourseSelection, value=2)
        self.both.grid(row=3, column=7)

        # Treeview table
        self.mainPageColumns = ['Name', 'Type']
        self.table = ttk.Treeview(self.smallFrame, height=15, columns=self.mainPageColumns, show='headings')
        self.table.grid(row=6, column=0, sticky=W, columnspan=5)
        self.table.heading('#1', text="Name")
        self.table.heading('#2', text="Type")
        self.table.column('#1,', minwidth=0, width=400)

        # BUTTONS
        self.applyFilterBtn = Button(self.smallFrame, width=10, text="Apply Filter", command=self.applyFilter)
        self.applyFilterBtn.grid(row=5, column=4, sticky=W)
        self.resetFilterBtn = Button(self.smallFrame, width=10, text="Reset Filter", command=self.clearFilter)
        self.resetFilterBtn.grid(row=5, column=4, sticky=E)
        self.addCategoryBtn = Button(self.smallFrame, width=10, text="Add Category", command=self.AddCategoryWindow)
        self.addCategoryBtn.grid(row=1, column = 5)


    def AddCategoryWindow(self):
        self.Connect()
        self.cursor = self.db.cursor()

        self.addCategoryWindow = Toplevel()

        self.smallFrame = Frame(self.addCategoryWindow)
        self.smallFrame.grid(row=1, column=0)

        self.catNameLb = Label(self.smallFrame, text = "Select a Category Name:")
        self.catNameLb.grid(row = 2, column = 0, sticky = E, padx = 5, pady = 5)
        self.catChoices = StringVar(self.smallFrame)

        self.cursor.execute(self.SQL_GetCategories)
        categories = self.cursor.fetchall()
        categoriesList = []
        addedcategories =[]
        donecats = self.categoriesListBox.get(0, END)

        for i in donecats:
            addedcategories.append(i)

        for i in categories:
            if i[0] not in addedcategories:
                categoriesList.append(i[0])

        self.catChoices.set("Select Option")
        popupMenu7 = OptionMenu(self.smallFrame, self.catChoices, *categoriesList)
        popupMenu7.grid(row = 2, column = 1, sticky = W)
        self.submitCategoryBtn = Button(self.smallFrame, text = "Ok", width = 10, command = self.addCategoryToListView)
        self.submitCategoryBtn.grid(row = 3, column = 1, sticky = E, pady = 5, padx = 100)

    def addCategoryToListView(self):
        self.categorySelected = self.catChoices.get()
        if self.categorySelected != "Select Option":
            self.categoriesListBox.insert(END, self.categorySelected)
        self.addCategoryWindow.withdraw()



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

        if self.table.get_children() != ():
            for row in self.table.get_children():
                self.table.delete(row)

        self.categoriesInListBox = []
        self.categoriesInListBox = self.categoriesListBox.get(0, END)

        self.SQL_CheckCategoryProject = " SELECT DISTINCT(Project_Name)" \
                                        " FROM PROJECT_CATEGORY" \
                                        " WHERE Category_Name = %s"

        self.SQL_CheckCategoryCourse = " SELECT DISTINCT(Course_Name)" \
                                       " FROM COURSE_CATEGORY" \
                                       " WHERE Category_Name = %s"

        self.SQL_GetProjects = " SELECT DISTINCT(Project_Name)" \
                               " FROM PROJECT"

        self.SQL_GetCourses = " SELECT DISTINCT(Course_Name)" \
                              " FROM COURSE"

        currentList = []
        self.cursor.execute(self.SQL_GetProjects)
        self.currTupleList = self.cursor.fetchall()
        for i in self.currTupleList:
            currentList.append(i[0])
        newListProjects = []
        for i in self.categoriesInListBox:
            self.cursor.execute(self.SQL_CheckCategoryProject, (i))
            self.currTupleList = self.cursor.fetchall()
            for row in self.currTupleList:
                newListProjects.append(row[0])
            currentList = set(currentList).intersection(newListProjects)
            currentList = list(currentList)
            newListProjects.clear()

        currentListCourse = []
        self.cursor.execute(self.SQL_GetCourses)
        self.currTupleList = self.cursor.fetchall()
        for i in self.currTupleList:
            currentListCourse.append(i[0])
        newListCourses = []
        for i in self.categoriesInListBox:
            self.cursor.execute(self.SQL_CheckCategoryCourse, (i))
            self.currTupleList = self.cursor.fetchall()
            for row in self.currTupleList:
                newListCourses.append(row[0])
            currentListCourse = set(currentListCourse).intersection(newListCourses)
            currentListCourse = list(currentListCourse)
            newListCourses.clear()



        majorList = []
        yearList = []

        self.SQL_GetAllRequirements = " SELECT DISTINCT(Requirements)" \
                                      " FROM PROJECT_REQUIREMENTS" \

        self.cursor.execute(self.SQL_GetAllRequirements)
        requirements = self.cursor.fetchall()
        requirementsList = []
        for item in requirements:
            requirementsList.append(item[0])

        self.SQL_GetCorrespondingDepartment = " SELECT Department_Name" \
                                              " FROM MAJOR" \
                                              " WHERE Major_Name = %s"


        if self.majorFilter != "":
            majorList.append(self.majorFilter + " students only")
            self.cursor.execute(self.SQL_GetCorrespondingDepartment, (self.majorFilter))
            department = self.cursor.fetchall()
            majorList.append(str(department[0][0]) + " students only")
        else:
            majorList = requirementsList


        if self.yearFilter != "":
            yearList.append(self.yearFilter + " only")
        else:
            yearList = requirementsList

        self.SQL_ApplyFilterProject = " SELECT DISTINCT(P.Project_Name) FROM PROJECT AS P LEFT OUTER JOIN PROJECT_CATEGORY AS PC ON P.Project_Name = PC.Project_Name" \
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

        self.SQL_ApplyFilterCourse = " SELECT DISTINCT(C.Course_Name) FROM COURSE AS C LEFT OUTER JOIN COURSE_CATEGORY AS CC ON C.Course_Name = CC.Course_Name" \
                                     " WHERE C.Course_Name = CASE WHEN (%s != '') THEN %s ELSE C.Course_Name END" \
                                     " AND C.Designation_Name = CASE WHEN (%s != '') THEN %s ELSE C.Designation_Name END" \
                                     " AND CC.Category_Name = CASE WHEN (%s != '') THEN %s ELSE CC.Category_Name END "



        resultsProject = []
        results = []
        if self.projCourseSelection.get() == 0:
            self.cursor.execute(self.SQL_ApplyFilterProject, (
            self.title.get(), self.title.get(), majorList, self.majorFilter, yearList, self.yearFilter,
            self.designationFilter, self.designationFilter, self.categoryFilter, self.categoryFilter))
            resultsProject = self.cursor.fetchall()
        elif self.projCourseSelection.get() == 1:
            self.cursor.execute(self.SQL_ApplyFilterCourse, (
            self.title.get(), self.title.get(), self.designationFilter, self.designationFilter, self.categoryFilter, self.categoryFilter))
            results = self.cursor.fetchall()
        else:
            self.cursor.execute(self.SQL_ApplyFilterProject, (
            self.title.get(), self.title.get(), majorList, self.majorFilter, yearList, self.yearFilter,
            self.designationFilter, self.designationFilter, self.categoryFilter, self.categoryFilter))
            resultsProject = self.cursor.fetchall()

            self.cursor.execute(self.SQL_ApplyFilterCourse, (
            self.title.get(), self.title.get(), self.designationFilter, self.designationFilter, self.categoryFilter,
            self.categoryFilter))
            results = self.cursor.fetchall()


        self.newList = []
        self.currList = []
        self.finalProjectList = []
        self.finalCoursesList = []
        for i in resultsProject:
            self.finalProjectList.append(i[0])
        for i in results:
            self.finalCoursesList.append(i[0])




        self.finalProjectList = set(self.finalProjectList).intersection(currentList)
        self.finalProjectList = list(self.finalProjectList)

        self.finalCoursesList = set(self.finalCoursesList).intersection(currentListCourse)
        self.finalCoursesList = list(self.finalCoursesList)





        if self.projCourseSelection.get() == 0:
            for i in self.finalProjectList:
                self.currList.append(i)
                self.currList.append("Project")
                self.newList.append(tuple(self.currList))
                self.currList.clear()
        elif self.projCourseSelection.get() == 1:
            for row in self.finalCoursesList:
                self.currList.append(row)
                self.currList.append("Course")
                self.newList.append(tuple(self.currList))
                self.currList.clear()
        else:
            for row in self.finalCoursesList:
                self.currList.append(row)
                self.currList.append("Course")
                self.newList.append(tuple(self.currList))
                self.currList.clear()
            for row in self.finalProjectList:
                self.currList.append(row)
                self.currList.append("Project")
                self.newList.append(tuple(self.currList))
                self.currList.clear()


        for row in self.newList:
            self.table.insert('', 'end', value=row)

        self.newList.clear()

        self.table.bind("<Double-1>", self.showItem)


        currItem = self.table.focus()
        itemDict = self.table.item(currItem)
        courseInfo = itemDict.get('values')


    def showItem(self, event):
        currItem = self.table.focus()
        itemDict = self.table.item(currItem)
        projInfo= itemDict.get('values')
        projOrCourse = projInfo[1]
        self.showName = projInfo[0]



        if projOrCourse == "Project":
            self.mainPage.withdraw()
            self.ViewProject()
        else:
            self.mainPage.withdraw()
            self.ViewCourse()


    def ViewProject(self):

        self.Connect()
        self.cursor = self.db.cursor()

        self.viewProject = Toplevel()

        self.bigFrame = Frame(self.viewProject)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)


        self.SQL_GetProjectSpecs = " SELECT Advisor_Name, Advisor_Email, Description, Designation_Name, P_Est_Num_Students" \
                                   " FROM PROJECT AS P" \
                                   " WHERE P.Project_Name = %s"
        self.cursor.execute(self.SQL_GetProjectSpecs, (self.showName))
        self.projectSpecs = self.cursor.fetchall()

        projectInstructor = self.projectSpecs[0][0]
        projectInstructorEmail = self.projectSpecs[0][1]
        projectDescription = self.projectSpecs[0][2]
        projectDesignation = self.projectSpecs[0][3]
        projectNumStudents = self.projectSpecs[0][4]

        newProjectDescription = re.sub("(.{60})", "\\1\n", projectDescription, 0, re.DOTALL)



        projectRequirementsStr = ""
        projectCategoriesStr = ""
        self.SQL_GetProjectRequirements = " SELECT DISTINCT(Requirements)" \
                                          " FROM PROJECT AS P LEFT OUTER JOIN PROJECT_REQUIREMENTS AS PR ON P.Project_Name = PR.Project_Name" \
                                          " WHERE P.Project_Name = %s"
        self.cursor.execute(self.SQL_GetProjectRequirements, (self.showName))
        self.projectRequirements = self.cursor.fetchall()
        self.requirementsListApplyProj = []
        for item in self.projectRequirements:
            self.requirementsListApplyProj.append(item[0])
            projectRequirementsStr += re.sub('[(),\']', '', str(item)) #Regex expression to remove all unwanted chars from the string
            if item != self.projectRequirements[len(self.projectRequirements) - 1]:
                projectRequirementsStr += ", "


        self.SQL_GetProjectCategories = " SELECT DISTINCT(Category_Name)" \
                                        " FROM PROJECT AS P LEFT OUTER JOIN PROJECT_CATEGORY AS PC ON P.Project_Name = PC.Project_Name" \
                                        " WHERE P.Project_Name = %s"
        self.cursor.execute(self.SQL_GetProjectCategories, (self.showName))
        self.projectCategories = self.cursor.fetchall()
        for item in self.projectCategories:
            projectCategoriesStr += re.sub('[(),\']', '', str(item))
            if item != self.projectCategories[len(self.projectCategories) - 1]:
                projectCategoriesStr += ", "


        self.projectNameLb = Label(self.smallFrame, text = self.showName)
        self.projectNameLb.grid(row = 0, column = 2, padx = 20)

        self.projectAdvisorLb = Label(self.smallFrame, text = "Advisor: " + projectInstructor + " (" + projectInstructorEmail + ")")
        self.projectAdvisorLb.grid(row = 1, column = 2)

        self.projectDescriptionLb = Label(self.smallFrame, text = "Description: " + newProjectDescription)
        self.projectDescriptionLb.grid(row = 2, column = 2, sticky = W, pady = 10)

        self.projectDesignationLb = Label(self.smallFrame, text = "Designation: " + projectDesignation)
        self.projectDesignationLb.grid(row = 8, column = 2)


        self.projectRequirementsLb = Label(self.smallFrame, text = "Requirements: " + projectRequirementsStr)
        self.projectRequirementsLb.grid(row = 9, column = 2)

        self.projectCategoriesLb = Label(self.smallFrame, text = "Categories: " + projectCategoriesStr)
        self.projectCategoriesLb.grid(row = 10, column = 2)

        self.projectNumStudentsLb = Label(self.smallFrame, text = "Estimated number of students: " + str(projectNumStudents))
        self.projectNumStudentsLb.grid(row = 11, column = 2)

        self.backViewProjectBtn = Button(self.smallFrame, text = "Back", command = self.backToMainPageFromViewProject)
        self.backViewProjectBtn.grid(row = 12, column = 2)

        self.applyToProjectBtn = Button(self.smallFrame, text = "Apply", command = self.applyToProject)
        self.applyToProjectBtn.grid(row = 12, column = 4)

    def applyToProject(self):

        newList = []
        possibleMajorsList = []
        possibleYear = ""

        self.SQL_IsDepartment = " SELECT Department_Name" \
                                " FROM DEPARTMENT" \
                                " WHERE Department_Name = %s"

        self.SQL_GetMajorsInDept = " SELECT DISTINCT(Major_Name)" \
                                   " FROM MAJOR" \
                                   " WHERE Department_Name = %s"

        self.SQL_VerifyMajor = " SELECT *" \
                               " FROM STUDENT" \
                               " WHERE Major_Name IN %s AND Username = %s"

        self.SQL_VerifyYear = " SELECT *" \
                              " FROM STUDENT" \
                              " WHERE Year = %s AND Username = %s"

        self.SQL_HasAlreadyApplied = " SELECT *" \
                                     " FROM APPLY" \
                                     " WHERE Username = %s AND Project_Name = %s"

        self.SQL_UserApply = "INSERT INTO APPLY (Username, Project_Name, Date, Status) VALUES (%s, %s, '2016-12-04', 'Pending')"

        majorVerificationBool = 0
        yearVerificationBool = 0


        for stri in self.requirementsListApplyProj:
            stri = str(stri)
            stri = re.sub(' students only', '', stri)
            stri = re.sub(' only', '', stri)
            newList.append(stri)

            results = self.cursor.execute(self.SQL_IsDepartment, (stri))
            print(results)

            if stri == "Freshman" or stri == "Sophomore" or stri == "Junior" or stri == "Senior":
                possibleYear = stri
            elif results > 0:
                self.cursor.execute(self.SQL_GetMajorsInDept, (stri))
                results = self.cursor.fetchall()
                for item in results:
                    possibleMajorsList.append(item[0])
            else:
                possibleMajorsList.append(stri)

        if possibleMajorsList != []:
            print(possibleMajorsList)
            result = self.cursor.execute(self.SQL_VerifyMajor, (possibleMajorsList, self.userLogin))
            print(result)
            if result > 0:
                majorVerificationBool = 1
        else:
            majorVerificationBool = 1

        if possibleYear != "":
            result2 = self.cursor.execute(self.SQL_VerifyYear, (possibleYear, self.userLogin))
            if result2 > 0:
                yearVerificationBool = 1
        else:
            yearVerificationBool = 1

        hasApplied = self.cursor.execute(self.SQL_HasAlreadyApplied, (self.userLogin, self.showName))
        if hasApplied > 0:
            hasApplied = 0
        else:
            hasApplied = 1


        if yearVerificationBool and majorVerificationBool and hasApplied:
            self.cursor.execute(self.SQL_UserApply, (self.userLogin, self.showName))
        elif hasApplied == 0:
            messagebox.showwarning("Error", "You have already applied to this project")
        elif yearVerificationBool == 0:
            messagebox.showwarning("Error", "You are not the correct year")
        elif majorVerificationBool == 0:
            messagebox.showwarning("Error", "Your major cannot apply to this project")


    def backToMainPageFromViewProject(self):
        self.viewProject.withdraw()
        self.MainPage()


    def clearFilter(self):
        self.choiceVar.set("Please Select")
        self.choiceVarTwo.set("Please Select")
        self.choiceVarThree.set("Please Select")
        self.title.delete(0, 'end')
        self.categoriesListBox.delete(0, END)

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
                                     pady=20, command=self.showEditProfilePage)
        self.editProfileBtn.grid(row=2, column=2, sticky=E)
        self.myAppBtn = Button(self.smallFrame, width=1, text="My Application", padx=80,
                               pady=50, command=self.showApplicationPage)
        self.myAppBtn.grid(row=3, column=2, sticky=E)
        self.backBtn = Button(self.smallFrame, width=1, text="Back", padx=80,
                              command=self.backToMainPage)  # Need a command here as well
        self.backBtn.grid(row=4, column=2, stick=E)

    def backToMainPage(self):
        self.mePage.withdraw()
        self.MainPage()

    def showEditProfilePage(self):
        self.mePage.withdraw()
        self.EditProfilePage()

    def EditProfilePage(self):
        self.editProfilePage = Toplevel()

        self.bigFrame = Frame(self.editProfilePage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_GetMajoriEditProf = " SELECT Major_Name, Year" \
                                     " FROM STUDENT " \
                                     " WHERE Username = %s"

        self.cursor.execute(self.SQL_GetMajors)
        majorList = self.cursor.fetchall()
        majorChoices = []
        for major in majorList:
            majorChoices.append(major[0])

        self.cursor.execute(self.SQL_GetMajoriEditProf, (self.usernameEntry.get()))
        results = self.cursor.fetchall()
        defaultMajor = results[0][0]
        defaultYear = results[0][1]

        self.titleLbEditProf = Label(self.smallFrame, text="Edit Profile")
        self.titleLbEditProf.grid(row=0, column=2)

        self.majorEditProfLb = Label(self.smallFrame, text="Major")
        self.majorEditProfLb.grid(row=1, column=0)

        self.defaultMajorEditProf = defaultMajor
        self.defaultMajorEditProfStringVar = StringVar()
        self.defaultMajorEditProfStringVar.set(self.defaultMajorEditProf)
        self.majorEditProf = OptionMenu(self.smallFrame, self.defaultMajorEditProfStringVar, *majorChoices, command=self.updateMajor)
        self.majorEditProf.config(width=20)
        self.majorEditProf.grid(row=1, column=2)

        self.yearEditProfLb = Label(self.smallFrame, text="Year")
        self.yearEditProfLb.grid(row=2, column=0)

        self.defaultYearEditProf = defaultYear
        self.defaultYearEditProfStringVar = StringVar()
        self.defaultYearEditProfStringVar.set(self.defaultYearEditProf)
        self.yearEditProf = OptionMenu(self.smallFrame, self.defaultYearEditProfStringVar, "Freshman",
                                       "Sopohomore", "Junior", "Senior", command=self.updateYear)
        self.yearEditProf.config(width=20)
        self.yearEditProf.grid(row=2, column=2)

        self.departmentEditProfLb = Label(self.smallFrame, text="Department")

        self.backEditProfBtn = Button(self.smallFrame, text="Back", command=self.editProfile)
        self.backEditProfBtn.grid(row=3, column=2)

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
            self.majorFilter = self.defaultMajorEditProf  # Sets the filter to the default (inital) value if nothing is changed
        if self.yearFilter == '':
            self.yearFilter = self.defaultYearEditProf

        # Execute the SQL query
        self.cursor.execute(self.SQL_EditProfile, (self.majorFilter, self.yearFilter, self.usernameEntry.get()))

        self.editProfilePage.withdraw()
        self.MePage()

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

        self.myApplicationLb = Label(self.smallFrame, text="My Application")
        self.myApplicationLb.grid(row=0, column=2)

        self.dataColumns = ['Date', 'Project Name', 'Status']
        self.myAppsTreeView = ttk.Treeview(self.smallFrame, columns=self.dataColumns, show='headings')
        self.myAppsTreeView.grid(row=6, column=0, sticky=W, columnspan=5)
        self.myAppsTreeView.heading('#1', text="Date")
        self.myAppsTreeView.heading('#2', text="Project Name")
        self.myAppsTreeView.heading('#3', text="Status")

        self.backBtnAppPage = Button(self.smallFrame, text = "Back", command = self.backToMePage)
        self.backBtnAppPage.grid(row = 10, column = 2)

        for row in results:
            self.myAppsTreeView.insert('', 'end', value=row)


    def ViewCourse(self):
        self.Connect()
        self.cursor = self.db.cursor()

        self.viewCourse = Toplevel()

        self.bigFrame = Frame(self.viewCourse)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)


        self.SQL_GetCourseSpecs = " SELECT Course_Number, Instructor, Designation_Name, C_Est_Num_Students" \
                                  " FROM COURSE" \
                                  " WHERE Course_Name = %s"


        self.cursor.execute(self.SQL_GetCourseSpecs, (self.showName))
        results = self.cursor.fetchall()

        csNum = results[0][0]

        self.titleLbViewCourse = Label(self.smallFrame, text=csNum)
        self.titleLbViewCourse.grid(row=1, column=2)

        self.courseNameLb = Label(self.smallFrame, text = "Course Name: " + self.showName)
        self.courseNameLb.grid(row = 2, column = 0)

        self.instructorLb = Label(self.smallFrame, text = "Instructor: " + results[0][1])
        self.instructorLb.grid(row = 3, column = 0)

        self.designationLb = Label(self.smallFrame, text = "Designation: " + results[0][2])
        self.designationLb.grid(row = 4, column = 0)

        self.estNumLb = Label(self.smallFrame, text = "Estimated number of students: " + str(results[0][3]))
        self.estNumLb.grid(row = 5, column = 0)



    def backToAdminViewFunct(self):
        self.viewApplication.withdraw()
        self.AdminViewFunct()

    def backToAdminViewFunct2(self):
        self.viewPopularproject.withdraw()
        self.AdminViewFunct()

    def backToAdminViewFunct3(self):
        self.AppReport.withdraw()
        self.AdminViewFunct()
        

    def AdminViewFunct(self):
        self.adminPage = Toplevel()

        self.bigFrame = Frame(self.adminPage)
        self.bigFrame.grid(row=0, column=0)
        self.smallFrame = Frame(self.adminPage)
        self.smallFrame.grid(row=1, column=0)


        self.titleAdmin = Label(self.bigFrame, text="Choose Functionality", fg="blue", font=("Helvetica", 16))
        self.titleAdmin.grid(row=1, column=2, columnspan=2, padx=150,pady=5, sticky=N)

        self.viewAppBtn = Button(self.smallFrame, width=3, text="View Applications", padx=80,pady=10, command = self.ViewApplication)
        self.viewAppBtn.grid(row=2, column=2, sticky=E)
        self.myAppBtn = Button(self.smallFrame, width=3, text="View Popular Project Report", padx=80,pady=10, command = self.ViewPopularProject)
        self.myAppBtn.grid(row=3, column=2, sticky=E)
        
        self.viewAppReportBtn = Button(self.smallFrame, width=3, text="View Application Report", padx=80, pady=10, command = self.ViewApplicationReport)
        self.viewAppReportBtn.grid(row=4, column=2, sticky=E)
        self.addProjBtn = Button(self.smallFrame, width=3, text="Add a Project", padx=80, pady=10) #command = self.AddProjectFunction
        self.addProjBtn.grid(row=5, column=2, sticky=E)
        self.addCourseBtn = Button(self.smallFrame, width=3, text="Add a Course", padx=80,pady=10) #command = self.AddCourseFunction
        self.addCourseBtn.grid(row=6, column=2, sticky=E)

    def ViewApplication(self):
        self.adminPage.withdraw()
        
        self.viewApplication = Toplevel()
        self.bigFrame = Frame(self.viewApplication)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.viewApplication)
        self.smallFrame.grid(row=0, column=0)

        self.l1 = Label(self.smallFrame, text="Application", width=30, padx=5, pady=5, fg="blue", font=("Helvetica", 16))
        self.l1.grid(row=0, column=1)

        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_PopulateViewApps = "SELECT Project_Name, Major_Name, Year, Status, Username" \
                                    " FROM APPLY NATURAL JOIN STUDENT" \
                                    " ORDER BY Status"

        self.cursor.execute(self.SQL_PopulateViewApps)

        results = self.cursor.fetchall()
       
        
        self.dataColumns = ["Project", "Applicant Major", "Applicant Year", "Status", "Username"]
        self.AppsView = ttk.Treeview(self.smallFrame, columns=self.dataColumns, show = 'headings')
        self.AppsView.grid(row=6, column=0, sticky=W, columnspan=4)
        self.AppsView.heading('#1', text="Project")
        self.AppsView.heading('#2', text="Applicant Major")
        self.AppsView.heading('#3', text="Applicant Year")
        self.AppsView.heading('#4', text="Status")
        self.AppsView.heading('#5', text="Username")
        
        self.backBtn = Button(self.smallFrame, text = "Back", command = self.backToAdminViewFunct)
        self.backBtn.grid(row = 10, column = 1)

        self.acceptBtn = Button(self.smallFrame, text = "Accept", command = self.changeStatusToAccepted)
        self.acceptBtn.grid(row=10, column=8)

        self.rejectBtn = Button(self.smallFrame, text = "Reject", command = self.changeStatusToRejected)
        self.rejectBtn.grid(row=10, column=9)

        
        for row in results:
            self.AppsView.insert('', 'end', value = row)

            
    def changeStatusToAccepted(self):
        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_UpdateStatus = "UPDATE APPLY" \
                                " SET Status = 'Accepted'"\
                                " WHERE Project_Name = %s AND Username = %s"

        currentItem = self.AppsView.focus()
        itemDict = self.AppsView.item(currentItem)
        appInfo = itemDict.get("values")
        statusA = appInfo[3]
        userNameA = appInfo[4]
        projectName = appInfo[0]
        if statusA == "Pending":
            self.cursor.execute(self.SQL_UpdateStatus, (projectName, userNameA))
        else:
            messagebox.showinfo("Your status is not matching")
                
    def changeStatusToRejected(self):
        self.Connect()
        self.cursor = self.db.cursor()

        self.SQL_UpdateStatus = "UPDATE APPLY" \
                                " SET Status = 'Rejected'"\
                                " WHERE Project_Name = %s AND Username = %s"
        
        


        currentItem = self.AppsView.focus()
        itemDict = self.AppsView.item(currentItem)
        appInfo = itemDict.get("values")
        statusA = appInfo[3]
        userNameA = appInfo[4]
        projectName = appInfo[0]
        if statusA == "Pending":
            self.cursor.execute(self.SQL_UpdateStatus, (projectName, userNameA))
        else:
            messagebox.showinfo("Your status is not matching")
          
            
    def ViewPopularProject(self):
        self.adminPage.withdraw()
        
        self.viewPopularproject=Toplevel()
        self.bigFrame2=Frame(self.viewPopularproject)
        self.bigFrame2.grid(row=1, column=0)
        self.smallframe2=Frame(self.viewPopularproject)
        self.smallframe2.grid(row=0,column=0)

        self.l1 = Label(self.smallframe2, text="Popular Project", width=20, padx=5, pady=5, fg="blue", font=("Helvetica", 16))
        self.l1.grid(row=0, column=1)

        self.Connect()
        self.cursor=self.db.cursor()

        self.SQL_PopulateViewPopularProjects= "SELECT DISTINCT(Project_Name), COUNT(Project_Name)"\
                                              " FROM APPLY" \
                                              " GROUP BY Project_Name"\
                                              " ORDER BY COUNT(*) DESC"\
                                              " LIMIT 10"
        self.cursor.execute(self.SQL_PopulateViewPopularProjects)
        results=self.cursor.fetchall()



        self.dataColumns = ["Project","# of Applicants"]
        self.PopProjView = ttk.Treeview(self.smallframe2, columns=self.dataColumns, show = 'headings')
        self.PopProjView.grid(row=1, column=0, sticky=W, columnspan=2)
        self.PopProjView.heading('#1', text="Project")
        self.PopProjView.heading('#2', text="# of Applicants")

        self.backBtn = Button(self.smallframe2, text="Back", command=self.backToAdminViewFunct2)
        self.backBtn.grid(row=6, column=1, sticky=W)

        for row in results:

            self.PopProjView.insert('', 'end', value = row)


    def ViewApplicationReport(self):
        self.adminPage.withdraw()
        
        self.AppReport = Toplevel()

        self.bigFrame3 = Frame(self.AppReport)
        self.bigFrame3.grid(row=1, column=1)
        self.smallFrame2 = Frame(self.AppReport)
        self.smallFrame2.grid(row=0, column=1)

        self.titleAR = Label(self.smallFrame2, text="Application Report", fg="blue", font=("Helvetica", 16))
        self.titleAR.grid(row=0, column=1)

        self.Connect()
        self.cursor = self.db.cursor()
        
        
        self.SQL_Proj1 = "SELECT Project_Name, COUNT(*)" \
                        " FROM APPLY" \
                        " GROUP By Project_Name"
        self.cursor.execute(self.SQL_Proj1)
        results2 = self.cursor.fetchall()
        
        
        projList1 = []
        projList2 = []
        for x in results2:
            projName = x[0]
            self.SQL_Project1 = "SELECT Project_Name, COUNT(*)" \
                                " FROM APPLY" \
                                " WHERE Project_Name = %s AND Status = 'Accepted'"
            self.cursor.execute(self.SQL_Project1, (projName))
            results1 = self.cursor.fetchall()

            numAccepted = results1[0][1]
            totalApp = x[1]
            
            
            AcceptedPercentage = (numAccepted/totalApp) * 100


            AP2 = round(AcceptedPercentage, 1)
            AP3 = str(AP2)
            AP4 = AP3 + '%'
            newTup = (projName, totalApp, AP4)
            projList2.append(newTup)
                

        projList3 = []
        
        for x in projList2:
            projName2 = x[0]
            self.SQL_Major1 = "SELECT Major_Name" \
                              " FROM APPLY NATURAL JOIN STUDENT" \
                              " WHERE Project_Name = %s" \
                              " GROUP BY Major_Name" \
                              " ORDER BY COUNT(*) DESC" \
                              " LIMIT 3 "
            self.cursor.execute(self.SQL_Major1, (projName2))
            majors1 = self.cursor.fetchall()
            string1 = ''
            string2 = " / "
            for majorType in majors1:
                string1 = string1 + str(majorType[0])
                if majorType != majors1[len(majors1) - 1]:
                    string1 = string1 + string2
                
            newTup2 = (projName2, x[1], x[2], string1)
            projList3.append(newTup2)
            
        
        
        self.dataColumns2 = ["Project", "# of Applicants", "Accepance Rate", "Top 3 Majors"]
        self.AppReportView = ttk.Treeview(self.bigFrame3, columns=self.dataColumns2, show='headings')
        self.AppReportView.grid(row=1, column=0, sticky=W, columnspan=5)
        self.AppReportView.heading('#1', text="Project")
        self.AppReportView.heading('#2', text="# of Applicants")
        self.AppReportView.heading('#3', text="Acceptance Rate")
        self.AppReportView.heading('#4', text="Top 3 Majors")
        self.AppReportView.column('#4', minwidth=0, width=650)

        self.backBtn2 = Button(self.bigFrame3, text="Back", command=self.backToAdminViewFunct3)
        self.backBtn2.grid(row=6, column=2, sticky=W)

        for row in projList3:
            self.AppReportView.insert('', "end", value=row)


    '''
    self.SQL_ApplyFilterAdmin = " SELECT *" \
                                    " FROM PROJECT AS P LEFT OUTER JOIN PROJECT_CATEGORY AS PR ON P.Project_Name = PR.Project_Name" \
                                    " WHERE PR.Requirements IN %s"
    '''


    def backToMePage(self):
        self.applicationPage.withdraw()
        self.MePage()




win = Tk()
a = masterGUI(win)
win.mainloop()
