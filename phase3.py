from Tkinter import *
import re
import string

class masterGUI:

    def __init__(self, win):
        self.win = win
        self.label1 = Label(self.win, text = "Login")
        self.label1.grid(row = 0, column = 0, columnspan = 2)
        #Niharchange
