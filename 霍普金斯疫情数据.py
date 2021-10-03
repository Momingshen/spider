import os,time,re,requests,datetime
def US():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27US%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Deaths%20desc&outSR=102100&resultOffset=0&resultRecordCount=55&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("US"):    #如果没有这个文件夹
            os.mkdir("US")          #创建这个文件夹
            os.chdir("US")          #切换到这个文件夹
    else:   
            os.chdir("US")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)

def Brazil():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27Brazil%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("Brazil"):    #如果没有这个文件夹
            os.mkdir("Brazil")          #创建这个文件夹
            os.chdir("Brazil")          #切换到这个文件夹
    else:   
            os.chdir("Brazil")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)

def Germany():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27Germany%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("Germany"):    #如果没有这个文件夹
            os.mkdir("Germany")          #创建这个文件夹
            os.chdir("Germany")          #切换到这个文件夹
    else:   
            os.chdir("Germany")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)
    
def France():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27France%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("France"):    #如果没有这个文件夹
            os.mkdir("France")          #创建这个文件夹
            os.chdir("France")          #切换到这个文件夹
    else:   
            os.chdir("France")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)
    
def UK():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27United%20Kingdom%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("United Kingdom"):    #如果没有这个文件夹
            os.mkdir("United Kingdom")          #创建这个文件夹
            os.chdir("United Kingdom")          #切换到这个文件夹
    else:   
            os.chdir("United Kingdom")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)
    
def spain():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27Spain%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("Spain"):    #如果没有这个文件夹
            os.mkdir("Spain")          #创建这个文件夹
            os.chdir("Spain")          #切换到这个文件夹
    else:   
            os.chdir("Spain")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)

def ltaly():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    response = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/3/query?f=json&where=Country_Region%3D%27Italy%27&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20desc&outSR=102100&resultOffset=0&resultRecordCount=75&resultType=standard&cacheHint=true', headers=headers)
    texts=response.text
    data=re.findall('"Province_State":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    t=re.findall('"Last_Update":(.*?),',texts,re.S)[0]
    timeTemp = float(int(t)/1000)
    tupTime = time.localtime(timeTemp)
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    if not os.path.exists("Italy"):    #如果没有这个文件夹
            os.mkdir("Italy")          #创建这个文件夹
            os.chdir("Italy")          #切换到这个文件夹
    else:   
            os.chdir("Italy")
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
    os.chdir(os.pardir)

def country():
    headers = {
        'authority': 'services9.arcgis.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'dnt': '1',
        'accept': '*/*',
        'origin': 'https://www.arcgis.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    url='https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/2/query?f=json&where=Recovered%3C%3E0&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Recovered%20desc&resultOffset=0&resultRecordCount=250&resultType=standard&cacheHint=true'
    response = requests.get(url, headers=headers)
    texts=response.text
    data=re.findall('"Country_Region":"(.*?)".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),',texts,re.S)
    #t=re.findall('"Last_Update":(.*?),',texts,re.S)
    #timeTemp = float(int(t)/1000)
    tupTime = time.localtime()
    t= time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
    
    url1='https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/FeatureServer/2/query?f=json&where=Deaths%3E0&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Deaths%20desc&outSR=102100&resultOffset=0&resultRecordCount=200&resultType=standard&cacheHint=true'
    response1 = requests.get(url1,headers=headers)
    texts1=response1.text
    data1=re.findall('"Country_Region":"Sweden".*?"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),''',texts1,re.S)
    name='Sweden'
    confirmed=data1[0][0]
    recovered=data1[0][2]
    deaths=data1[0][1]
    if recovered=='null':
        recovered=''
    if not os.path.exists(name):    #如果没有这个文件夹
            os.mkdir(name)          #创建这个文件夹
            os.chdir(name)          #切换到这个文件夹
    else:   
            os.chdir(name)
    txt=name+'.csv'
    f=open(txt,'a',encoding='utf-8')
    f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
    f.close()
    os.chdir(os.pardir)
    
    for i in range(int(len(data))):
        name=data[i][0]
        confirmed=data[i][1]
        recovered=data[i][3]
        deaths=data[i][2]
        if recovered=='null':
            recovered=''
        name=name.replace('*','')
        if not os.path.exists(name):    #如果没有这个文件夹
                os.mkdir(name)          #创建这个文件夹
                os.chdir(name)          #切换到这个文件夹
        else:   
                os.chdir(name)
        txt=name+'.csv'
        f=open(txt,'a',encoding='utf-8')
        f.write(t+','+confirmed+','+recovered+','+deaths+'\n')
        f.close()
        os.chdir(os.pardir)
    
if not os.path.exists("new_hopkins"):    #如果没有这个文件夹
        os.mkdir("new_hopkins")          #创建这个文件夹
        os.chdir("new_hopkins")          #切换到这个文件夹
else:   
        os.chdir("new_hopkins")

country()
US()
time.sleep(0.5)
spain()
ltaly()
time.sleep(0.5)
UK()
France()
time.sleep(0.5)
Germany()
Brazil()
t=datetime.datetime.now()
t=str(t).split('.')[0].replace(':','-')+','
print(t,'写入完成')
