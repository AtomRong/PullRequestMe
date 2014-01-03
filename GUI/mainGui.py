#!/usr/bin/python
# -*- coding:utf-8 -*-
# GUI.py
import time
import sys

from PyQt4 import QtGui, QtCore, Qt


class friendListGui(QtGui.QWidget):
    def __init__(self, parent = None):
        super( friendListGui, self ).__init__( None )
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Minet")
        
        self.chatWnds = {}  # 以id 为键， chatGui为值
        self.flag = 0  #0表示p2p，1表示聊天室
        
        #在线好友列表
        self.online = QtGui.QLabel("OnlineFriend", self)
        self.online.setGeometry(0,0,350,30)
        
        self.onList = QtGui.QListWidget(self)
        self.onList.setGeometry(0, 30, 350, 200)
        self.onListItem=[]
        
        for i in range(20):
            self.onListItem.append(QtGui.QListWidgetItem("name "+ str(i) ))
        
        for i in range(len(self.onListItem)):
            self.onList.insertItem(i+1,self.onListItem[i])
        self.onList.clicked.connect(self.onChat)
        
        #不在线好友列表
        self.offline = QtGui.QLabel("offlineFriend", self)
        self.offline.setGeometry(0,230,350,30)
        
        self.offList = QtGui.QListWidget(self)
        self.offList.setGeometry(0, 260, 350, 200)
        offListItem=[]
        
        for i in range(20):
            offListItem.append(QtGui.QListWidgetItem( "name "+str(i+20)  )  )
        
        for i in range(len(offListItem)):
            self.offList.insertItem(i+1,offListItem[i])
        self.offList.clicked.connect(self.offChat)    
        
        #Chatroom
        self.chat = QtGui.QPushButton("ChatRoom", self)
        self.chat.setGeometry(0, 460, 350, 30)
        self.chat.clicked.connect(self.chatRoom)
        
        #Add Or Delete Friend
        self.addFri = QtGui.QPushButton("AddFriend", self)
        self.addFri.setGeometry(250, 580, 100, 20)
        self.addFri.clicked.connect(self.AddFri)
        
        self.delFri = QtGui.QPushButton("DelFriend", self)
        self.delFri.setGeometry(150, 580, 100, 20)
        self.delFri.clicked.connect(self.DelFri)
        
        self.resize(350, 600)
        self.edge()
        
    def AddFri(self):
        #向服务器发送，返回能够加为好友的数据包
        self.addF = AddFriGui(self.onList)
        self.addF.show()
    
    def DelFri(self):
        reply = QtGui.QMessageBox.question(self, 'Message',
        "Are you sure to delete the friend "+self.onList.currentItem().text(),
         QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            row = self.onList.currentRow()
            self.onList.takeItem(row)

    def chatRoom(self):
        self.flag = 1
        self.Chat()
    
    def onChat(self):
        self.flag = 0
        self.Chat()
    
    def offChat(self):
        self.flag = 2
        self.Chat()
        
    def Chat(self):
        if self.flag == 1:
            key = chatTitle = "ChatRoom"
            
        elif self.flag == 0:
            chatTitle = self.onList.currentItem().text()
            key = chatTitle.split(" ")[1]  # friend ID
                        
        elif self.flag == 2:
            chatTitle = self.offList.currentItem().text()
            key = chatTitle.split(" ")[1]  # friend ID
        else:
            print( "error in Chat()!!")
        if not key in self.chatWnds: 
            chat_with = ChatGui(self,  chatTitle, self.flag)
            self.chatWnds[key]= chat_with
            self.flag = 0
            chat_with.show()
    
    def edge(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width()), 0)
        
        
        
class AddFriGui(QtGui.QDialog):
    def __init__(self, List):
        QtGui.QDialog.__init__(self)    
        
        self.List = List
        
        self.setWindowTitle("AddFriend")
        
        self.grid = QtGui.QGridLayout()
        
        self.ID = QtGui.QLabel("ID")
        self.IDEdit = QtGui.QLineEdit()
        self.search = QtGui.QPushButton("Search", self)
        
        self.grid.addWidget(self.ID, 0, 0 )
        self.grid.addWidget(self.IDEdit, 0, 1)
        self.grid.addWidget(self.search, 1, 1 )
        
        self.setLayout(self.grid)
        self.resize(300, 200)
        
        self.search.clicked.connect(self.Search)
        
    def Search(self):
        if True: #如果服务器查找该id存在，且对方同意，则加其为好友
            self.List.insertItem(self.List.count()+1, QtGui.QListWidgetItem("1111"))
            #用从服务器中返回的昵称代替这里的‘1111’就可以在列表中显示了
        else:
            QtGui.QMessageBox.critical(self, 'Error', "The ID"+self.IDEdit.text()+' does not exit!')

class ChatGui(QtGui.QDialog):
    def __init__(self, parent, FriName='', flag=0):  #parent 参数是 friendListGui
        QtGui.QDialog.__init__(self, parent )   #这里使用 未绑定的 超类构造函数 
        
        self.setAttribute( QtCore.Qt.WA_DeleteOnClose ) 
        self.parent = parent
        if "ChatRoom" == FriName:
            self.key = FriName
        else:
            self.key = FriName.split(" ")[1]
        self.message = ''  #text_read(显示消息的文本框)中显示的内容
        
        self.FriName = FriName
        self.flag = flag     #0表示p2p，1表示聊天室,根据这个来区分报文
        
        self.setWindowTitle(self.FriName)    # 使聊天框的title为好友的昵称
        #self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        
        self.text_read = QtGui.QTextEdit('', self)
        #self.text_read.setMaximumSize(QtCore.QSize(16777215, 25))
        self.text_read.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        
        self.text_read.setReadOnly(True)
        self.text_read.setGeometry(QtCore.QRect(0, 0, 600, 400))
        
        self.submit = QtGui.QPushButton("Submit", self)
        self.submit.setGeometry(500, 600, 100, 20)
        self.submit.setShortcut('Ctrl+.')        #发送消息的快捷键
        self.submit.clicked.connect(self.Submit)
        
        self.record = QtGui.QPushButton("Recording", self)
        self.record.setGeometry(500, 400, 100, 20)
        self.submit.clicked.connect(self.Recording)
        
        self.color_bu = QtGui.QPushButton("Color", self)
        self.color_bu.setGeometry(0, 400, 100, 20)
        self.color_bu.clicked.connect(self.setColor_)
        
        self.font_bu = QtGui.QPushButton("font", self)
        self.font_bu.setGeometry(100, 400, 100, 20)
        self.font_bu.clicked.connect(self.setfont_)
        
        self.text_write = QtGui.QTextEdit('', self)
        self.text_write.setGeometry(QtCore.QRect(0, 420, 600, 180))
        
        self.resize(600, 620)
        self.center()
        
    def Recording(self):
        #将原来（一短时间）的记录显示到text_read中。
        #self.text.read.setText(从文件中读取的内容--字符串)
        pass
    
    def Submit(self):    #根据self.flag 区分报文
        if self.text_write.toPlainText() != '':
            self.message += time.ctime()+"\n"+ self.text_write.toPlainText()+"\n"
            self.text_read.setText( self.message )
            self.text_write.setText("")
        else:
            QtGui.QMessageBox.critical(self, 'Error', "You can't sent message without content!")
        
    def setColor_(self):
        col = QtGui.QColorDialog.getColor()
        if col.isValid():
            self.text_write.setTextColor(QtGui.QColor(col.name()))
            self.text_read.setTextColor(QtGui.QColor(col.name()))
        
    def setfont_(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.text_read.setFont(font)
            self.text_write.setFont(font)
        
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
                (screen.height()-size.height())/2)
    
    def closeEvent( self, event ):
        del self.parent.chatWnds[self.key]
