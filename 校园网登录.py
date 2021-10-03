import requests
import re 
print('欢迎使用校园网登录\n')

import os
if os.path.isfile('./id.json')==True:
    f=open('./id.json','r')
    txt=f.read()
    num1=txt.split(',')[0]
    num2=txt.split(',')[1]
else:
    f=open('./id.json','w')
    num1=input('请输入账号：')
    num2=input('请输入密码：')
    f.write(num1+','+num2)
    f.close()
while(1):    
    try:
        url='http://172.16.30.45/drcom/login?callback=dr1620058048120&DDDDD={}&upass={}&0MKKey=123456&R1=0&R3=1&R6=0&para=00&v6ip=&_=1620058031830'.format(num1,num2)
        data=requests.get(url)
        text=data.text
        NID=re.findall('"NID":"(.*?)"',text)[0]
        break
    except:
        f=open('./id.json','w')
        num1=input('请输入账号：')
        num2=input('请输入密码：')
        f.write(num1+','+num2)
        f.close()

result=re.findall('"result":(.*?)',text)[0]
NID=re.findall('"NID":"(.*?)"',text)[0]
uid=re.findall('"uid":"(.*?)"',text)[0]
olmac=re.findall('"olmac":"(.*?)"',text)[0]

etime=re.findall('"etime":"(.*?)"',text)[0]
ip=re.findall('"v46ip":"(.*?)"',text)[0]
olip=ip
last_time=re.findall('"stime":"(.*?)"',text)[0]
    
import os,time
print('登录成功')
print('姓名：',NID)
print('学号：',uid)
print('上次登陆的ip是：',ip)
print('本次登陆的ip是：',olip)
print('上次登陆的时间是：',last_time)
print('当前的时间是：',etime)
print('当前的MAC地址是：',olmac)
time.sleep(60)



