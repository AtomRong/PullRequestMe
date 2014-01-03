#-*- coding: utf-8 -*-
def show(str):
    global onUdic
    if str=='n':
       print '当前在线总用户数为：'+str(len(onUdic))
    elif str == 'l':
       print '序号： id    ip      Login_time'
       for i in range(1,len(onUdic)):
          print 'User '+str(i)+': '+str(onUdic[i].id)+' '+onUdic[i].ip+" "+onUdic[i].time
    else:
       print '命令错误，请重新输入，或者help查询'



    
