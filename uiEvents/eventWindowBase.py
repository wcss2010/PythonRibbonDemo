#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
import os
import sys
import pathlib

'''
    这是窗体的事件抽象类(类似于C#中的Form类,而uiDefines中的Ui_MainWindow.py则类似于form.designer.cs)
'''
class IEventWindow(object):
    '''
        窗体初始化
    '''
    def initWindow(self,appObj,mainWindowThread,mainUIDefine):
        #保存引用
        #Application对象
        self.applicationObj = appObj
        #主窗体线程
        self.mainWindowObj = mainWindowThread
        #窗体定义类
        self.mainUIDefineObj = mainUIDefine
        #初始化所有数据
        self.initUIAndData()

    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        pass

    '''
        创建窗体线程并进行配置
    '''
    def buildWindow(app,parent,ui,event):
        if app != None and ui != None and event != None:
            #创建窗体线程
            windowThread = QMainWindow(parent)
            #初始化窗体事件类
            event.initWindow(app,windowThread,ui)
            #设置描述类到窗体线程
            ui.setupUi(windowThread)
            #返回对象
            return windowThread,ui,event
        else:
            return None,None,None