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
    for i in range(90):
        p.apply_async(long_time_task, args=("http://www.jb51.net",))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# long_time_task("http://www.jb51.net")