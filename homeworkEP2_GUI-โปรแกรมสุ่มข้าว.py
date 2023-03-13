from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import random



GUI = Tk() #จอหลัก
GUI.title('โปรแกรมสุ่มช่วยเลือกข้าว') #ชื่อโปรแกรม
GUI.geometry('300x200') #ขนาด

L1 = Label(GUI,text='วันนี้กินไรดี?',font=('Angsana New',25),fg='dark green')
L1.place(x=90,y=20)

my_list = ["ชาบูปะ", "ส้มตำมะ", "ยำก็ได้", "ซูชิก็ดีนะ", "หมูทะเลอ", "สลัด จบ!"]

##########
def choose_random():
    random_choice = random.choice(my_list)
    messagebox.showinfo("วันนี้จะได้กิน..", f"{random_choice}")

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=100)
B3 = ttk.Button(FB2,text='มาลุ้นกัลเล๊ยย',command=choose_random)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
