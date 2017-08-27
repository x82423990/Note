# coding:utf8
import os
import requests
import re, random
from time import sleep

from pyquery import PyQuery as pq

cmp = re.compile(r'\d+\.jpg')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':'gzip',
           }
UserAgent_List = [
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# input_file = unicode(open(html).read(), 'utf-8')
# doc = pq(input_file)
# page = urllib2.urlopen("http://www.baidu.com")
# class 1023(object):
#     def __init__(self, url, real_url, down_url, ra):
#         self.url = url
#         self.real_rul = real_url
#         self.down_url = down_url
#     def get_dir_resource
#         page = requests.get(url, headers=headers, timeout=10)
#         page.encoding = 'utf-8'
#         doc = pq(page.text)
#         li = (doc('tr').find('h3'))
#         for i in li.items():
#             res_dir = (i.text())
#             tmp = pq(str(i))    # 我解析不出来href, 用这种方法实属无奈自举.
#             res_url = (tmp('a').attr('href'))


# 获取图片URL

# 保存到文件
def download(res, img_dir):
    res_page = requests.get(res, headers=headers, timeout=30)
    res_doc = pq(res_page.text)
    res_li = (res_doc('#read_tpc').find('a'))
    for j in res_li.items():
        tmp = pq(str(j))
        img_url = str(tmp('a').attr('href')).replace('i/?i=', '')
        print(img_url)
        r = requests.get(img_url, headers=headers, timeout=30)
        img_name = re.search(cmp, img_url)
        if img_name is not None:
            with open(img_dir + img_name.group(), 'wb') as file:
                file.write(r.content)
                sleep(0.5)
        else:
            sleep(0.5)


# 判断已经下载的的图片数量和标题的数量是否相等
def Pd(save_dir, save_url):
     Num = re.search(r'(\d+)(?:P)', save_dir)
     if Num:
        totalFileCount = sum([len(files) for root, dirs, files in os.walk(save_dir)])
        if int(Num.group(1))-5 > totalFileCount:
            download(save_url, save_dir + '/')

#
def get_down(i):
    res_dir = (i.text()).replace(' ', '').replace('，', '_')  # 去掉空格
    tmp = pq(str(i))  # 我解析不出来href, 用这种方法实属无奈自举.
    res_url = 'http://1024.stv919.biz/pw/' + (tmp('a').attr('href'))
    print(res_url, res_dir)
    if not os.path.isdir(res_dir):
        os.mkdir(res_dir)
        download(res_url, res_dir + '/') # 传入URL 和DIR
    else:
        Pd(res_dir, res_url)

# 获取标题和LI的url


def get_url_dir(url1, page_num):
    sleep(1)
    print('正在执行------')
    page = requests.get(url1, headers=headers, timeout=10)
    page.encoding = 'utf-8'
    doc = pq(page.text)
    li = (doc('tr').find('h3'))
    n = 0
    for i in li.items():
        if page_num == 1:
            if n > 5:
                get_down(i)
        else:
            get_down(i)
        n += 1

for p in range(3, 10):
    url = 'http://1024.stv919.biz/pw/thread.php?fid=16&page=%s' % str(p+1)
    get_url_dir(url, p+1)






