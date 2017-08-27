# coding:utf8
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

from pyquery import PyQuery as pq
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':'gzip',
           }
url1 = 'http://1024.stv919.biz/pw/thread.php?fid=16&page=1'
url2 = 'http://www.baidu.com'
# input_file = unicode(open(html).read(), 'utf-8')
# doc = pq(input_file)
#page = urllib2.urlopen("http://www.baidu.com")
page = requests.get(url1, headers=headers, timeout=10)
page.encoding='utf-8'
# text = unicode(html.read(), "utf-8")
# # query = pq(text)
doc = pq(page.text)
li = doc('.tr3 t_one').text()
print doc('#a_ajax_754135').html()
# ('p').filter('#1') #返回[<p#1>]
# d('p').filter('.2') #返回[<p.2>]
print li              # 处理元素
# for i in li:
#     print doc(i).find('h3')

# 1.把11行换为12行, 重点是要把读出的内容转成unicode再存为PyQuery对象
# input_file = open(file).read()
# input_file = unicode(open(html).read(), 'utf-8')
# doc = pq(input_file)