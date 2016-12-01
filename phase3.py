from tkinter import *
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

        #Setup
        self.win = win

        #Titles
        self.label1 = Label(self.win, text = "Login")
        self.label1.grid(row = 0, column = 0, columnspan = 2)

        #Initialize labels
        self.usernameLabel = Label(self.win, text = "Username")
        self.passwordLabel = Label(self.win, text = "Password")
        self.usernameLabel.grid(row = 1, column = 0)
        self.passwordLabel.grid(row = 2, column = 0)

        #Initialize entries
        self.usernameEntry = Entry(self.win, width = 20)
        self.usernameEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.passwordEntry = Entry(self.win, width = 20)
        self.passwordEntry.grid(row = 2, column = 1, padx = 5, pady = 5)

        #Initialize buttons
        self.btRegister = Button(self.win, width = 5, text = "Register", padx=5, pady=5, command = self.registerOpen)
        self.btRegister.grid(row = 3, column = 1, sticky=E)
        self.btLogin = Button(self.win, width = 5, padx=5, pady=5, text = "Login", command = self.LoginCheck)
        self.btLogin.grid(row = 3, column = 1, sticky=W)

    def showWin(self):
        self.win.deiconify()
        self.registerpage.withdraw()

    def Connect(self):
        try:
            self.db = pymysql.connect(host="academic-mysql.cc.gatech.edu",passwd="Z8IHtiyg",user="cs4400_Team_9",db="cs4400_Team_9")
            self.cursor = self.db.cursor()
        except:
            raise
            messagebox.showinfo("Connection error. Check your Internet Connection and/or code!")


    def registerOpen(self):
        self.win.withdraw()
        self.RegisterPage()

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
        self.cp = Entry(self.smallFrame, width=50)
        self.cp.grid(row=4, column=1, sticky=E, pady=5)

        regButton = Button(self.bigFrame, text="Create", width=10, bg="white",command = self.RegisterNew)
        regButton.grid(row=7, column=0)

    
    def RegisterNew(self):
        self.Connect()
        self.sql = "SELECT Username,GT_Email,Password FROM STUDENT"

        self.cursor.execute(self.sql)
        information = self.cursor.fetchall()
        self.db.close()

        self.uname = self.usernameReg.get()
        self.passw = self.passwordReg.get()
        self.passconf = self.cp.get()
        self.emailconf = self.email.get()
        null = "0"

        if self.uname == "" or self.passw == "" or self.passconf == "" or self.emailconf == "":
            messagebox.showwarning("Error!", "Cannot have empty field")
        elif self.passconf != self.passw:
            messagebox.showwarning("Error", "Passwords do not match! Try again.")
        elif "@gatech.edu" not in self.emailconf:
            messagebox.showwarning("Error!", "Please enter valid email")
        else:
            fruit = True
            for each in information:
                if self.emailconf in each:
                    messagebox.showwarning("Error", "Email already in system! Please try again!")
                elif self.uname in each:
                    messagebox.showwarning("Error", "Username already in system. Please try again!")
                    fruit = False
                if fruit:
                    self.Connect()
                    self.sql2 = "INSERT INTO STUDENT(Username, GT_Email, Password, Year, Major_Name) VALUES(%s,%s,%s,%s,%s)"
                    self.cursor.execute(self.sql2,(self.uname,self.emailconf,self.passw,null,null))
                    self.db.commit()
                    self.db.close()
                    messagebox.showwarning("Successful Registration!", "Please log in!")
                    self.showWin()
                    
            
    def LoginCheck(self):
        self.Connect()

        self.userLogin = self.usernameEntry.get()
        self.passLogin = self.passwordEntry.get()

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
        self.mainpage = Toplevel()
        self.bigFrame = Frame(self.mainPage)
        self.bigFrame.grid(row=1, column=0)
        self.smallFrame = Frame(self.bigFrame)
        self.smallFrame.grid(row=0, column=0)

        self.titleReg = Label(self.smallFrame,text="Main Page", width=30, padx=5, pady=5, fg="blue", font=("Helvetica", 16))
        self.titleReg.grid(row=0, column=1)
        self.usernameReg = Entry(self.smallFrame, width=50)
        




win = Tk()
a = masterGUI(win)
win.mainloop()
