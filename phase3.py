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
        self.btRegister = Button(self.win, width = 5, text = "Register")
        self.btRegister.grid(row = 3, column = 1, sticky=E)
        self.btLogin = Button(self.win, width = 5, text = "Login", command = self.LoginCheck)
        self.btLogin.grid(row = 3, column = 1, sticky=W)

    #def LoginCheck(self):
        #self.db2 = self.Connect()

<<<<<<< HEAD
        #self.userLogin = self.
#Neeltest    
        
=======
class studentRegistration:

    def __init__(self, win):
        self.win = win

        self.lbTitle = Label(self.win, text = "Student Register")
        self.lbTitle.grid(row = 0, column = 0, columnspan = 2)

        self.lbUsername = Label(row = 0)
        self.stuff


>>>>>>> refs/remotes/origin/rauten

        
        




win = Tk()
a = masterGUI(win)
win.mainloop()
