import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

class procuder(threading.Thread):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kw):
        super(procuder,self).__init__(*args,**kw)
        self.page_queue=page_queue
        self.img_queue=img_queue
    def run(self):
        while True: 
            if self.page_queue.empty():
                break
            url=self.page_queue.get()
            self.parse_page(url)
    def parse_page(self,url):
        response=requests.get(url,headers=self.headers)
        text=response.text
        html=etree.HTML(text)
        imgs=html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            img_url=img.get("data-original")
            alt=img.get("alt")
            alt=re.sub(r'[\?？。,.，!！*]','',alt)
            suffix=os.path.splitext(img_url)[1]
            filemane=alt+suffix
            self.img_queue.put((img_url,filemane))
            
class consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kw):
        super(consumer,self).__init__(*args,**kw)
        self.page_queue=page_queue
        self.img_queue=img_queue
    def run(self):
        while True:
            if self.img_queue.empty()and self.page_queue.empty():
                break 
            img_url,filemane=self.img_queue.get()
            request.urlretrieve(img_url,'threading/a/'+filemane)
            print(filemane+'下载完成!')
def main():
    page_queue=Queue(100)
    img_queue=Queue(1000)
    for x in range(1,101):
        url='http://www.doutula.com/photo/list/?page=%d'%x
        page_queue.put(url)
    for x in range(5):
        t=procuder(page_queue,img_queue)
        t.start()
    for x in range(5):
        t=consumer(page_queue,img_queue)
        t.start()



if __name__ == "__main__":
    main()
