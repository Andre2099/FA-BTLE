#!/Usr/bin/python

from __future__ import division

import pyautogui as cntrl
import time

def fileMenu():
    #!OS specific!
    #get the top left xy coords of the file menu
    try:
        x,y,bx,by = cntrl.locateOnScreen('File.png')
        cntrl.moveTo(x, y)
        cntrl.moveRel(9,35)
        cntrl.click()
       
    except:
        cntrl.alert("oops...something went wrong with File menu. See Andre")

def exportPacketDissections(exportAs):
    #Warning! Only use this after calling fileMenu()
    fileMenu()
    #get mouse location
    x,y = cntrl.position()

    #scroll down and expand the "Export Packet Dissetions"
    xrel = 0
    yrel = 235
    cntrl.moveRel(xrel,yrel)
    cntrl.click()

    #dictionary map of export types in wireshark
    exportAsXYMap = {
        "Plain Text":(320,0),
        "PostScript":(320,16),
        "CSV":(320,36),
        "C Arrays":(320,54),
        "PSML":(320,66),
        "PDML":(320,87)        
        }

    xrel,yrel = exportAsXYMap[exportAs]
    cntrl.moveRel(xrel,yrel)
    cntrl.click()
    
    #!OS specific!
    #at this point the "save as" window appears.
    #go up levels until we get to the desktop.

    #need to put a delay in to allow the save window to open first
    time.sleep(0.25)

    #find the desktop location to make our way to the project folder
    x,y,bx,by = cntrl.locateOnScreen("save_as_window_leftIcons.png")
    cntrl.moveTo(x, y)
    cntrl.moveRel(0,143)
    cntrl.click()
    
    '''#find the pulldown menu
    x,y,bx,by = cntrl.locateOnScreen('save_as_pull_down.png')
    cntrl.moveTo(x, y)
    cntrl.click()
    x,y,bx,by = cntrl.locateOnScreen('desktop_pull_down.png')
    cntrl.click()'''

    #at this point we will be saving on the desktop. So we need to find our
    #investigation folder.
    

#do some timing stuff to allow wireshark to collect enough data
'''some code'''
#stop the capture
x,y,bx,by = cntrl.locateOnScreen("Stop.png")
cntrl.moveTo(x,y)
cntrl.click()
time.sleep(2)

#save the pcap file in the project folder
'''cntrl.hotkey('ctrl','s')'''
'''some code to enter filename with location'''

#export in specific format
exportPacketDissections("C Arrays")
invstgn_name = "BLAZE_238"
time.sleep(1)
cntrl.typewrite(invstgn_name+'\\')
#wait for saving to complete
time.sleep(2)
'''
#export in another specific format
exportPacketDissections("PDML")
#wait for saving to complete
'''

