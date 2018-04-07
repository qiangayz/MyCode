#coding=utf-8
"""
进程: 要以一个整体的形式暴露给操作系统管理，里面包含对各种资源的调用，内存的管理，网络接口的调用等。。。
对各种资源管理的集合 就可以成为  进程
线程: 是操作系统最小的调度单位， 是一串指令的集合
进程 要操作cpu , 必须要先创建一个线程  ，
所有在同一个进程里的线程是共享同一块内存空间的
进程与线程的区别？
线程共享内存空间，进程的内存是独立的
同一个进程的线程之间可以直接交流，两个进程想通信，必须通过一个中间代理来实现
创建新线程很简单， 创建新进程需要对其父进程进行一次克隆
一个线程可以控制和操作同一进程里的其他线程，但是进程只能操作子进程
"""
import threading
import time
# def run(n):
#     print 'it is ',n,threading.current_thread()
#     time.sleep(5)
#     print 'done'

# t1 = threading.Thread(target = run,args=('x1',))
# t2 = threading.Thread(target = run,args=('x1',))
# t1.start()
# t2.start()
# run('x1')
# run('x1')
class MyThread(threading.Thread):       #继承式调用
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self):
        print 'now run is',self.n,threading.current_thread()

# t1 = MyThread('x1')
# t2 = MyThread('x2')
# t1.start()
# t2.start()
# start_time = time.time()     #主线程不会等子线程执行完毕就会继续往下走，所以花费时间的值不是5S
# t_obj = []   #储存线程实例的列表
# for i in range(50):
#     t1 = threading.Thread(target=run, args=('x%s'%i,))
#     t1.setDaemon(True)  #当前线程设置为守护线程，主线程完成之后不会等待守护线程执行到什么进度直接退出。
#     t1.start()
#     t_obj.append(t1)
# print '__________',threading.active_count()
# # for i in t_obj:
# #     i.join()                        #等待所有线程结束之后再往下继续执行
#
# print 'cost time is ',time.time()-start_time,threading.current_thread(),threading.active_count()  #返回当前线程，返回活跃的线程个数
#加入 t1.join()就会等待t1执行完成后再往下走,循环的50个属于子线程，主线程不包含在内，所以当前执行的线程一共有51个
# num = 0
# lock = threading.Lock()                 #加入进程锁
# def run(n):
#     lock.acquire()             #获取锁
#     global num
#     num += 1
#     #time.sleep(1)             #加入sleep就会变成串行，等待时间释放锁
#     lock.release()             #释放锁
#
# t_obj = []
# for i in range(50):
#     t1 = threading.Thread(target=run, args=('x%s'%i,))
#     t1.start()
#     t_obj.append(t1)
# for i in t_obj:
#     i.join()
#
# print 'now num is ',num

#递归锁
import threading, time


def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)




# num, num2 = 0, 0
# lock = threading.RLock()
# for i in range(1):
#     t = threading.Thread(target=run3)
#     t.start()
#
# while threading.active_count() != 1:               #等待子进程结束的另一种方式
#     print(threading.active_count())
# else:
#     print('---- done---')
#     print(num, num2)

# #信号量
# num = 0
# lock = threading.Lock()                 #加入进程锁
# semaphore = threading.BoundedSemaphore(5)  #最多允许5个进程同时运行
# def run(n):
#     semaphore.acquire()
#     #lock.acquire()             #获取锁
#     global num
#     num += 1
#     time.sleep(1)             #加入sleep就会变成串行，等待时间释放锁
#     #lock.release()             #释放锁
#     semaphore.release()
#     print num
#
# t_obj = []
#
# for i in range(50):
#     t1 = threading.Thread(target=run, args=('x%s'%i,))
#     t1.start()
#     t_obj.append(t1)
# for i in t_obj:
#     i.join()
#
# print 'now num is ',num
#事件,两个线程之间的交互
event = threading.Event()
def light():
    count = 0
    event.set()
    while True:
        if count >5 and count <10:    #变红灯
            event.clear()   #清除标志位
            print '\033[41;1mred lingt is on...\033[0m '
        elif count>10:
            event.set()     #设置标志位 变绿灯
            count = 0
            print '\033[42;1mgreen lingt is on...\033[0m '
        else:
            print '\033[42;1mgreen lingt is on...\033[0m '

        time.sleep(1)
        count +=1

def car():
    while True:
        if event.is_set():   #代表是绿灯
            print 'running'
        else:
            print 'waiting'
            event.wait()
            print 'begain run'
        time.sleep(1)
# light = threading.Thread(target=light)
# car1 = threading.Thread(target=car)
# light.start()
# car1.start()

#队列 queue
import Queue
# q = Queue.Queue()   #先入先出
# #q = Queue.Queue(maxsize=3)  设置队列的最大值
# q.put('d1')
# q.put('d2')
# q.put('d3')
# print q.qsize()
# print q.get()
# print q.get()
# print q.get()
# #q.get()    #如果队列里面没有内容会锁死
# #解决锁死的两种办法，put也可以加block和timeout参数
# q.get(block=False)
# q.get(timeout=1)
#
# q = Queue.LifoQueue() #后进先出
# q1 = Queue.PriorityQueue()#可以设置有限级
# q.put((10,'a'))  #设置的方法
# q.put((6,'b'))
# q.put((-1,'v'))
# q.put((0,'d'))


#生产者消费者模型
q = Queue.Queue(maxsize=10)
def Producer():
    count = 0
    while True:
         q.put('baozi%s'%count)
         count +=1
         print "生产了%s包子"%count
         time.sleep(1)

def Consumer(name):
    #while q.qsize()>0:
    while True :
        print '%s 取到包子%s'%(name,q.get())

p = threading.Thread(target=Producer)
c = threading.Thread(target=Consumer,args=('xiaoming',))
d = threading.Thread(target=Consumer,args=('xiaohong',))
p.start()
c.start()
d.start()


