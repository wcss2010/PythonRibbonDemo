#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_MainWindow import *
import os
import sys
import pathlib
import datetime

'''
    这是MainWindow窗体的实现类
'''
#class FMainWindow(IWindowImpl):
class FMainWindow(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()
        self.msgWorker = QTInvokeQueueWorker(self)
        self.msgWorker.start()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnTestA.clicked.connect(self.btnTestAClicked)
        self.uiObj.btnTestB.clicked.connect(self.btnTestBClicked)
        self.uiObj.btnTestC.clicked.connect(self.btnTestCClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_MainWindow()

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        self.uiObj.txtContent.setText(uiArgs.content)

    '''
        按钮A
    '''
    def btnTestAClicked(self, e):
        self.invokeUI(QTObjectInvokeArgs("aaaaaaaaaaaaaaaa"))

    '''
        按钮B
    '''
    def btnTestBClicked(self, e):
        self.invokeUI(QTObjectInvokeArgs("bbbbbbbbbbbbbbb"))

    '''
        按钮C
    '''
    def btnTestCClicked(self, e):
        self.msgWorker.addMsg(QTObjectInvokeArgs(datetime.datetime.now().__str__()))
