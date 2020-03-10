from tkinter import *
from firebase import firebase
import random
import time
import os



A=NONE
B=NONE
C=NONE
D=NONE
Ans=NONE
res=NONE
l2 = NONE
r1=NONE
r2=NONE
r3=NONE
r4=NONE
r=NONE
qunosup=1


firebase = firebase.FirebaseApplication('https://python-mcq-12fd2.firebaseio.com/', None)

def Start():
    Change(1)


def Change(quno):
    qunosup = quno
    #takecommand(qunosup)
    print("Print QU",qunosup)
    stres = str('/Q'+str(quno)+'/Qu/')
    res = firebase.get(stres, '')

    print(res)

    A = firebase.get('/Q'+str(quno)+'/A/', '')

    B = firebase.get('/Q'+str(quno)+'/B/', '')

    C = firebase.get('/Q'+str(quno)+'/C/', '')

    D = firebase.get('/Q'+str(quno)+'/D/', '')

    Ans = firebase.get('/Q'+str(quno)+'/ANS/', '')

    print("Answer:- ",Ans)

    l2 = Label(x, text=res, font=("Times New Roman", 20), bg="Blue")
    l2.place(x=0, y=60, h=100, w=700)

    r1 = Radiobutton(x, text=A, font=("Times New Roman", 16), value=A, variable=i)
    print(i)
    r1.place(x=60, y=200, h=50, w=150)

    r2 = Radiobutton(x, text=B, font=("Times New Roman", 16), value=B, variable=i)
    r2.place(x=500, y=200, h=50, w=150)

    r3 = Radiobutton(x, text=C, font=("Times New Roman", 16), value=C, variable=i)
    r3.place(x=60, y=350, h=50, w=150)

    r4 = Radiobutton(x, text=D, font=("Times New Roman", 16), value=D, variable=i)
    r4.place(x=500, y=350, h=50, w=150)



x = Tk()
x.quno2=1
p1 = PhotoImage(file="previous.png")
p2 = PhotoImage(file="next.png")
i = StringVar()



def MCQCheck(quno):
    Ans = firebase.get('/Q'+str(quno)+'/ANS/', '')
    print(quno)
    r = str(i.get())
    print("You have Selected:-",r)
    print(Ans)
    if r == Ans:
        print("You are Right")
    else:
        print("You are Wrong")
    x.quno2+=1
    Change(x.quno2)

def Prevous(quno):
    x.quno2 -= 1
    Change(x.quno2)


'''def takecommand(quno):
    qunosup=quno
    print("takecmd:-",qunosup)
    quno2=qunosup'''






x.geometry("700x500+400+100")
x.resizable(False, False)
l1 = Label(x, text="Python Quiz", font=("Cambria", 30, "bold"), bg="Yellow")
l1.place(x=0, y=0, h=50, w=700)

b1 = Button(x, text="Start", font=("Times New Roman", 16),command=Start)
''',command=lambda:Countdown(120)'''
b1.place(x=3, y=7, h=35, w=50)

b2 = Button(x, text="Stop", font=("Times New Roman", 16))
b2.place(x=70, y=7, h=35, w=50)

l2 = Label(x, text=res, font=("Times New Roman", 20), bg="Blue")
l2.place(x=0, y=60, h=100, w=700)

r1 = Radiobutton(x, text=A, font=("Times New Roman", 16), value=A,variable=i)
print(i)
r1.place(x=60, y=200, h=50, w=150)

r2 = Radiobutton(x, text=B, font=("Times New Roman", 16),value=B,variable=i)
r2.place(x=500, y=200, h=50, w=150)

r3 = Radiobutton(x, text=C, font=("Times New Roman", 16),value=C,variable=i)
r3.place(x=60, y=350, h=50, w=150)

r4 = Radiobutton(x, text=D, font=("Times New Roman", 16),value=D,variable=i)
r4.place(x=500, y=350, h=50, w=150)

b1 = Button(x, image=p1, font=("Times New Roman", 16), border=0,command=lambda:Prevous(x.quno2))
b1.place(x=20, y=430, h=50, w=50)

b2 = Button(x, image=p2, font=("Times New Roman", 16), border=0,command=lambda:MCQCheck(x.quno2))
b2.place(x=630, y=430, h=50, w=50)


x.mainloop()
