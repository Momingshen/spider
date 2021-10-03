import requests
import lxml
from bs4 import BeautifulSoup
response=requests.get('https://www.autohome.com.cn/news/')
response.encoding=response.apparent_encoding

soup=BeautifulSoup(response.text,features='lxml')
target=soup.find(id="snize-search-results-content clearfix")
li_list=target.find_all('li')
for i in li_list:
    a=i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt=a.find('h3').text
        print(txt)
        img_url=a.find('img').attrs.get('src')
        print(img_url)
        with open('汽车新闻.txt','a',encoding='utf-8') as f:
            f.write(txt)