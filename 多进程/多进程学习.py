#coding=utf-8
'''线程与进程的区别
线程同时修改一份数据时必须加锁，mutex互斥锁
什么时候使用多线程？
io操作不占用CPU
计算占用CPU，
pyhton多线程不适合cpu密集操作性的任务，适合io操作密集的任务
'''
import multiprocessing
import time
import threading

# def threadrun():
#     print threading._get_ident()
#
# def run(name):
#     time.sleep(2)
#     print 'hello',name
#     t = threading.Thread(target=threadrun)     #进程里面再启动线程
#     t.start()
#
# if __name__ ==  '__main__':
#     for i in range(10):
#         p = multiprocessing.Process(target=run,args=('zq%s'%i,))    #启动进程
#         p.start()
#     #p.join()
#
# #获取进程号
# from multiprocessing import Process
# import os
#
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())
#     print("\n\n")
#
#
# def f(name):
#     info('\033[31;1mcalled from child process function f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
#     info('\033[32;1mmain process line\033[0m')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     # p.join()
#进程之间的通讯   线程之间的队列可以共享使用，但是进程之间不行，线程的队列不可以传给另一个进程使用
#如果想使用，必须使用进程队列：Queue
'''
主进程将进程队列当做参数传给子进程，实际上是克隆一个进程队列给子进程，并不是共享，
但是当主进程往主进程序列put东西的时候，主进程队列会通过pickle数据实例化把主进程
队列的数据分享克隆给子进程的序列，
'''

# from multiprocessing  import Process
# from multiprocessing  import Queue
# def f(qq):
#     qq.put([42,None,'zq'])
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f,args=(q,))
#     p.start()
#     print q.get()
#     p.join()
#两个进程之间通信的另一种方法：管道
# from multiprocessing import Process,Pipe
# def f(conn):
#     conn.send(['12341','qweqwe'])
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn,child_conn = Pipe()
#     p = Process(target=f,args=(child_conn,))
#     p.start()
#     print  parent_conn.recv()
#     p.join()

#两个进程之间分享数据之：manager    manager自带进程锁，不需要设置
# from multiprocessing import Process,Manager
# import os
#
# def f(dict1,list1):
#     dict1[os.getpid()] = os.getpid()
#     list1.append(os.getpid())
#     print list1
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()     #生成一个字典可以在多个进程之间传递和共享
#         l= manager.list(range(5)) #生成一个列表可以在多个进程之间传递和共享
#         p_objlist = []
#         for i in range(10):
#             p = Process(target=f,args=(d,l))
#             p.start()
#             p_objlist.append(p)
#         for res in p_objlist:
#             res.join()
#
#         print d
#         print l

#进程锁   用于屏幕共享，比如打印进程1的数据时候会插入进程2的数据
# from multiprocessing import Process,Lock
# def f(l,i):
#     l.acquire()
#     print ' I am %s'%i
#     l.release()
#
# if __name__ == '__main__':
#     lock= Lock()
#     for num in range(100):
#         Process(target=f,args=(lock,num)).start()

#进程池   防止进程过多占用过多内存指定同时执行的进程数量，其他进程属于挂起状态
from multiprocessing import Process,Pool
import time
import os
def Foo(i):
    time.sleep(1)
    print 'in process',os.getpid()
    return i + 100,'a'

def  Bar(arg):                #回调
    print 'exec done',arg,os.getpid()

if __name__ == '__main__':
    pool = Pool(processes=3)    #允许进程池同时放入进程的数量
    print '主进程的ID：',os.getpid()
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)  #callback为回调函数，每个子进程完成会干的事，在主进程中进行的  Foo的返回值的参数给了Bar函数
        #pool.apply()  #串行
    print 'end'
    pool.close()
    pool.join()     #必须先关闭进程池再join，顺序不能错，否则程序直接关闭