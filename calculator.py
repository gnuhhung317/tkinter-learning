from tkinter import *

win=Tk()
win.title("simple caculator")
entry=Entry(win,font=("Aria",20))
entry.grid(row=0,column=0,columnspan=4)


def click(num):
    text=entry.get()+num
    entry.delete(0,END)
    entry.insert(0,text)
def clear_click():
    entry.delete(0,END)
def add_click():
    global f_num
    global math
    if entry.get()!="":

        f_num=float(entry.get())
        math="+"
    entry.delete(0,END)
def subtract_click():
    global f_num
    global math
    if entry.get()!="":
        f_num=float(entry.get())
        math="-"
    entry.delete(0,END)
def multiply_click():
    global f_num
    global math
    if entry.get()!="":
        f_num=float(entry.get())
        math="*"
    entry.delete(0,END)
def devide_click():
    global f_num
    global math

    if entry.get()!="":
        f_num=float(entry.get())
        math="/"
    entry.delete(0,END)
def equal_click():
    global s_num
    global math
    if entry.get()!="":
        s_num=float(entry.get())
    entry.delete(0,END)
    if math== "+":
        entry.insert(0,s_num+f_num)
    elif math== "-":
        entry.insert(0,s_num-f_num)
    elif math== "*":
        entry.insert(0,s_num*f_num)
    elif math== "/":
        entry.insert(0,f_num/s_num)
    
    math=""

but0=Button(win,text="0",padx=40,pady=20,command=lambda: click("0"))
but1=Button(win,text="1",padx=40,pady=20,command=lambda: click("1"))
but2=Button(win,text="2",padx=40,pady=20,command=lambda: click("2"))
but3=Button(win,text="3",padx=40,pady=20,command=lambda: click("3"))
but4=Button(win,text="4",padx=40,pady=20,command=lambda: click("4"))
but5=Button(win,text="5",padx=40,pady=20,command=lambda: click("5"))
but6=Button(win,text="6",padx=40,pady=20,command=lambda: click("6"))
but7=Button(win,text="7",padx=40,pady=20,command=lambda: click("7"))
but8=Button(win,text="8",padx=40,pady=20,command=lambda: click("8"))
but9=Button(win,text="9",padx=40,pady=20,command=lambda: click("9"))
but_clear=Button(win,text="AC",padx=38,pady=20,command=clear_click)
but_equal=Button(win,text="=",padx=40,pady=20,command=equal_click)
but_multi=Button(win,text="*",padx=40,pady=20,command=multiply_click)
but_divde=Button(win,text="/",padx=40,pady=20,command=devide_click)
but_add=Button(win,text="+",padx=40,pady=20,command=add_click)
but_subtract=Button(win,text="-",padx=40,pady=20,command=subtract_click)


but0.grid(row=4,column=0)
but_equal.grid(row=2,column=3)
but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)
but_clear.grid(row=1,column=3)
but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)
but_multi.grid(row=3,column=3)
but7.grid(row=3,column=0)
but8.grid(row=3,column=1)
but9.grid(row=3,column=2)
but_divde.grid(row=4,column=3)
but_add.grid(row=4,column=2)
but_subtract.grid(row=4,column=1)

win.mainloop()