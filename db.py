import pymysql.cursors
import csv
import os

#mysql 연결
class mysql_application():

    def __init__(self):
        
        try:
            self.conn = pymysql.connect(
            host='54.180.1.233',
            port = 3306,
            user='kym2675',
            password='dbals3319',
            db='moviedb',
            charset='utf8')
            print("DB CONNECTED")
        except :
            print("failed")

        self.curs=self.conn.cursor()
    
        sql = """create table movie (
            id           char(3), 
            title        varchar (100), 
            company      varchar (50),
            releasedate  date,
            country      varchar (10),  
            totalscreen  int,
            profit       numeric (15,2),
            totalnum     int,
            grade        varchar (50),
            primary key (id));
    """
        try:
            print("테이블이 없습니다. 새로 생성합니다.")
            self.curs.execute(sql)
            self.conn.commit
        except:
            print("테이블이 존재합니다. 기존 테이블을 사용합니다.")
            self.conn.commit()
        
    def insert_data(self):
        pwd = os.getcwd()
        sql = """INSERT INTO movie values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        with open(pwd+"/movie_data.TXT",'r',encoding='cp949') as f:
            read_data = f.readlines()

        for data in read_data:
            data = data.split('|')
            data = data[1:]
            data[-1] = data[-1].replace('\n','')
            data[5] = data[5]
            data[7] = data[7]
            self.curs.execute(sql,(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
        self.conn.commit()
        return 
          
    def search_title(self,str):
      
        sql = "select * from movie where title like %s"
        try:
            self.curs.execute(sql,'%'+str+'%')
            for f in self.curs.fetchall():
                print(f)
        except:
            print("검색 결과가 없습니다.")
        
    def search_total_num(self,total_num):
        sql = """select * from movie where totalnum > %s"""
        try:
            self.curs.execute(sql,total_num)
            for f in self.curs.fetchall():
                print(f)
        except:
            print("검색 결과가 없습니다.")

    def search_date(self,start_date,end_date):
        sql="""select * from movie where between %s and %s"""
        try:
            self.curs.execute(sql,start_date,end_date)
            for f in self.curs.fetchall():
                print(f)
        except:
            print("검색 결과가 없습니다.")
        
    
    def end_application(self):
        print("종료합니다")
        self.conn.close()
        return 0
    




