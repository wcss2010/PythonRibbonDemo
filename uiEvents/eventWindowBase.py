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
    def initWindow(self,mainWindowThread,mainUIDefine):
        #保存引用
        #主窗体线程
        self.mainWindowThread = mainWindowThread
        #窗体定义类
        self.mainUI = mainUIDefine
        #初始化所有数据
        self.initUIAndData()

    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        pass