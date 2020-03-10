from tkinter import *
t=Tk()
'''
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   print(selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()

root.mainloop()'''

def Count(i):
   print(i)
   i=i+1
   print(i)
   print(i)

t.geometry("700x500+400+100")

b1 = Button(t, text="Start", font=("Times New Roman", 16),command=Count(i=0))
''',command=lambda:Countdown(120)'''
b1.place(x=3, y=7, h=35, w=50)

t.mainloop()
