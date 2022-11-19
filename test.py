with open("./movie_data.TXT",'r',encoding='cp949') as f:
            read_data = f.readlines()

for data in read_data:
        data = data.split('|')
        data = data[1:]
        data[-1] = data[-1].replace('\n','')
        print(data)