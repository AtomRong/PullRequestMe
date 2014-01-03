#! /usr/bin/env python
# -*- coding: utf-8 -*-


#id,name,pass,friends,offmsgs

#online list
#id,ip,loginTime

#server 
#types 登录，退出，注册，增，删好友，
import pickle,pprint

import threading,sys 
import socket, traceback
from consolofun import show  
  

onUdic={}
class recvHander(threading.Thread):
       def __init__(self,host='',port=54321):
           threading.Thread.__init__(self)
           self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.s.bind((host, port))
           self.s.listen(10)

          
       def run(self):
            connection,address =self.s.accept()
            print '接受来自'+str(address)+'的连接.'
            ra = connection.recv(1024)
            print str(address)+ '的数据：'+ra     
            
class onlineUser(object):
    def __init__(self,id,ip,time,name,port):
        self.id=id
        self.ip=ip
        self.time=time
        self.name=name
        self.port=port

def main():
     connectHander=recvHander('',54321)
     connectHander.start()
     while 1:
      print 'minro>:)'
      cmd = sys.stdin.readline().strip()
      if cmd == 'show':
          print 'hello,world'

if __name__=="__main__":
     main()
    
