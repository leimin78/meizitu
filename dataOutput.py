### 存储数据并生成文件
import urllib
import os
import requests

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
headers = {'User-Agent':useragent}

class outputData:

    #初始化数据列表
    def __init__(self):
        self.datas = []

    def storeData(self,data):
        if data is None:
            return
        self.datas.append(data)

    def download(self,url,filename):

        ir = requests.get(url,headers=headers,stream=True)
        if ir.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in ir:
                    f.write(chunk)

    def outputImg(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        for data in self.datas:
            print("数据data{0}".format(data))
            # 图片路径
            try:
                title = data['title'][0]
            except:
                pass
            img_path = os.path.join(basedir, 'meizitu', title)
            # 目录不存在则创建
            isExists = os.path.exists(img_path)
            if not isExists:
                os.makedirs(img_path)
                i = 1
                for url in data['img_url']:
                    self.download(url, img_path + '/' + str(i) + '.jpg')
                    i += 1
            else:
                print("目录已存在不需要创建。")

