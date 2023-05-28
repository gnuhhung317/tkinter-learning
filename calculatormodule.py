from tkinter import *
class MyGUI:
    def __init__(self):
        self.win=Tk()
        self.win.title("Simple calculator")
        self.entry=Entry(self.win,font=("Arial",20))
        self.entry.grid(row=0,column=0,columnspan=4)
        self.math=""
        self.equal=False
        self.f_num=float
        self.s_num=float

        but0=Button(self.win,text="0",padx=40,pady=20,command=lambda: self.click("0"))
        but1=Button(self.win,text="1",padx=40,pady=20,command=lambda: self.click("1"))
        but2=Button(self.win,text="2",padx=40,pady=20,command=lambda: self.click("2"))
        but3=Button(self.win,text="3",padx=40,pady=20,command=lambda: self.click("3"))
        but4=Button(self.win,text="4",padx=40,pady=20,command=lambda: self.click("4"))
        but5=Button(self.win,text="5",padx=40,pady=20,command=lambda: self.click("5"))
        but6=Button(self.win,text="6",padx=40,pady=20,command=lambda: self.click("6"))
        but7=Button(self.win,text="7",padx=40,pady=20,command=lambda: self.click("7"))
        but8=Button(self.win,text="8",padx=40,pady=20,command=lambda: self.click("8"))
        but9=Button(self.win,text="9",padx=40,pady=20,command=lambda: self.click("9"))
        but_clear=Button(self.win,text="AC",padx=38,pady=20,command=self.clear_click)
        but_equal=Button(self.win,text="=",padx=40,pady=20,command=self.equal_click)
        but_multi=Button(self.win,text="*",padx=40,pady=20,command=self.multiply_click)
        but_divde=Button(self.win,text="/",padx=40,pady=20,command=self.devide_click)
        but_add=Button(self.win,text="+",padx=40,pady=20,command=self.add_click)
        but_subtract=Button(self.win,text="-",padx=40,pady=20,command=self.subtract_click)


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

        self.win.mainloop()
    def click(self,num):
        if self.equal==True:
            text=num
        else:
            text=self.entry.get()+num
        self.entry.delete(0,END)
        self.entry.insert(0,text)
        self.equal=False
    def clear_click(self):
        self.entry.delete(0,END)
    def add_click(self):
        self.equal_click()
        if self.entry.get()!="":

            self.f_num=float(self.entry.get())
            self.math="+"
        self.entry.delete(0,END)
    def subtract_click(self):
        
        self.equal_click()
        if self.entry.get()!="":
            self.f_num=float(self.entry.get())
            self.math="-"
        self.entry.delete(0,END)
    def multiply_click(self):
        self.equal_click()
        if self.entry.get()!="":
            self.f_num=float(self.entry.get())
            self.math="*"
        self.entry.delete(0,END)
    def devide_click(self):
        
        self.equal_click()
        if self.entry.get()!="":
            self.f_num=float(self.entry.get())
            self.math="/"
        self.entry.delete(0,END)
    def equal_click(self):

        if self.entry.get()!="":
            self.s_num=float(self.entry.get())
        self.entry.delete(0,END)
        if self.math== "+":
            self.entry.insert(0,self.s_num+self.f_num)
        elif self.math== "-":
            self.entry.insert(0,self.s_num-self.f_num)
        elif self.math== "*":
            self.entry.insert(0,self.s_num*self.f_num)
        elif self.math== "/":
            if self.s_num!=0:
                self.entry.insert(0,self.f_num/self.s_num)
            else:
                self.entry.insert(0,"Math error")
        elif self.math=="":
            self.entry.insert(0,self.s_num)
        self.math=""
        self.equal=True
Ducung=MyGUI()