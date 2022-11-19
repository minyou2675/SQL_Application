from db import mysql_application
sql = mysql_application()
def main():
    print('='*20)
    print("(0) 종료")
    print("(1) 릴레이션 생성 및 데이터 추가")
    print("(2) 제목을 이용한 검색")
    print("(3) 관객수를 이용한 검색")
    print("(4) 개봉일을 이용한 검색")
    print('='*20)
    print("원하는 번호를 입력 하시오")
    num = int(input())
   

    if num == 0:
        print("끝")
    elif num == 1:
        sql.insert_data()
        main()
    elif num == 2:
        print("사용자 입력:")
        str1 = input()
        sql.search_title(str1)
        main()
    elif num == 3 :
        print("사용자 입력:")
        str1 = input()
        sql.search_total_num(str1)
        main()
    elif num == 4 :
        print("사용자 입력:")
        str1,str2 = map(str,input().split())
        sql.search_date(str1,str2)
        main()
main()  
