import requests
from lxml import etree
response=requests.get('https://www.zhihu.com/billboard',headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})
p=etree.HTML(response.text)
item=p.xpath('//*[@id="root"]/div/main/div/a/div[2]/div[1]/text()')
with open('知乎热搜.txt','w',encoding='utf-8') as f:
    for i in item:
        f.write(i+'\n')
print('打印完成')  