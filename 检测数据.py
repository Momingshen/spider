import time,datetime,os,requests
import pandas as pd
import numpy as np
from urllib.request import urlretrieve
import matplotlib.pyplot as plt 
def states():
    if not os.path.exists("states daily"):    #如果没有这个文件夹
            os.mkdir("states daily")          #创建这个文件夹
            os.chdir("states daily")          #切换到这个文件夹
    else:   
            os.chdir("states daily") 
    url='https://covidtracking.com/api/v1/states/daily.csv'
    #path=r'C:\Users\admin\Desktop\检测数据\states daily'+now
    path='states daily'+now1
    urlretrieve(url,path)
    datas=pd.read_csv(path)
    index=datas['state']
    a=index.loc[:55]
    b=index.loc[56:60]
    A=np.array(a).tolist()
    B=np.array(b).tolist()
    for i in range(5):
       if B[i] not in A:
           print(B[i])
    # datas=datas.fillna(0)
    data=datas[['date','state','positive','negative','pending','hospitalized','death','totalTestResults','dateChecked','totalTestResultsIncrease','positiveIncrease','deathIncrease','recovered']].astype(str)
    #data=datas.drop('hash',axis=1).astype(str)
    data.to_csv(path,index=False)
    os.chdir(os.pardir)
    print(data.dtypes)
def us():
    if not os.path.exists("us daily"):    #如果没有这个文件夹
            os.mkdir("us daily")          #创建这个文件夹
            os.chdir("us daily")          #切换到这个文件夹
    else:   
            os.chdir("us daily") 
    url='https://covidtracking.com/api/v1/us/daily.csv'
    #path=r'C:\Users\admin\Desktop\检测数据\us daily'+now
    path='us daily'+now1
    urlretrieve(url,path)
    datas=pd.read_csv(path)
    # datas=datas.fillna(0)
    data=datas[['date','positive','negative','pending','hospitalized','death','totalTestResults','dateChecked','totalTestResultsIncrease','positiveIncrease','deathIncrease','recovered']].astype(str)
    #data=datas.drop('hash',axis=1).astype(str)
    data.to_csv(path,index=False)
    os.chdir(os.pardir)
    print(data.dtypes)

def download_source(url, output_path, chunk_size=512):
    response = requests.get(url=url, stream=True)
    with open(output_path, mode='wb') as f:
        for chunk in response.iter_content(chunk_size):
            f.write(chunk)

def al():
    if not os.path.exists("owid-covid-data"):    #如果没有这个文件夹
            os.mkdir("owid-covid-data")          #创建这个文件夹
            os.chdir("owid-covid-data")          #切换到这个文件夹
    else:   
            os.chdir("owid-covid-data") 
    url='https://covid.ourworldindata.org/data/owid-covid-data.xlsx'
    #path=r'C:\Users\admin\Desktop\检测数据\owid-covid-data'+now1
    path='owid-covid-data'+now2
    #response=requests.get(url)
    #f=open(path,'w',encoding='utf-8')
    #f.write(response.text)
    #f.close()
          
    download_source(url, path)
    #urlretrieve(url,path)
    time.sleep(1)
    os.chdir(os.pardir)
    #############巴西检测数据##########################
    if not os.path.exists("cases-brazil-states"):    #如果没有这个文件夹
            os.mkdir("cases-brazil-states")          #创建这个文件夹
            os.chdir("cases-brazil-states")          #切换到这个文件夹
    else:   
            os.chdir("cases-brazil-states") 
    url='https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv'
    #path=r'C:\Users\admin\Desktop\检测数据\cases-brazil-states'+now
    path1='cases-brazil-states'+now1
    #response=requests.get(url)
    #f=open(path1,'w',encoding='utf-8')
    #f.write(response.text)
    #f.close()
    download_source(url, path1)
    #urlretrieve(url,path1)
    os.chdir(os.pardir)


if __name__ == "__main__":
        now=datetime.datetime.now()
	#os.chdir("./检测数据") 
        now1='-'+str(now).split(' ')[0]+'.csv'
        now2='-'+str(now).split(' ')[0]+'.xlsx'
        states()
        us()
        al()
        print('下载完成')
        time.sleep(3)
