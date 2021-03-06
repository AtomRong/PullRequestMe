#-*- coding: utf-8 -*- 
import socket, sys
import threading,Queue
import select
import time  
host = sys.argv[1]
textport = sys.argv[2]
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
     port = int(textport)
except ValueError:
     port = socket.getservbyname(textport, 'tcp')
#s.connect((host, port))
s.bind( ('',54321))

#任务类，tcp要处理的连接
class work(object):
      def __init__(self,othersoc,otheradd,pri):
          self.othersoc=othersoc
          self.otheradd=otheradd
          self.pri=pri
      def __cmp__(self,other):
          return cmp(self.pri,other.pri)


class WorkerManager(threading.Thread):
      def __init__(self,work_num=1000,thread_num=2):
          self.workQ=Queue.PriorityQueue()        
          self.threads=[]
          self.init_work_queue_(work_num)
          self.init_thread_pool_(thread_num)
          threading.Thread.__init__(self)

      #初始化线程池
      def init_thread_pool_(self,thread_num):
          for i in range(thread_num):
             self.threads.append(Worker(i,self.workQ))
      #初始化任务队列
      def init_work_queue_(self,work_num):
          print 'init_work_queue'

      #添加一项任务至队列
      def add_work(self,twork):
          print 'add a job to queue'
          self.workQ.put(twork,False)  
      
      def check_queue(self):
          return self.workQ.qsize()

      def wait_allcomplete(self):
          for item in self.threads:
              if item.isAlive():
                 item.join()
     
#worker 处理任务线程                             

class Worker(threading.Thread):
      def __init__(self,id,work_q):
          self.id=id
          self.work_queue=work_q
          threading.Thread.__init__(self)
          self.setDaemon(1)
          self.start()

      def run(self):
          while 1:
             try:
               if self.work_queue.qsize()>0:
                  job=self.work_queue.get(block=False)#任务异步出队，Queue内部实现同步机制
                  self.process(job)
                  print 'Process: Job complete'
                  self.work_queue.task_done()
                  print 'Undo works:'+str(self.work_queue.qsize())
               else:
                  time.sleep(10)
             except Exception,e:
                   print str(e)
                   break
      def process(self,job):
          print 'process data'
          data='start'
          while  len(data)>0:
           data=job.othersoc.recv(100)
           job.othersoc.send('guess who am I')
           print 'thread '+str(self.id)+'recv data:'+data


work_manager=WorkerManager(10,2)
s.listen(10)  
inputs=[s]         
while 1:
     try:
        othersock,otheraddr=s.accept()
     except (KeyboardInterrupt, SystemExit):
        raise
     except:
        continue
     if otheraddr == host:
        work_manager.add_work(work(othersock,otheraddr,1))
     else:
        work_manager.add_work(work(othersock,otheraddr,10))    
     print "你想怎么样\n"
  
