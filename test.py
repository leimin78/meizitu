from lxml import etree
from parseHtml import htmlParse
import re

with open('test.txt','r') as f:
    html = f.readlines()

obj = etree.HTML(str(html))

url_rule = '//*//a//@href'
links = obj.xpath(url_rule)

title_rule = '//*[@class="lemmaWgt-lemmaTitle-title"]/h1/text()'
title = obj.xpath(title_rule)

print(title)

# newlink = []
#
# url_reg = r'^/item/.*'
#
# for link in links:
#     if re.search(url_reg,link):
#         newlink.append(link)
#
# print(newlink)

jiexi = htmlParse()
print(jiexi.parse('https://baike.baidu.com/item/%E5%B9%BF%E5%BA%9C%E6%96%87%E5%8C%96#1',str(html)))