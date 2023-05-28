from tkinter import *
from tkinter import messagebox

win=Tk()
win.title("Frame learning")
win.iconbitmap("anh8.ico")

frame=LabelFrame(win,text="This is my frame..",padx=50,pady=50)
frame.pack(padx=10,pady=10)
b=Button(frame,text="HAHA")
b.pack()

win.mainloop()