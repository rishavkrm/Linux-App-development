#!/usr/bin/env python

from microscope import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from zoom import *

#Main Window
main = Tk()
main.title("Medical Slide Scanner")
main.geometry("1280x800")

# Creating Menubar
menubar = Menu(main)

#Open a file
def OpenFile():
    main.filename = filedialog.askopenfilename(initialdir = "/pi", title = "Select", filetypes = (("png files","*.png"),("jpg files",".jpg"),("All files","*.*")))
    Open_file = Label(main, text=main.filename).pack()

#Save a file
def SaveFileAs():
    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)


#New Window
def CreateNewWindow():
    
    #Creating new window
    Untitled = Toplevel()
    Untitled.title("Untitled.mss")
    Untitled.geometry("1280x800")

    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='New File', command = CreateNewWindow)
    file.add_command(label ='Open File', command = OpenFile)
    file.add_command(label ='Save As', command = lambda: SaveFileAs())
    file.add_separator()
    file.add_command(label ='Exit', command = main.destroy)
    
    # Adding Edit Menu and commands
    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Edit', menu = edit)
    edit.add_command(label ='Cut', command = None)
    edit.add_command(label ='Copy', command = None)
    edit.add_command(label ='Paste', command = None)
    edit.add_command(label ='Select All', command = None)
    edit.add_separator()
    edit.add_command(label ='Find...', command = None)
    edit.add_command(label ='Find again', command = None)
    
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)
    
    # display Menu
    main.config(menu = menubar)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = CreateNewWindow)
file.add_command(label ='Open File', command = OpenFile)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = main.destroy)
  
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# display Menu
main.config(menu = menubar)

#Microsope
#canvas = Canvas(main, width = 500, height = 500)
#canvas.pack()
#blood = ImageTk.PhotoImage(Image.open('blood.jpeg'))
#canvas.create_image(100,100,anchor = CENTER, image = blood)
photo = Image.open("blood.jpeg")
photo = photo.resize((100,100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)
label = Label(main, image = img, ).pack()

#Zooming



main.mainloop()
