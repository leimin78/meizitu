import os
import datetime
import pymysql
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


class queryDB:
    # 初始化查询连接
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.conn = pymysql.connect('localhost', 'root', '123456', 'wordpress',charset='utf8')
        self.cur = self.conn.cursor()

    def query_db(self, query):
        #执行语句,获取数据
        print(query)
        self.cur.execute(query)
        self.datas = self.cur.fetchall()
        return self.datas

    def delete_db(self,delsql):
        self.cur.execute(delsql)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

def addPressPost(title,id,content):
    post = WordPressPost()
    post.title = title
    # post.content = """
    #             <img class="alignnone size-medium wp-image-54" src="http://127.0.0.1/meizitu/1.jpg" />
    #             <img class="alignnone size-medium wp-image-53" src="http://127.0.0.1/meizitu/2.jpg" />
    #             <img class="alignnone size-medium wp-image-52" src="http://127.0.0.1/meizitu/3.jpg" />
    #             <img class="alignnone size-medium wp-image-51" src="http://127.0.0.1/meizitu/4.jpg" />
    #             <img class="alignnone size-medium wp-image-50" src="http://127.0.0.1/meizitu/5.jpg" />
    #             <img class="alignnone size-medium wp-image-49" src="http://127.0.0.1/meizitu/6.jpg" />"""

    post.content = content
    print(content)
    post.post_status = 'publish'
    post.thumbnail = id
    post.definition
    post.id = client.call(posts.NewPost(post))

#填入自己域名及wordpress 账号密码
client = Client('http://xxxxx/xmlrpc.php', 'xxxxx', 'xxxxxx')

#filename = ['/Users/leimin/spiderCrawl/baike/meizitu/这背影真是让人难忘/3.jpg','/Users/leimin/spiderCrawl/baike/meizitu/这背影真是让人难忘/4.jpg']

# prepare metadata
data = {
        'name': 'picture.jpg',
        'type': 'image/jpeg',  # mimetype
}

# read the binary file and let the XMLRPC library encode it into base64
# for file in filename:
#     with open(file, 'rb') as img:
#             data['bits'] = xmlrpc_client.Binary(img.read())
#
#     response = client.call(media.UploadFile(data))
#     addPressPost('test',response['id'])
# response == {
#       'id': 6,
#       'file': 'picture.jpg'
#       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
#       'type': 'image/jpeg',
# }
#attachment_id = response['id']
#

#新增文件

def getFileList(path):
    for root, dirs, files in os.walk(path):
        # print("root{0}".format(root))
        # print("dirs{0}".format(dirs))
        # print("files{0}".format(files))

        #如果没有子目录
        if len(dirs) == 0:

            #文章标题
            post_title = root.split('/')[-1]
            db = queryDB()
            datas = db.query_db("select post_title from wp_posts where post_title='{0}'".format(post_title))
            if len(datas) == 0:
                post_content = """"""
                for file in files:
                    post_content += '<img class="alignnone size-medium wp-image-54" src="http://www.mzitup.com/meizitu/{0}/{1}" />'.format(post_title,file) +'\n'
                try:
                    #添加特色图片并新增文章
                    with open(root+'/'+files[0], 'rb') as img:
                        data['bits'] = xmlrpc_client.Binary(img.read())
                except Exception as e:
                    print(e.args)
                response = client.call(media.UploadFile(data))
                addPressPost(post_title, response['id'],post_content)
            else:
                print("图片已存在不插入")

getFileList('/var/www/html/meizitu')

