# -*- coding: utf-8 -*-


class msg(object):
      def __init__(type='',srcid,dstid,time,content):
          self.dic={}
          self.dic['type']=type
          self.dic['srcId']=srcid
          self.dic['dstId']=dstid
          self.dic['time']=time
          self.dic['text']=text

class onlineUser(object):
    def __init__(self,id,ip,time,name,port):
        self.id=id
        self.ip=ip
        self.time=time
        self.name=name
        self.port=port
  
