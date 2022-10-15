from tkinter import *

root=Tk()

#define function for label
def myClick():
    myLabel=Label(root,text="Look! I clicked a Button!!")
    myLabel.pack()

#creating button
#fg foreground colour
#bg background colour # you can use hex colour codes
myButton=Button(root, text="Click me!",padx=50,pady=50, command=myClick, fg="blue")

#showing it on screen 
#using pack the text is always at the centre of window
myButton.pack()


#event loop 
root.mainloop()