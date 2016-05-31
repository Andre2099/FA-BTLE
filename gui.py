#!/Usr/bin/Python
'''This GUI is intended to automate the nordic bluetooth le sniffer,
   and the collection of wireshark data. It creates folders for FA
   investigations based on assigned FA cases.
   
   Author: F. Andre Bertomeu
   Title: FA Firmware Engineer
   Date Created: 5/26/2016
   Last update: 5/31/2016
   Ver: ??.???.???

   Comments: For the sake of time I just created this incrementally. The buttons and layout I got just right then just copied and paste more.
   I don't like this implementation. See the to do list below.

   To Do:
       - Create a Git repo and push on to it ASAP!
       - Make the buttons one class, then invoke each button as an object.
   '''

from __future__ import division

from Tkinter import *
from tkFileDialog import *
import sys

mainWindow = Tk()
mainWindow.wm_title("Maestro: Fitbit BTLE Traffic Analyzer")
mainWindow.wm_iconbitmap('favicon.ico')

def callbackPlaceHolder():
    #this callback does nothing, it just a placeholder for testing gui
    print "Button pressed"

def fileNew():
    print "steps out of any investigation folder if its in one, then clears the text fields."
    print "should have a Save pop up with a window to enter investigation number"
    print "this Investigation number should go in a variable for file access."

def fileSave():
    print "Saves the report file wherever you would like"

def fileOpen():
    #this is a placeholder for file>open menu item.
    print "file open"

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
invstgn_ID_value="No Investigation Open..."
Label(frame, text=invstgn_ID_value, font="Helvetica 8 italic").grid(row=1,column=0)
#invstgn_ID_field = Entry(frame).grid(row=1,column=0)

##==--==GetID==--==--##
getDevIDButton = Button(frame, text="Get ID", height=4, width=15, command=callbackPlaceHolder).grid(row=2,column=0,pady=(10,0))
devIDdata = "ff:ff:ff:ff:ff:ff"
devIDScrollBar = Scrollbar(frame) #create a scrollbar
#attach the scrollbar to the text window, disable user editing of contents. 
devIDResult = Text(frame, height=4, width=35)
devIDResult.grid(row=2,column=1,sticky=W, pady=(10,0))

devIDScrollBar.grid(row=2,column=2,sticky=E+N+S, pady=(10,0))
#update the text window with data
devIDResult.insert(END, devIDdata)
devIDScrollBar.config(command=devIDResult.yview)
devIDResult.config(yscrollcommand=devIDScrollBar.set)

#configure the text widget to not allow user input
devIDResult.config(state=DISABLED)

#add radio buttons

##==--==Capture Response==--==--##
capRspnButton = Button(frame, text="Capture Response", height=4, width=15, command=callbackPlaceHolder).grid(row=3,column=0,pady=(10,0))
responseData= "Advertising Packets OK...\nReponse detected...\n"
capRspnScrollBar = Scrollbar(frame) #create a scrollbar
#attach the scrollbar to the text window, disable user editing of contents. 
capRspnResult = Text(frame, height=4, width=35)
capRspnResult.grid(row=3,column=1,sticky=W, pady=(10,0))

capRspnScrollBar.grid(row=3,column=2,sticky=E+N+S, pady=(10,0))
#update the text window with data
capRspnResult.insert(END, responseData)
capRspnScrollBar.config(command=capRspnResult.yview)
capRspnResult.config(yscrollcommand=capRspnScrollBar.set)

#configure the text widget to not allow user input
capRspnResult.config(state=DISABLED)

##==--==Capture Sync==--==--##
capSyncButton = Button(frame, text="Capture Sync", height=4, width=15, command=callbackPlaceHolder).grid(row=4,column=0,pady=(10,0))
syncData= "Connection Request...\nTime interval check...\n"
capSyncScrollBar = Scrollbar(frame) #create a scrollbar
#attach the scrollbar to the text window, disable user editing of contents. 
capSyncResult = Text(frame, height=4, width=35)
capSyncResult.grid(row=4,column=1,sticky=W, pady=(10,0))

capSyncScrollBar.grid(row=4,column=2,sticky=E+N+S, pady=(10,0))
#update the text window with data
capSyncResult.insert(END, syncData)
capSyncScrollBar.config(command=capSyncResult.yview)
capSyncResult.config(yscrollcommand=capSyncScrollBar.set)

#configure the text widget to not allow user input
capSyncResult.config(state=DISABLED)

##==--==Capture Notification==--==--##
capNtfnButton = Button(frame, text="Capture Notification", height=4, width=15, wraplength=100, command=callbackPlaceHolder).grid(row=5,column=0,pady=(10,0))
notificationData= "Opcode num...\nTime interval check...\n"
capNtfnScrollBar = Scrollbar(frame) #create a scrollbar
#attach the scrollbar to the text window, disable user editing of contents. 
capNtfnResult = Text(frame, height=4, width=35)
capNtfnResult.grid(row=5,column=1,sticky=W, pady=(10,0))

capNtfnScrollBar.grid(row=5,column=2,sticky=E+N+S, pady=(10,0))
#update the text window with data
capNtfnResult.insert(END, syncData)
capNtfnScrollBar.config(command=capNtfnResult.yview)
capNtfnResult.config(yscrollcommand=capNtfnScrollBar.set)

#configure the text widget to not allow user input
capNtfnResult.config(state=DISABLED)

mainWindow.mainloop()


