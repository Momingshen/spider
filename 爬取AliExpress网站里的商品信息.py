#-*-coding:utf-8-*- #编码声明
import requests,os,time,re,csv,threading  #调用第三方模块请求模块、文件处理模块、时间模块、正则、csv格式储存、多线程
from lxml import etree   #这里使用lxml，也就是xpath的方法
from urllib.request import urlretrieve #保存下载网页模块
def dowmload():
                
                try:
                        response1=requests.get(href_url1,headers=headers)       #请求网页
                except:                                                         #有错误跳过报错
                        print('报错，直接跳过...')      
                        
                response1=response1.text
                
                pattern=re.compile('"productDetailUrl":"(.*?)"',re.S)            #用正则找到目标
                items=re.findall(pattern,response1)                             
                for item in items:                                              #循环出列表的内容
                        
                        item='https:'+item
                        print(item)
                        time.sleep(1)
                        try:
                            response2=requests.get(item,headers=headers)
                            response2=response2.text
                        except:
                            print('报错，直接跳过...')
                        
                        
                        pattern1=re.compile('"itemWishedCount":(.*?),.*?"formatedActivityPrice":"(.*?)".*?"averageStar":"(.*?)".*?"totalValidNum":(.*?),.*?"formatTradeCount":"(.*?)".*?"subject":"(.*?)"',re.S)
                        items1=re.findall(pattern1,response2)
                        for x in items1:
                                #print(x[1],x[5],x[0],x[3],x[4],x[2])
                                if x==0 or x==1:                        #这里会出现空内容，就判断跳过
                                        a=x
                                else:
                                        a=x[5]
                                        a=re.sub(r'[\?\\？。,.，!！/*]','',a)
                                        try:
                                                urlretrieve(item,(str(a)+'.html'))              #这里保存下载网页
                                        except:
                                                print('报错，直接跳过...')
                                                continue
                                        with open('data.csv', 'a',encoding='utf-8') as csvfile:        #下载商品内容到data.csv
                                                writer = csv.writer(csvfile)
                                                writer.writerow([x[1],x[5],x[0],x[3],x[4],x[2]])
                        
                        #break
                

if not os.path.exists("aliexpress"):    #如果没有这个文件夹
        os.mkdir("aliexpress")          #创建这个文件夹
        os.chdir("aliexpress")          #切换到这个文件夹
else:   
        os.chdir("aliexpress")       
headers={
        'cookie':'ali_apache_id=11.180.122.34.1582367654815.212810.0; cna=qvHXFuyx1RECAXjvcV/JDt9t; _m_h5_tk=3dc0729e9a641ceb877f02df8fdcfde8_1582377022766; _m_h5_tk_enc=7870c91cb07e554e846d7391b03cbd77; _ga=GA1.2.1107086217.1582367665; _gid=GA1.2.1278933622.1582367665; aep_common_f=Cre3Dbon0nc9AoyS1+wFH3e+lbuVSDd1PJPvR8ng5xdvzXxXucuVlw==; _bl_uid=avkIh645xnhgpgxttwm4aLkqk4zF; _fbp=fb.1.1582367853055.1780169290; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932856973252%094000590954581%0932856973252%094000481329602%094000179867421; acs_usuc_t=x_csrf=ccb5xqx1eu3h&acs_rt=d3b28ed019c5-45e3-a718-29ce1c56a0a2; intl_locale=en_US; havana_tgc=eyJjcmVhdGVUaW1lIjoxNTgyMzcwNjE4OTM1LCJsYW5nIjoiZW5fVVMiLCJwYXRpYWxUZ2MiOnsiYWNjSW5mb3MiOnsiMTMiOnsiYWNjZXNzVHlwZSI6MSwibWVtYmVySWQiOjIyMDc0MjIzMjQ4MDksInRndElkIjoiMW9sdktwRGt4SGpNT2wxM01VdWxRYUEifX19fQ; _hvn_login=13; xman_us_t=x_lid=cn263520100ypsae&sign=y&x_user=2CmMIpPu77K+qV4sv7I7JP2faHOzOAuWYkutbP3etQ8=&ctoken=14wmkw16q3a0w&need_popup=y&l_source=aliexpress; aep_usuc_t=ber_l=A0; xman_f=bkxZDpT839Ra5Ms4wJJnEVWfqnQEPAg8jLQWlh3nroHVdVbCIzcjzI0OY0u34Rhr6hPXm+h2xtmY6j19fjVIrYNXEPGOyPMdY0elM9csf01DRAS0b+luHePvUoCAnqFwYFfRdiiLSHlStMiw+jyTt+GopJ2bdaEDiRv8E/pRW96WXzv1KvzX87wW6qgcQLyu0rMnX6ZiPx2pxa3mbQFrMqA74wPIpFFZ1dXVIyEj1UpnZP2h/eGBLfvDHFZB5fjGMQT1QhOOEI9w5Gqtj5h+NJX/Dx2VxP0tXxvRGebeTWh8cH8D7Ts8HxoC3WabnIOSZVriHw+x0i/dyYWO3WIuSZZVf9FtYHCtHVB94iQC6d9PeeJBhoTFFMRsZgDd4bfxr8UzH2AsV8WGDDUdxtk+t3H0AFAKO1Urq+C4oJg+EJMcOyGfk7HNWA==; x5sec=7b2261652d676c6f7365617263682d7765623b32223a226437393732323832626264343466633934363061333463333634376330393830434d796678504946454f43703566544c6b4c767971774561444445344e6a51314e6a45344d6a6b374d673d3d222c2261652d676c6f64657461696c2d7765623b32223a226235383438326431393034653037653536333862376134363865343164323132434f6d5578504946454e62712f3747566839765758686f4d4d5467324e4455324d5467794f547378227d; aep_usuc_f=site=glo&c_tp=USD&x_alimid=1864561829&isb=y&region=CN&b_locale=en_US; intl_common_forever=/lA73/XjajMZyItbLM0XKzimU5IWFPmgQsKD4nFIdrgh90pkVWgJ0g==; JSESSIONID=DABD7EDEDF5C26CC813D60B1872C7B76; ali_apache_track=mt=1|ms=|mid=cn263520100ypsae; ali_apache_tracktmp=W_signed=Y; _gat=1; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_c_chg=0&x_user=CN|CN|shopper|ifm|1864561829&zero_order=y&acs_rt=cfc984e2044f485ea88d2a9e9643cc52&last_popup_time=1582367685583&x_as_i=%7B%22cookieCacheEffectTime%22%3A1582370895546%2C%22isCookieCache%22%3A%22Y%22%2C%22ms%22%3A%220%22%7D; xman_t=dYZ/QhdqVI68Kjy4ERcgNkM/dQidLpCkIQIbXlRmLNA4R5A4xZ0shAUUkepik7Zj8Kz3HsZgu5qznKMOcaCXsWWTq+/0PkCbAEnvnuhcvP/yFViLChoTqbQlCfm9IUF4XqiFwnkAhcAxL2ey5BfZy8ywQFOSamE7pOgSB0NFlF8ioDCUmzGTdfDRkXqdEFd+hY9qh/WIJUiHnTJUz66pobfRtCvX1T9lhw+C1WQL4os6Bk7nbPqdLBzc/8nY9TQzqtMUGjvGT7kwtf3GUwUbFSJ41LRlHl7VnOtRD5GZnQ5oiycW4m6N1NGwwrQKIPnZaQo4ah7t1mydRT2NdChK9jvGuiv2rBxB0HteeBtdMm0klUBIaF8yGns+9MmMGCVtlQ40IlRrLYpTQ9mdFJarJErXuehRr3/rmXUiyLQALvEw4WT0qluPhFrZpez7+6lK514loLJO5EnJe3Ss8SgqEhV4U4j09Le7xN7tU2N/SJpwPSDkIfF5Roe8FotbzK7kaX6PlgUO9asM8HmDD5CNA21L/7hNWtfAfO1w7IBqIHFKkARipICQ8mE6P1ftk+d9cAFWujOJcdnTqFsWHSTlgXahlQAR3llch2TVxf+muG150LG7cka9KWTOs6lAVFd8f/39gVBEN2T2zjw2NwZf+g==; l=dBIBeub7QszDMCDDBOCNlm-eQ5bTKIRf_ul2TIIei_5d1186z_WOo-wU0eJ6cjWAMTLB4WtSLw2t1eCTJXziOZmlVXHyTxDDB; isg=BDg4UIjAksqhGv5OITU1glevCebKoZwrzq2NM3Kpz3Mmjdl3GrGauyBnRYU92lQD',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
url='https://www.aliexpress.com/all-wholesale-products.html?spm=a2g0o.home.16005.1.3ddf2c25FZwjMV'
response=requests.get(url,headers=headers)      #请求网页
html=etree.HTML(response.text)                  #解析网页
a_list=html.xpath('//*[@id="category"]/div[3]/div/div[1]/div/div/div/ul/li/a')     #寻找a节点下的内容  
for a in a_list:
        href_url='https:'+a.xpath('@href')[0]   #找到网址
        title=a.xpath("text()")[0]                     #找到文本
        title=re.sub(r'[\?？。,.，!！/*]','',title)   #替换掉字符
        if not os.path.exists(title):
                os.mkdir(title)     
                os.chdir(title)
        else:
                os.chdir(title)
        for x in range(1,11):                   #循环商品10页
            href_url1=href_url+'?page=%d'%x             #第几页网址
            th = threading.Thread(target = dowmload)    #用多线程运行
            th.start()                                  #开始
            time.sleep(0.2)            
        th.join()                                       #等待多线程运行完
        time.sleep(0.2)
        os.chdir(os.pardir)                             #切换到上一目录
        time.sleep(0.2)
