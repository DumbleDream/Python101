import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมช่วยสุ่มเลือกข้าว')
GUI.geometry('500x400')

L1 = Label(GUI,text='วันนี้กินไรดี?',font=('Angsana New',35),fg='dark green')
L1.place(x=30,y=30)


my_list = ["ชาบูปะ", "ส้มตำมะ", "ยำก็ได้", "ซูชิก็ดีนะ", "หมูทะเลย", "สลัด จบ!"]

def choose_random():
    random_choice = random.choice(my_list)
    result_label.config(text=random_choice)

root = tk.Tk()
root.title("Random Choice Selector")

choose_button = tk.Button(root, text="Choose", command=choose_random)
choose_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
