from tkinter import *

root=Tk()

#label widget
#define then place on screen

#creating label widget
myLabel=Label(root, text="Hello World!")

#showing it on screen 
#using pack the text is always at the centre of window
myLabel.pack()


#event loop 
root.mainloop()