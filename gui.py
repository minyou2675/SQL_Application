from tkinter import *
from db import mysql_application

# str1,str2 = map(str,input().split())
def on_change_title(event):
        print_records = " "
        idx = 0
        records = sql.search_title(event.widget.get())
        for rec in records:
                print_records += str(rec) + '\n'
                rec_label = Label(tk,text=rec)
                rec_label.grid(row=4+idx,column=0,columnspan=10)
                idx += 1
def on_change_total_num(event):
        print_records = ""
        idx = 0
        records = sql.search_total_num(event.widget.get())
        for rec in records:
                print_records += str(rec) + '\n'
                rec_label = Label(tk,text=rec)
                rec_label.grid(row=4+idx,column=0,columnspan=2)
                idx += 1
def on_change_date(event):
        print_records = ""
        records = sql.search_date(event.widget.get())
        for rec in records:
                print_records += str(rec) + '\n'
                rec_label = Label(tk,text=rec)
                rec_label.grid(row=4,column=0,columnspan=2)

def search_title_screen():
        tk2 = Tk()
        label = Label(tk2,text="제목을 입력하세요")
        label.grid(row=0,column=0)
        entity = Entry(tk2,width=30)
        entity.grid(row=1,column=0)
        # entity.pack()
        entity.bind("<Return>",on_change_title)
        # records = sql.search_title(entity.get())
        # print_records = ""
        # for rec in records:
        #         print_records += str(rec) + '\n'
        # rec_label = Label(tk,text=rec)
        # rec_label.grid(row=4,column=0,columnspan=2)
        tk2.mainloop()
def search_total_num_screen():
        tk = Tk()
        label = Label(tk,text="관객수를 입력하세요")
        label.grid(row=0,column=0)
        entity = Entry(tk,width=30)
        entity.grid(row=1,column=0)
        entity.bind("<Return>",on_change_total_num)
        
        tk.mainloop()
        
def search_date_screen():        
        tk = Tk()
        label = Label(tk,text="제목을 입력하세요")
        label.grid(row=0,column=0)
        entity1 = Entry(tk,width=30)
        entity1.grid(row=1,column=0)
        entity2 = Entry(tk, width=30)
        entity2.grid(row=1,columns=1)
        # entity.bind("<Return>",on_change_total_num)
      
sql = mysql_application()
tk = Tk()

button0 = Button(tk,text='(0) 종료',bg='green',font=15,width=30,height=5,command= sql.end_application).grid(row=0, column=0,pady=5)

button1 = Button(tk,text='(1) 릴레이션 생성 및 데이터 추가',bg='red',font=15,width=30,height=5,command= sql.insert_data).grid(row=2, column=0,pady=5)

button2 = Button(tk,text='(2) 제목을 이용한 검색',bg='blue',font=15,width=30,height=5,command=lambda : search_title_screen()).grid(row=4, column=0,pady=5)

button3 = Button(tk,text='(3) 관객수를 이용한 검색',bg='white',font=15,width=30,height=5,command=lambda : search_total_num_screen()).grid(row=6, column=0,pady=5)

button4 = Button(tk,text='(4) 개봉일을 이용한 검색',bg='pink',font=15,width=30,height=5,command=lambda : search_date_screen()).grid(row=8, column=0,pady=5)

tk.mainloop()
        