from tkinter import *
from db import mysql_application


sql = mysql_application()
# str1,str2 = map(str,input().split())

def search_title_screen():
        tk2 = Tk()
        label = Label(tk2,text="제목을 입력 하시오")
        label.pack()
        entry = Entry(tk2,width=30)
        str1 = entry.get()
        entry.delete(0,"end")
        entry.bind("<Return>",sql.search_title(str1))
        entry.pack()
        tk2.mainloop()
        
def search_total_num_screen():
        tk2 = Tk()
        label = Label(tk2,text="관객수를 입력 하시오")
        label.pack()
        entry = Entry(tk2,width=30)
        str1 = entry.get()
        entry.delete(0,"end")
        entry.bind("<Return>",sql.search_total_num(str1))
        entry.pack()
        tk2.mainloop()
        
        
def search_date_screen():
        tk2 = Tk()
        label = Label(tk2,text="날짜를 입력 하시오")
        label.pack()
        entry = Entry(tk2,width=30)
        str1 = entry.get()
        entry2 = Entry(tk2,width=30)
        str2 = entry2.get()
        entry.delete(0,"end")
        entry2.delete(0,"end")
        entry.bind("<Return>",sql.search_date(str1,str2))
        entry.pack()
        tk2.mainloop()



tk = Tk()

button0 = Button(tk,text='(0) 종료',bg='green',font=15,width=30,height=5,command= sql.end_application).grid(row=0, column=0)

button1 = Button(tk,text='(1) 릴레이션 생성 및 데이터 추가',bg='red',font=15,width=30,height=5,command= sql.insert_data).grid(row=1, column=0)

button2 = Button(tk,text='(2) 제목을 이용한 검색',bg='blue',font=15,width=30,height=5,command= search_title_screen).grid(row=2, column=0)

button3 = Button(tk,text='(3) 관객수를 이용한 검색',bg='white',font=15,width=30,height=5,command= search_total_num_screen).grid(row=3, column=0)

button4 = Button(tk,text='(4) 개봉일을 이용한 검색',bg='pink',font=15,width=30,height=5,command= search_date_screen).grid(row=4, column=0)

tk.mainloop()