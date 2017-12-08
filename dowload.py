#网页下载器

import requests
class htmlDowload:
    def __init__(self):
        self.s = requests.session()
        self.useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        self.headers = {'User-Agent':self.useragent}
        self.s.headers.update(self.headers)

    def download(self,url):

        r = self.s.get(url)
        if r.status_code == 200:
            r.encoding='gb2312'
            return r.text
        else:
            return None

