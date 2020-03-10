from tkinter import *
import time
x=Tk()

x.geometry("700x500+400+100")
x.resizable(False,False)
lf1=LabelFrame(x,bg="Yellow")
lf1.place(x=0,y=0,h=180,w=700)

l1=Label(lf1,text="Python Quiz",font=("Cambria",30,"bold"))
l1.pack()

b1=Button(lf1,text="Start",font=("Times New Roman",16))
b1.place(x=10,y=80,h=35,w=50)

b2=Button(lf1,text="Stop",font=("Times New Roman",16))
b2.place(x=10,y=130,h=35,w=50)

f1=Frame(x)
#r1=Radiobutton()

x.mainloop()