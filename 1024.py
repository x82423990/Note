# coding:utf8
import os
import requests
import re, random, threading, time
from time import sleep, ctime

from pyquery import PyQuery as pq

cmp = re.compile(r'\d+\.jpg') # 图片的名字
Pre = re.compile(r'(\d+)(?:P)') # 每个主题图片的数量
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

# 获取图片URL


# 利用子页面，下载图片到本地
def download(res, img_dir, num_retries=3):  #重试次数为3
    try:
        res_page = requests.get(res, headers=headers, timeout=30)
        res_page.raise_for_status()
        res_doc = pq(res_page.text)
        res_li = (res_doc('#read_tpc').find('a'))
    except requests.HTTPError as e:
        res_li = None
        if num_retries > 0:
            download(res, img_dir, num_retries - 1)
    except requests.ConnectionError as e:
        return ''
    for j in res_li.items():
        tmp = pq(str(j))
        img_url = str(tmp('a').attr('href')).replace('i/?i=', '')
        print('正在下载'+img_url)
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
     Num = re.search(Pre, save_dir)
     if Num:
        totalFileCount = sum([len(files) for root, dirs, files in os.walk(save_dir)])
        if totalFileCount < 1:
            download(save_url, save_dir + '/')


# 根据PYQUERY生成的html条目解析href.
def get_down(i):
    res_dir = (i.text()).replace(' ', '').replace('，', '_')  # 去掉空格
    tmp = pq(str(i))  # 我解析不出来href, 用这种方法实属无奈自举.
    res_url = 'http://1024.stv919.biz/pw/' + (tmp('a').attr('href'))
    # print(res_url, res_dir)
    print('当前下载目录为%s' % res_dir)
    if not os.path.isdir(res_dir):
        os.mkdir(res_dir)
        download(res_url, res_dir + '/')    # 传入URL 和DIR
    else:
        Pd(res_dir, res_url)

# 获取标题和LI的url


def get_url_dir(url1, page_num, retry_num=3):   # 重试次数为3
    sleep(1)
    print('正在执行------')
    try:
        page = requests.get(url1, headers=headers, timeout=10)
        page.encoding = 'utf-8'
        doc = pq(page.text)
        li = (doc('tr').find('h3'))
    except requests.HTTPError as e:
        print(e+'尝试连接失败，正在重试')
        if retry_num:
            get_url_dir(url1, page_num, retry_num - 1)
    n = 0
    for i in li.items():    # 首页的前6个条目不要
        if page_num == 1:
            if n > 6:
                get_down(i)
        else:
            get_down(i)
        n += 1


def main(page_start=5, page_end=None):  # 传入起始页面，默认结抓取前5页
    if page_end is None:   
        for p in range(page_start):
            url = 'http://xxxx/pw/thread.php?fid=16&page=%s' % str(p+1)
            get_url_dir(url, p+1)
    else:
        for p in range(page_start, page_end):
            url = 'http://xxxx/pw/thread.php?fid=16&page=%s' % str(p+1)
            get_url_dir(url, p+1)

# 启用2个线程
threads = []
t1 = threading.Thread(target=main())
threads.append(t1)
t2 = threading.Thread(target=main())
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print("all over %s" % ctime())

