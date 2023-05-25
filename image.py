from tkinter import *
from PIL import Image,ImageTk
win=Tk()
win.title("Image in tkinter")
win.geometry("500x600")
win.iconbitmap("C:/Users/Acer/Downloads/anh.bmp")

# Open the JPEG image
img1 = Image.open("C:/Users/Acer/OneDrive - Hanoi University of Science and Technology/Pictures/anh34xanh.JPG").resize((500,500))
img2= Image.open("C:/Users/Acer/OneDrive - Hanoi University of Science and Technology/Pictures/nam.jpg").resize((500,500))
img3=Image.open("C:/Users/Acer/OneDrive - Hanoi University of Science and Technology/Pictures/anh.jpg").resize((500,500))
# Convert the JPEG image to a supported format (e.g., PNG)

img1 = ImageTk.PhotoImage(img1.convert("RGBA"))
img2= ImageTk.PhotoImage(img2.convert("RGBA"))
img3= ImageTk.PhotoImage(img3.convert("RGBA"))

img_lst=[img1,img2,img3]
ind =0

mylabel=Label(image=img_lst[ind])
mylabel.grid(row=0,column=0,columnspan=3)
content=Label(win,text=f"image {ind} of {len(img_lst)}",relief=SUNKEN)
content.grid(row=2,column=0,columnspan=3,sticky=E,padx=20)
def back():
    global ind
    global mylabel
    global content
    content.grid_forget()
    mylabel.grid_forget()
    if ind==0:
        ind=len(img_lst)-1
    else:
        ind-=1
    mylabel=Label(image=img_lst[ind])
    mylabel.grid(row=0,column=0,columnspan=3)
    content=Label(win,text=f"image {ind+1} of {len(img_lst)}",relief=SUNKEN)
    content.grid(row=2,column=0,columnspan=3,sticky=E,padx=20)
def forward():
    global ind
    global mylabel
    mylabel.grid_forget()
    if ind==len(img_lst)-1:
        ind=0
    else:
        ind+=1
    mylabel=Label(image=img_lst[ind])
    mylabel.grid(row=0,column=0,columnspan=3)
    content=Label(win,text=f"image {ind+1} of {len(img_lst)}",relief=SUNKEN)
    content.grid(row=2,column=0,columnspan=3,sticky=E,padx=20)
back_but=Button(win,text="<<",command=back)
back_but.grid(row=1,column=0)
forward_but=Button(win,text=">>",command=forward)
forward_but.grid(row=1,column=2)
but=Button(win,text="EXIT",command=win.quit)
but.grid(row=1,column=1)

win.mainloop()