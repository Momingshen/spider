import requests
from lxml import etree
response=requests.get('https://tophub.today/n/KqndgxeLl9',headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})
p=etree.HTML(response.text)
item=p.xpath('//*[@id="page"]/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr/td[2]/a')
#items=p.xpath('//*[@id="page"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[2]/a/text()|//*[@id="page"]/div[2]/div[2]/div[2]/div[2]/div/div[1]/table/tbody/tr/td[1]/text()')
with open('微博热搜.txt','w',encoding='utf-8') as f:
    for i in item:
        #href_url=i.xpath('@href')[0]
        name=i.xpath('text()')[0]
        f.write(name+'\n')   
    #for a in items:
    #    f.write(a+'\n')
print('打印完成') 