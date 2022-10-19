#https://www.youtube.com/watch?v=H71ts4XxWYU

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path=filedialog.askopenfilename()

print (file_path)

input("press any key to exit")