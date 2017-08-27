# coding:utf8
from multiprocessing import Pool
import os, time, random, requests
from datetime import datetime

def long_time_task(url):
    with open('/tmp/test.txt', 'a+') as f:
        time1_str = datetime.now().strftime('%H-%M-%S')
        f.write(time1_str+'\n')
        code=str(requests.get(url).status_code)
        print code, time1_str
        f.write(code+'\n')



if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(20)
    n=0
    while n<10:
      p.apply_async(long_time_task, args=("http://www.jb51.net",))
      n+=1
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


# 注解：对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成