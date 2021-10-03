import requests
import re,time,os 
print('欢迎使用豆瓣获取热门电影的影评系统\n')

import os
if os.path.isfile('./cookie.json')==True:  
    f=open('./cookie.json','r')
    txt=f.read()
    cookie=txt
    f.close()
else:
    f=open('./cookie.json','w')
    cookie=input('请输入cookie，即登陆豆瓣的信息：')
    f.write(cookie)
    f.close()

headers={'Cookie': str(cookie),
'Host': 'movie.douban.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'DNT': '1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

url1='https://movie.douban.com/chart'
idlist=requests.get(url1,headers=headers)
ids=re.findall('<a class="nbg" href="(.*?)"  title="(.*?)">',idlist.text,re.S) #获取movie链接
if not os.path.exists('./movie/'):
    os.mkdir('./movie/')
print('获取热门电影的链接和名称为：\n',ids)
import random
for j in ids:
    list1=[]
    print('-------------------正在获取：{}-----------------------'.format(j[1]))
    for i in range(0,200,20): #这里选择爬取10页
        if i==0:  #判断请求是否为首页
            url='{}comments?limit=20&status=P&sort=new_score'.format(j[0])
        else:
            url='{}comments?start={}&limit=20&status=P&sort=new_score'.format(j[0],i)
        time.sleep(0.3+random.random())
        data=requests.get(url,headers=headers)
        texts=data.text
        data1=re.findall('<span class="short">(.*?)</span>',texts,re.S) #获取影评
        list1.append(data1)
    f=open('./movie/{}.txt'.format(j[1]),'w',encoding='utf8')
    for i1 in list1:
        for j1 in i1:
            f.write(j1+'\n')
    f.close()
    print('电影名字：',j[1])
    print('保存影评完成。')
    
time.sleep(60) #等待1分钟后
os.system('cls')   #自动退出软件