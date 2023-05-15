from haha import *
win =Tk()
win.title("Đức Hùng học entry")
win.geometry("400x500")
win.attributes("-topmost",True)
entry= Entry(win,font=("Time New Roman",12),width=20,bg="yellow",fg="pink")
entry.pack()
entry.focus()#tự trỏ vào cái ô nhập vào


win.mainloop()