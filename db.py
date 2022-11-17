import pymysql.cursors
import csv

#mysql 연결
class mysql_application():

    def init(self):
        self.conn = pymysql.connect(
            host='ec2-54-180-1-233.ap-northeast-2.compute.amazonaws.com:3306',
            user='kym2675',
            password='dbals3319',
            db='moviedb',
            charset='utf8')

        self.curs=self.conn.cursor()
        self.sql = """create table movie (
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
    def insert_data(self):
        sql = """INSERT INTO moive values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        f=open('movie_data.txt','r',encoding='utf-8')
        while True:
            rd=f.readlines.split('|')
            if not rd:
                break
        f.close()
        for line in rd:
            self.curs.execute(sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]))
        self.conn.commit()
        self.conn.close()

    def search_title(self,str):
        sql = """select * from moive where title = %s """
        self.curs.excute(sql,str)
        self.conn.commit()
        self.conn.close()
        
    def search_total_num(self,total_num):
        sql = """select * from movie where totalnum > %s"""
        self.curs.excute(sql,total_num)
        self.conn.commit()
        self.conn.close()

    def search_date(self,start_date,end_date):
        sql="""select * from movie where between %s and %s"""
        self.curs.excute(sql,start_date,end_date)
        self.conn.commit()
        self.conn.close()

    




