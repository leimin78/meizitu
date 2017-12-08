### 爬虫管理器

class spiderManager:

    #初始化已爬去，未爬去集合
    def __init__(self):
        self.new_urls = set() #未爬取url
        self.old_urls = set() #已爬去url

    #判断是否存在未爬去url
    def has_new_url(self):
        return self.get_new_url_size != 0

    #获取新url,对未爬去url进行出栈,然后加入到已爬去url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    #新增爬去链接
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #新增url 列表
    def add_new_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    #获取未爬去url size
    def get_new_url_size(self):
        return len(self.new_urls)

    #获取已爬去url size
    def get_old_url_size(self):
        return len(self.old_urls)

