from tkinter import *

root = Tk()

#Creating the label widject and display 
#not as clean code as doing it in two separate stepsdddd
MyLabel1=Label(root, text="Hello World!").grid(row=0,column=0)
MyLabel2=Label(root, text="Hello World againnn!").grid(row=1,column=5)

root.mainloop()