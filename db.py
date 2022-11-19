import pymysql.cursors
import csv

#mysql 연결
class mysql_application():

    def __init__(self):
        self.conn = pymysql.connect(
            host='54.180.1.233',
            port = 3306,
            user='kym2675',
            password='dbals3319',
            db='moviedb',
            charset='utf8')
        if(self.conn):
            print("DB CONNECTED")
            
        # sql2 = """drop table movie"""
        self.curs=self.conn.cursor()
        # self.curs.execute(sql2)
    
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
        # self.curs.execute(sql)
        self.conn.commit()
        
    def insert_data(self):
        sql = """INSERT INTO movie values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        with open("./movie_data.TXT",'r',encoding='cp949') as f:
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
        self.curs.execute(sql,'%'+str+'%')
        for f in self.curs.fetchone():
            print(f)
        
    def search_total_num(self,total_num):
        sql = """select * from movie where totalnum > %s"""
        self.curs.execute(sql,total_num)
        for f in self.curs.fetchall():
            for r in f:
                print(r)

    def search_date(self,start_date,end_date):
        sql="""select * from movie where between %s and %s"""
        self.curs.execute(sql,start_date,end_date)
        for f in self.curs.fetchone():
            print(f)
        
    
    def end_application(self):
        print("종료합니다")
        self.conn.close()
        return 0
    




