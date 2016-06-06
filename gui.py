#!/Usr/bin/Python
'''This GUI is intended to automate the nordic bluetooth le sniffer,
   and the collection of wireshark data. It creates folders for FA
   investigations based on assigned FA cases.
   
   Author: F. Andre Bertomeu
   Title: FA Firmware Engineer
   Date Created: 5/26/2016
   Last update: 6/5/2016
   Ver: ??.???.???

   Comments: For the sake of time I just created this incrementally. The buttons and layout I got just right then just copied and paste more.
   I don't like this implementation. See the to do list below.
   Created a class for buttons with the text widget. Way cleaner.

   To Do:
       - Create flag for investigation open via File->New.. or File->Open.. and have buttons check. This is to ensure that the user wont be running tests in garbage directory.
       - use os.makedirs(directory) for file->New... don't forget to check if it doesn't already exist with os.path.exists
       - Add radio buttons to select the type of characterization file. 

   '''

from __future__ import division

import Tkinter,tkFileDialog
from Tkinter import *
from tkFileDialog import *
import sys, time
import pathlib
from pathlib import *

mainWindow = Tk()
mainWindow.wm_title("Maestro: Fitbit BTLE Traffic Analyzer")
mainWindow.wm_iconbitmap('favicon.ico')

# defining options for accessing a directory
dir_opt = options = {}
options['initialdir'] = 'C:\\'
options['mustexist'] = True
options['parent'] = mainWindow
options['title'] = 'Location for the investigation'

#flags
invstg_opened_flag = 0 #to tell if any investigation was opened.

#the rest of globals
invstgn_ID = StringVar()
invstgn_ID.set("No Investigation Open...")

def callbackPlaceHolder():
    #this callback does nothing, it just a placeholder for testing gui
    print "Button pressed"
    getDevID.addData("ff:ff:ff:ff:ff:ff")

def fileNew():
    print "steps out of any investigation folder if its in one, then clears the text fields,"
    print "and the directory variable. Pretty much like closing everything and opening it up fresh." 
    print "Should have a Save pop up with a window to enter investigation number"
    print "this Investigation number will be the directory name that will be created."
    print "the directory path is then saved in the investigation directory variable."
    print "Make sure to check first if directory already exists."
    print "when an investigation is created, make a investigation .inv file. \n Look for this file to exist when doing File->Open..." 

def fileSave():
    print "Saves the report file wherever you would like"

def fileOpen():
    #this is for file>open menu item.
    print "file open"
    global invstgn_directory
    invstgn_directory = pathlib.Path(tkFileDialog.askdirectory(**dir_opt))
    #debug
    print invstgn_directory
    invstgn_ID.set(str(invstgn_directory).split("\\")[-1])
    #get the folder name
    
    #check this flag in the button callbacks before trying to read files
    invstgn_opened_flag = 1

def fileClose():
    print "Closes the investigation"
    print "should clear all fields and variables"
    print "ready for file->open or file->new"
    print "it should also start in this state"

def editClear():
    print "Clears the text widgets."

def fileExit():
    print "Quitting program"
    #mainWindow.quit
    #sys.exit
    raise SystemExit

#====MENU BAR====    
#-create a menu bar
menubar = Menu(mainWindow)

#--create the 'File' menu
filemenu = Menu(menubar,tearoff=0)
#--create items in the 'File' pulldown
filemenu.add_command(label="New Investigation",command=fileNew)
filemenu.add_command(label="Open Investigation",command=fileOpen)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=fileExit)
#--add the pulldown to the menubar
menubar.add_cascade(label="File",menu=filemenu)
#display the menu
mainWindow.config(menu=menubar)

frame = Frame(mainWindow)
frame.grid(padx=10, pady=10)

Label(frame, text = "Investigation ID:", font="TkDefaultfont 9").grid(row=0,column=0,sticky=W)
Label(frame, textvariable=invstgn_ID, font="Helvetica 8 italic").grid(row=1,column=0)
#invstgn_ID_field = Entry(frame).grid(row=1,column=0)

##==--==Button-And-Window Class==--==--##
class ButtonAndText:
    def __init__(self,master,name,row,column):
        self.row = row
        self.column = column
        self.name = name
        self.button = Button(frame, text=self.name, height=4, width=15, wraplength=100, command=callbackPlaceHolder).grid(row=self.row,column=self.column,pady=(10,0))
        #create a scrollbar
        self.scrollbar = Scrollbar(frame)
        #attach the scrollbar to the text window, disable user editing of contents. 
        self.textwidget = Text(frame, height=4, width=35)
        self.textwidget.grid(row=self.row,column=self.column+1,sticky=W, pady=(10,0))
        self.scrollbar.grid(row=self.row,column=self.column+2,sticky=E+N+S, pady=(10,0))
        self.scrollbar.config(command=self.textwidget.yview)
        self.textwidget.config(yscrollcommand=self.scrollbar.set)

        #add radio buttons
        pass
    
    def addData(self,data):
        #allow the text widget to be updated
        self.textwidget.config(state=NORMAL)
        self.data = data
        #update the text window with data
        self.textwidget.insert(END, self.data)
        self.textwidget.see(Tkinter.END)
        mainWindow.update()
        #prevent user from editing contents
        self.textwidget.config(state=DISABLED)

getDevID = ButtonAndText(frame,"Get ID",2,0)
capRspn = ButtonAndText(frame,"Capture Response",3,0)
capRspn.addData("Advertising Packets OK...\nReponse detected...\n")
capSync = ButtonAndText(frame,"Capture Sync",4,0)
capSync.addData("Connection Request...\nTime interval check...\n")
capNtfn = ButtonAndText(frame,"Capture Notification",5,0)
capNtfn.addData("Opcode num...\nTime interval check...\n")
mainWindow.mainloop()


