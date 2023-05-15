from haha import *

win = Tk()
win.title("Duc Hung leanr to link label button and entry")
win.geometry("400x500")
win.attributes("-topmost", True)
# make label
username = Label(win, font=("arial", 14), text="username: ")
username.place(x=20, y=20)
# make entry
userentry = Entry(win, font=("arial", 14), width=18)
userentry.place(x=140, y=20)
userentry.focus()
# make button


def click():
    printsuc = Label(win, text=userentry.get()+" logined",
                     font=("arial", 15), width=18)
    printsuc.place(x=70, y=110)


but = Button(win, text=("Log in"), fg="black",
             bg="grey", width=20, command=click)
but.place(x=110, y=70)


win.mainloop()
