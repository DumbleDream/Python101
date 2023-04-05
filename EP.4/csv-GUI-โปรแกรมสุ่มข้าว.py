from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
import random

######CSV######
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf=8',newline='') as file:
        fw = csv.writer(file) #fw = file wrtier
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf=8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
######CSV######



GUI = Tk() #จอหลัก
GUI.title('โปรแกรมสุ่มช่วยเลือกข้าว') #ชื่อโปรแกรม
GUI.geometry('800x400') #ขนาด

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

##########SECTION RIGHT##########
LF1 = ttk.LabelFrame(GUI,text='กรอกเมนูอาหารที่เพิ่งทานไป')
LF1.place(x=400,y=50)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def Savedata():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get()  #ดึงข้อมูลจากตัวแปร v_data มาใช้
    text = [t,data] #เวลา,ข้อมูลที่กรอก
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=Savedata)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()
