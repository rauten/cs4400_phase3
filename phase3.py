from Tkinter import *
import re
import string

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
        self.btLogin = Button(self.win, width = 5, text = "Login")
        self.btLogin.grid(row = 3, column = 1, sticky=W)




win = Tk()
a = masterGUI(win)
win.mainloop()