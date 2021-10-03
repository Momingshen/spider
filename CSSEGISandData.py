import datetime,os,time
import pandas as pd
import numpy as np
from urllib.request import urlretrieve
def paqucsv():
    if not os.path.exists("csse_covid_19_daily_reports"):    #如果没有这个文件夹
            os.mkdir("csse_covid_19_daily_reports")          #创建这个文件夹
            os.chdir("csse_covid_19_daily_reports")          #切换到这个文件夹
    else:   
            os.chdir("csse_covid_19_daily_reports")
    #begin = datetime.date(2020,8,3)
    #end = datetime.date(2020,8,6)

    delta = datetime.timedelta(days=1)
    begin=datetime.datetime.now()
    end = begin
    begin = begin-delta-delta
    x=[]
    while begin < end:
        x.append(begin.strftime("%m-%d-%Y"))
        begin += delta
    for i in range(len(x)):
        url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv'.format(x[i])
        path=x[i]+'.csv'
        try:
            urlretrieve(url,path)
        except:
            time.sleep(60)
            urlretrieve(url,path)
        time.sleep(1)


def chulicsv():
    if not os.path.exists("csse_covid_19_daily_reports(1)"):    #如果没有这个文件夹
            os.mkdir("csse_covid_19_daily_reports(1)")          #创建这个文件夹
    Folder_Path=r'./csse_covid_19_daily_reports'
    file_list = os.listdir(r'./csse_covid_19_daily_reports')
    for j in range(len(file_list)-1):
        datas= pd.read_csv(Folder_Path + '\\' + file_list[j])
        a=datas.shape[0]
        try:
            x=datas['Country/Region']
        except:
            x=datas['Country_Region']
        list1=np.array(x).tolist()
        for i in range(a-1):
            d=datas.iloc[i:i+1]
            path1=r'./csse_covid_19_daily_reports\csse_covid_19_daily_reports(1)'+'\\'+str(list1[i]).replace('*','')+'.csv'
            d.to_csv(path1,mode='a',index=False,header=False)
        print('清洗完',file_list[j])
if __name__ == "__main__":
    paqucsv() 
    #chulicsv()