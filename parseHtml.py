import re
from lxml import etree

class htmlParse:

    def parse(self,page_url,page_content):
        if page_url is None or page_content is None:
            return
        new_urls = self._get_new_urls(page_url,page_content)
        new_datas = self._get_new_data(page_url,page_content)
        return new_urls,new_datas

    def _get_new_urls(self,page_url,page_content):
        new_urls = set()
        url_rule = '//*//a//@href'
        obj = etree.HTML(page_content)
        links = obj.xpath(url_rule)
        url_reg = r'http://www.meizitu.com.*\d.html'

        for link in links:
            if re.search(url_reg, link):
                new_url = link
                #print(new_url)
                new_urls.add(new_url)

        #print("new_urls{0}".format(new_urls))
        return new_urls


    def _get_new_data(self,page_url,page_content):
        data = {}
        data['url'] = page_url

        title_rule = '//*[@id="maincontent"]/div[1]/div[1]/h2//a/text()'
        imgs_rule = '//*[@id="picture"]/p//img/@src'
        obj = etree.HTML(page_content)
        data['title'] = obj.xpath(title_rule)
        data['img_url'] = obj.xpath(imgs_rule)

        print("正在爬去{0}".format(page_url))
        print("data_title:{0}".format(data['title']))
        print("data_imgulr:{0}".format(data['img_url']))

        return data