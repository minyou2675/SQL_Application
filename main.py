from db import mysql_application
import time

sql = mysql_application()
def main():
    print('='*50)
    print(":(0) 종료:")
    print(":(1) 릴레이션 생성 및 데이터 추가:")
    print(":(2) 제목을 이용한 검색:")
    print(":(3) 관객수를 이용한 검색:")
    print(":(4) 개봉일을 이용한 검색:")
    print('='*50)
    print(":원하는 번호를 입력 하시오:")
    num = int(input())
   

    if num == 0:
        print("프로그램을 종료합니다.")
        time.sleep(2)
        exit()
    elif num == 1:
        sql.insert_data()
        print("메인화면으로 돌아갑니다.")
        time.sleep(2)
        main()
    elif num == 2:
        print("제목을 입력해주세요:")
        str1 = input()
        sql.search_title(str1)
        print("메인화면으로 돌아갑니다.")
        time.sleep(2)
        main()
    elif num == 3 :
        print("총 관객수를 입력해주세요:")
        str1 = input()
        sql.search_total_num(str1)
        print("메인화면으로 돌아갑니다.")
        time.sleep(2)
        main()
    elif num == 4 :
        print("처음날짜와 두번째날짜 사이에 출시한 영화를 검색합니다.")
        print("첫번째 날짜를 입력해주세요(ex:2006-04-01)")
        str1 = input()
        print("두번째 날짜를 입력해주세요(ex:2006-05-01)")
        str2 = input()
        sql.search_date(str1,str2)
        print("메인화면으로 돌아갑니다.")
        time.sleep(2)
        main()
main()  
