###调度器

from dataOutput import outputData
from parseHtml import htmlParse
from dowload import htmlDowload
from manager import spiderManager
import multiprocessing as mp


class MeiziTu:

    #初始化 url管理,下载器,解析器,存储
    def __init__(self):
        self.manage = spiderManager()
        self.load = htmlDowload()
        self.jiexi = htmlParse()
        self.output = outputData()

    #添加爬虫入口
    def crawl(self,root_url):
        self.manage.add_new_url(root_url)

        #判断url管理是否有新url 同时判断抓取的数据条数
        while(self.manage.has_new_url()):
            try:
                #从url管理器获取新的url
                new_url = self.manage.get_new_url()

                #对网页进行下载
                page_content = self.load.download(new_url)
                # with open('test.txt','w') as f:
                #     f.write(page_content)

                #对下载网页做解析
                new_urls,data = self.jiexi.parse(new_url,page_content)
                print("new_urls:{0},type{1}".format(new_urls,type(new_urls)))
                #print("type{0}".format(type(new_urls)))

                #将新抓取的url加入url管理器
                self.manage.add_new_urls(new_urls)

                #对数据进行存储
                self.output.storeData(data)
            except Exception as e:
                print(e.args)
                print("crawl failed")

            self.output.outputImg()

if __name__ == '__main__':

    meizi = MeiziTu()
    #baike.crawl('http://www.meizitu.com/')

    p = mp.Pool(10)
    p.map_async(meizi.crawl('http://www.meizitu.com/'))
    p.close()
    p.join()

