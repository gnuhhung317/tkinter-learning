from haha import *
from PIL import ImageTk, Image
win = Tk() #tạo một cửa sổ
win.title("Đức Hùng học GUI") #tạo tiêu đề
win.geometry("500x700") #tạo CD-CR
win.attributes("-topmost",True)
img_imp=(Image.open(r'C:\Users\Acer\Documents\Zalo Received Files\z3931861965485_464484f2211f3e89498a2cbb25f48fcb.jpg'))
resize = img_imp.resize((1500,1500),Image.ANTIALIAS)
img =ImageTk.PhotoImage(resize)

pic=Button(win, text="hihi", font=("arial",12),image=img)
pic.place(x=10,y=20)




win.mainloop()