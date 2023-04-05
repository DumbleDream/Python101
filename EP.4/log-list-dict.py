Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======
Traceback (most recent call last):
  File "C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py", line 14, in <module>
    adddata('เวย์โปรตีน 3000 บาท')
  File "C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py", line 10, in adddata
    file.writeline(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'. Did you mean: 'writelines'?

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======
Traceback (most recent call last):
  File "C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py", line 14, in <module>
    adddata('เวย์โปรตีน 3000 บาท')
  File "C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py", line 10, in adddata
    file.writelineห(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writelineห'. Did you mean: 'writelines'?

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======
['ไข่กะทะ 30 บาทอกไก่ 300 บาทเวย์โปรตีน 3000 บาทps5 20 บาท\n', 'ps5 20000 บาท\n', 'มะยงชิด\n', 'ลำไย\n', 'ลิ้นจี้\n']

======= RESTART: C:\Users\apinp\OneDrive\เดสก์ท็อป\python101\writefile.py ======
ไข่กะทะ 30 บาทอกไก่ 300 บาทเวย์โปรตีน 3000 บาทps5 20 บาท
ps5 20000 บาท
มะยงชิด
ลำไย
ลิ้นจี้

>>> box = []
>>> box.append('ปากกา')
>>> box.append('ดินสอ')
>>> box.append('ยางลบ')
>>> print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
>>> print(box[1])
ดินสอ
>>> print(box[2])
ยางลบ
>>> print(box[-1])
ยางลบ
>>> print(box[-2])
ดินสอ
>>> print(box[-3])
ปากกา
>>> print(box[-4])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(box[-4])
IndexError: list index out of range
>>> brand = {'pen' : [ 'Lamy','Pentel','Feber-castel'], 'pencil':['hourse','straedtler'],'eraser':['ยางลบ2สี']}
>>> brand = {'pen' : [ 'Lamy','Pentel','Feber-castel'], 'pencil':['hourse','straedtler'],'eraser':'ยางลบ2สี'}
>>> print(brand['pen'])
['Lamy', 'Pentel', 'Feber-castel']
>>> print(brand['pen'][1])
Pentel
>>> print(brand['pencil'][0])
hourse
>>> print(brand['eraser'][0])
ย
>>> print(brand['eraser'])
ยางลบ2สี
