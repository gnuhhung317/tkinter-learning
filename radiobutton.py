from tkinter import *

win=Tk()
win.title("Radiobutton")
win.geometry("600x600")
win.iconbitmap("anh8.ico")
r=IntVar()
r.get()
def clickradio():
    Label(win,text=r.get()).place(x=290,y=60)
Radiobutton(win,text="Handsome",variable=r,value=1,command=clickradio).pack()
Radiobutton(win,text="Inteligent",variable=r,value=2,command=clickradio).pack()

win.mainloop()



