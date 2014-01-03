#!/usr/bin/python
# -*- coding:utf-8 -*-
# GUI.py
import time
import sys
from PyQt4 import QtGui, QtCore


class loginGui(QtGui.QDialog):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self)
		
		self.setWindowTitle("Login")
		
		self.user = QtGui.QLabel("ID")
		self.pw = QtGui.QLabel("Password")
		
		self.userEdit = QtGui.QLineEdit()
		self.pwEdit = QtGui.QLineEdit()
		self.pwEdit.setEchoMode(QtGui.QLineEdit.Password)
		
		self.login = QtGui.QPushButton("Login")
		self.register= QtGui.QPushButton("Register")
		
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)
		
		self.grid.addWidget(self.user, 1, 0)
		self.grid.addWidget(self.userEdit, 1, 1)
		
		self.grid.addWidget(self.pw, 2, 0)
		self.grid.addWidget(self.pwEdit, 2, 1)
		
		
		self.grid.addWidget( QtGui.QLabel(''), 3, 0)
		self.grid.addWidget(self.login, 3, 1 )
		self.grid.addWidget(self.register, 3, 2)
		
		self.setLayout(self.grid)
		self.resize(400, 250)
		self.center()
		
		self.login.clicked.connect(self.isSuccess)
		self.register.clicked.connect(self.gotoRe)
		
	def isSuccess(self):   
		if self.userEdit.text() == '' and self.pwEdit.text() == '':   
            # 如果用户名和密码正确，关闭对话框，accept()关闭后，如果增加一个取消按钮调用reject()   
			self.accept()   
		else:   
			QtGui.QMessageBox.critical(self, 'Error', 'ID or password error')
	
	def gotoRe(self):	#go to register 
		registergui = RegisterGui()
		registergui.exec_()
	
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,
				(screen.height()-size.height())/2)
				
				
				
				
				
				
				
				
class RegisterGui(QtGui.QDialog):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self)
		self.setWindowTitle("Register")
		
		self.name = QtGui.QLabel("Name")
		self.pw = QtGui.QLabel("Password")
		self.pwAgain = QtGui.QLabel("PwdAgain")
		
		self.nameEdit = QtGui.QLineEdit()
		self.pwEdit = QtGui.QLineEdit()
		self.pwEdit.setEchoMode(QtGui.QLineEdit.Password)
		self.pwAgainEdit = QtGui.QLineEdit()
		self.pwAgainEdit.setEchoMode(QtGui.QLineEdit.Password)
		
		self.submit = QtGui.QPushButton("Submit")
		
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)
		
		self.grid.addWidget(self.name, 1, 0)
		self.grid.addWidget(self.nameEdit, 1, 1)
		
		self.grid.addWidget(self.pw, 2, 0)
		self.grid.addWidget(self.pwEdit, 2, 1)
		
		self.grid.addWidget(self.pwAgain, 3, 0)
		self.grid.addWidget(self.pwAgainEdit, 3, 1)
		
		
		self.grid.addWidget( QtGui.QLabel(''), 3, 0)
		self.grid.addWidget(self.submit, 4, 1 )
		
		self.setLayout(self.grid)
		
		self.resize(400, 250)
		self.center()
		
		self.submit.clicked.connect(self.submit2ser)
		
	def submit2ser(self):
		if self.pwEdit.text() == self.pwAgainEdit.text():
			print "pipei"
			self.close()
		else:
			QtGui.QMessageBox.critical(self, 'Error', 'Password error')
		
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,
				(screen.height()-size.height())/2)
						
		
