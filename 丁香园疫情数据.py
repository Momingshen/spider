import re
import time
import os
import requests
from urllib import request
import json

#保存位置
savePath = r'./new_dxy1'

class Spider():

    def creat_dir(self, path):
        '''
        创建文件夹
        参数：创建位置路径
        '''
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")# 判断路径是否存在
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False
    
    def get_html(self, html_url):
        '''
        获取html
        参数：url
        '''
        html = requests.get(html_url).content #添加headers避免服务器拒绝非浏览器访问
        return html.decode("utf-8", "ignore")
    
    def get_json_str(self, html):
        '''
        获取城市页面url字段
        参数：主页面html
        '''
        # json_str = re.findall('<script id="getListByCountryTypeService2">try { window.getListByCountryTypeService2 = (.*)}catch\(e\){}</script><script id="getIndexRecommendList">', html)
        json_str = re.findall('<script id="getAreaStat">try { window.getAreaStat = (.*?)}catch\(e\){}', html)
        return json_str

    def convert_str_to_json(self, json_str):
        '''
        获取城市页面url字段
        参数：主页面html
        '''
        data = json.loads(json_str[0])
        return data

    def download(self, save_path, data):
        
        print('writing file ...' + save_path)
        html_file = open(save_path, 'a', encoding='utf-8')
        html_file.write(data)
        html_file.close()
        print('successfully!')

    def analyse(self, run_time):
        '''
        下载保存
        参数：保存路径，创建时间
        '''
        url = 'https://3g.dxy.cn/newh5/view/pneumonia'
        html = self.get_html(url)
        # print(html)
        json_str = self.get_json_str(html) # 获取html中的json数据
        while len(json_str)==0:
            print('获取失败')
            print(len(json_str))
            self.run()
        # 保存html文件
        html_folder_path = savePath + '\\html'
        self.creat_dir(html_folder_path) # 创建html文件夹
        html_file_path = html_folder_path + '\\' + run_time + '.html'
        self.download(html_file_path, html)
        data = self.convert_str_to_json(json_str)
        # print(data)
        for i in range(0, len(data)):
            provinceName = data[i]['provinceName']
            provinceShortName = data[i]['provinceShortName']
            provinceConfirmedCount = data[i]['confirmedCount']
            provinceSuspectedCount = data[i]['suspectedCount']
            provinceCuredCount = data[i]['curedCount']
            provinceDeadCount = data[i]['deadCount']
            provinceComment = data[i]['comment']
            
            province_file_path = savePath + '\\' + provinceName
            self.creat_dir(province_file_path) # 创建省文件夹
            

            if provinceComment!='':
                print('补充说明:'+provinceComment)
                comment_file_path = province_file_path + '\\comment.txt'
                self.download(comment_file_path, provinceComment+'\n')

            cityNames = data[i]['cities']
            if len(cityNames)==0:
                province_data = str(run_time)+','+str(provinceConfirmedCount)+','+str(provinceSuspectedCount)+','+str(provinceCuredCount)+','+str(provinceDeadCount)+'\n'
                print(province_data)
                city_file_path = province_file_path + '\\' + provinceShortName + '.csv'
                self.download(city_file_path, province_data)
            else:   
                print(str(provinceName)+'  '+str(provinceShortName)+'  '+str(provinceConfirmedCount)+'  '+str(provinceSuspectedCount)+'  '+str(provinceCuredCount)+'  '+str(provinceDeadCount)) 
                for j in range(0, len(cityNames)):
                    cityName = cityNames[j]['cityName']
                    cityConfirmedCount = cityNames[j]['confirmedCount']
                    citySuspectedCount = cityNames[j]['suspectedCount']
                    cityCuredCount = cityNames[j]['curedCount']
                    cityDeadCount = cityNames[j]['deadCount']
                    city_data = str(run_time)+','+str(cityConfirmedCount)+','+str(citySuspectedCount)+','+str(cityCuredCount)+','+str(cityDeadCount)+'\n'
                    print(city_data)
                    city_file_path = province_file_path + '\\' + cityName + '.csv'
                    self.download(city_file_path, city_data)


    def run(self):
        #运行时间
        run_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        #创建备用文件夹等待压缩
        #下载
        self.analyse(run_time)

#开始运行
print('Start ' + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))  
spider = Spider()
spider.run()
print('End ' + time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))

