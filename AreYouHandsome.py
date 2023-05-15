from tkinter import *
from tkinter import messagebox
class MyGUI:

    def __init__(self) :
        self.win =Tk()
        self.win.geometry("500x500")
        self.label=Label(self.win,text="Enter your name",font=("Airal",16))
        self.label.pack(padx=10,pady=10)

        self.textbox=Text(self.win,font=("Arial",16),height=2)
        self.textbox.pack(padx=10,pady=10)

        self.check_state = IntVar()

        self.checkbut=Checkbutton(self.win, text="Are u handsome",font=("Arial",16),variable=self.check_state)
        self.checkbut.pack(padx=10,pady=10)
        
        self.button= Button(self.win,text="Show message",font=("Arial",18),command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.win.mainloop()

    def show_message(self):
        getstr=self.textbox.get("1.0",END).strip("\n")
        if self.check_state.get()==1:
            if len(getstr)>0:
                hi="Yeah,right! "+getstr+" is so handsome"
            else:
                hi="Enter something"
    
        else:
            hi="Don't be inferiority, "+getstr
            
            
        messagebox.showinfo(title="Message",message=hi)
MyGUI()
