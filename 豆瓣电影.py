import requests
import os,time,re
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

def get_movies():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
               'Host':'movie.douban.com'}
    movie_list = []
    daoyan_list = []
    pic_list = []
    country_list= []
    language_list= []
    for i in range(0,10):
        print('第'+str(i+1)+'页传输完毕')
        link = 'https://movie.douban.com/top250?start=' + str(i*25)
        r = requests.get(link, headers = headers, timeout = 20)
        time.sleep(1)                                   
        soup = BeautifulSoup(r.text, 'lxml')
        name_list = soup.find_all('div', class_ = 'hd')
        for each in name_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
            
            movie_link = each.a['href']
            r1 = requests.get(movie_link, headers = headers, timeout = 20)
            time.sleep(1)
            soup1 = BeautifulSoup(r1.text, 'lxml')
            name_list = soup1.find_all('div', id='info')                                    
            lan=re.findall('<span class="pl">语言:</span> (.*?)<br/>',str(name_list),re.S)    
            country=re.findall('<span class="pl">制片国家/地区:</span> (.*?)<br/>',str(name_list),re.S)   
            try:
                language_list.append(lan[0])
                country_list.append(country[0])
            except:
                language_list.append(lan)
                country_list.append(country[0])
            
        pics = soup.find_all('div', class_ = 'pic')   
        for pic in pics:
            url = pic.a.img['src']
            pic_list.append(url)
        
        daoyans = soup.find_all('div', class_ = 'bd')   
        for each in daoyans[1:]:
            daoyan = each.p.text.strip().split(' ')[1]
            daoyan.append(daoyan)
            
    return movie_list,daoyan_list,pic_list,country_list,language_list

movie_list,daoyan_list,pic_list,country_list,language_list = get_movies()

df=pd.DataFrame([movie_list,daoyan_list,pic_list,country_list,language_list]).T
df.columns=['片名','导演','封面图片链接','制片国家_地区','语言']
df.to_csv('result.csv',index=0)

conn = sqlite3.connect('./douban_movies_250.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE "movie" (
    "主键" INTEGER,
    "电影名" TEXT,
    "导演" TEXT,
    "图片" TEXT,
    "地区" TEXT,
    "语言" TEXT,
    PRIMARY KEY("主键")
)''')

path = 'result.csv'
df = pd.read_csv(path)
names = df.values.tolist()

for name in names:
    cursor.execute('INSERT INTO movie (电影名,导演,图片,地区,语言) VALUES (?,?,?,?,?)',(name))
    print('將',name,'寫入數據庫')

conn.commit()
cursor.close()
conn.close()
