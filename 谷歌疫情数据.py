import requests,re,os,time,datetime
from selenium import webdriver


if not os.path.exists("google全球疫情数据"):    #如果没有这个文件夹
        os.mkdir("google全球疫情数据")          #创建这个文件夹
        os.chdir("google全球疫情数据")          #切换到这个文件夹
else:   
        os.chdir("google全球疫情数据")

browser = webdriver.Chrome()
browser.get('https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen')
time.sleep(5)

js = "var q=document.getElementsByClassName('sOh CrmLxe')[0].scrollTop = 1000"
browser.execute_script(js)
time.sleep(2)
browser.execute_script("window.scrollBy(0,500)")
js1 = "var q=document.getElementsByClassName('sOh CrmLxe')[0].scrollTo(0,0)"
browser.execute_script(js1)
a=browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.dzRe8d.pym81b > div > div.sOh.CrmLxe > table > thead > tr > th.oyBoPe.L8R3fc.Q3JyKe.qCOQbc.NmDtHe')
a.click()
time.sleep(2)
browser.execute_script(js)

name=browser.find_elements_by_css_selector('#yDmH0d > c-wiz > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.dzRe8d.pym81b > div > div.sOh.CrmLxe > table > tbody > tr > th > div > div')
data=browser.find_elements_by_css_selector('#yDmH0d > c-wiz > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.dzRe8d.pym81b > div > div.sOh.CrmLxe > table > tbody > tr > td')
import datetime
t=datetime.datetime.now()
t=str(t).split('.')[0]
#t=browser.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.FVeGwb.ARbOBb > div.BP0hze > div.y3767c > div > div > div.zRzGke.EA71Tc.pym81b > div.mvmWx > span > time')
#t=t.get_attribute('datetime')
#t=t.split('T')[0]
time.sleep(2)

for i in range(int(len(name)/2)):
        j=i*5
        name1=name[2*i+1].text
        confirmed=data[j].text.replace(',','')
        recovered='0'#data[j+3].text.replace(',','')
        deaths=data[j+4].text.replace(',','')
        txt=name1+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
os.chdir(os.pardir)
browser.quit()

time.sleep(2)
def download_data(url):
        response=requests.get(url,headers=headers)
        texts=response.text
        table=re.findall('<tbody class="ppcUXd">(.*?)</tbody>',texts,re.S)
        t=re.findall('datetime="(.*?)">',texts,re.S)
        try:
                t=(''.join(t[0])).replace('T',' ').replace('Z','')
        except:
                t=str(now)
        location=re.findall('<div class="pcAJd">(.*?)</div',table[0],re.S)
        nums=re.findall('<td class="l3HOY.*?>(.*?)</td>',table[0],re.S)
        for i in range(1,len(location)):
            j=i*5
            name=location[i]
            name=''.join(name)
            confirmed=(nums[j]).replace(',','').replace('—','0')
            recovered=nums[j+3].replace(',','').replace('—','0')
            deaths=nums[j+4].replace(',','').replace('—','0')
            if recovered.isdigit()==False:
                    recovered='0'
            if deaths.isdigit()==False:
                    deaths='0'
            '''
            if not os.path.exists(name):
                    os.mkdir(name)     
                    os.chdir(name)
            else:
                    os.chdir(name)
                '''
            txt=name+'.csv'
            f=open(txt,'a',encoding='utf-8')
            f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
            f.close()
            #os.chdir(os.pardir)
        os.chdir(os.pardir)
        
def main():
        if not os.path.exists("google全球疫情数据"):    #如果没有这个文件夹
                os.mkdir("google全球疫情数据")          #创建这个文件夹
                os.chdir("google全球疫情数据")          #切换到这个文件夹
        else:   
                os.chdir("google全球疫情数据")           
        url='https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en'
        href='https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US:en&mid='
        response=requests.get(url,headers=headers)
        texts=response.text
        x=re.findall('data-id="(.*?)".*?<div class="pcAJd">(.*?)</div>',texts,re.S)
        for i in range(1,int(len(x)/2)):
                url=href+x[i][0]
                name=x[i][1]
                if not os.path.exists(name):
                            os.mkdir(name)     
                            os.chdir(name)
                else:
                            os.chdir(name)
                download_data(url)
        os.chdir(os.pardir)
                   
if __name__ == "__main__":
    #while True:
        start=time.time()
        now=datetime.datetime.now()
        headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                } 
        main()
        end=time.time()
        print(now,end-start,'google data写入完成')
    #    time.sleep(7200)



