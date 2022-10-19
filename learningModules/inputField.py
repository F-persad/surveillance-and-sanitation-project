from tkinter import *

root = Tk()
#Nme of program
root.title("Get you name")

#input box
e=Entry(root, width=50, bg="pink", fg="purple", borderwidth=5)
e.pack()
e.get()

#default text in box
e.insert(0,"Enter you name: ")

def myClick():
    hola="Holddddda "+e.get()
    myLabel=Label (root, text="Hello " +e.get())
    myLabel2=Label(root, text=hola)
    myLabel.pack()
    myLabel2.pack()

myButton = Button(root, text="Enter your name", command =myClick)
myButton.pack()

root.mainloop()