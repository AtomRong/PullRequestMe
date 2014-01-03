#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

def getLocalIP( website="sysu.edu.cn"):
    """ 返回 局域网中的 本地IP """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(( website,80)) 
    result = s.getsockname()[0]
    s.close()
    return result

