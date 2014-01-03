#!/usr/bin/python
# -*- coding:utf-8 -*-
# GUI.py
import time
import sys
from PyQt4 import QtGui, QtCore

from loginGui import loginGui
import mainGui


app = QtGui.QApplication(sys.argv)
icon = loginGui()
if icon.exec_():   
    fri = mainGui.friendListGui()  
   # app.setMainWidget( fri )
    fri.show()   
    sys.exit(app.exec_())
