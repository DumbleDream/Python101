from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมอะไรเอ่ย...?')
GUI.geometry('450x400')

L1 = Label(GUI,text='อะไรเอ่ย..',font=('Angsana New',35),fg='orange')
L1.place(x=170,y=25)
         
def Button1():
    text = 'เพราะ ทำให้สูงไว ไงล่ะ'
    messagebox.showinfo('เฉลยจ้า!',text)

FB1 = LabelFrame(GUI,text='คลิกเพื่อดูเฉลยเล้ยย')
FB1.place(x=60,y=100)
B1 = ttk.Button(FB1,text='ทำไมกินนมแล้วแก่เร็ว',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'น้ำตื้นจ่ะ'
    messagebox.showinfo('เฉลยจ้า!',text)

FB2 = LabelFrame(GUI,text='คลิกเพื่อดูเฉลยเล้ยย')
FB2.place(x=270,y=100)
B2 = ttk.Button(FB2,text='น้ำอะไรเอ่ย ยืนได้ ',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'นกอินทรี'
    messagebox.showinfo('เฉลยจ้า!',text)

FB3 = LabelFrame(GUI,text='คลิกเพื่อดูเฉลยเล้ยย')
FB3.place(x=270,y=250)
B3 = ttk.Button(FB3,text='นกอะไรอยู่ในทะเล',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'แว่นตาไง'
    messagebox.showinfo('เฉลยจ้า!',text)

FB4 = LabelFrame(GUI,text='คลิกเพื่อดูเฉลยเล้ยย')
FB4.place(x=60,y=250)
B4 = ttk.Button(FB4,text='อะไรเอ่ย ต้องถ่างก่อนเสียบ',command=Button4)
B4.pack(ipadx=20,ipady=20)


GUI.mainloop()
