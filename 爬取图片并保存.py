import requests
import lxml
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
headers={
    'dnt': '1',
'if-none-match': 'cacheable:2e61345a2e1d9ba6dd4c092b57be4990',
'referer': 'https://www.bluefly.com/',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
response=requests.get('https://www.autohome.com.cn/news/',headers=headers)
response.encoding=response.apparent_encoding

soup=BeautifulSoup(response.text,features='lxml')
target=soup.find(id="auto-channel-lazyload-article")
targets=target.find('ul')
li_list=targets.find_all('li')
for i in li_list:
    a=i.find('img')
    if a:
        s='http:'+a.attrs.get('src')
        print(s)
        img=requests.get(s)
        name = s.split("/")[-1]
        urlretrieve(s,name)
