from tkinter import *

root=Tk()

#label widget
#define then place on screen

#creating label widget
myLabel1=Label(root, text="Hello World!")
myLabel2=Label(root, text="the text does not move when the row column method is used!")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1,column=0)

#event loop 