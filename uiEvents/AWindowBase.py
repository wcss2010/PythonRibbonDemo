#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiUtil.envs import *
import os
import sys
import pathlib

'''
    这是窗体的事件抽象类(类似于C#中的form.cs类,而uiDefines中的Ui_MainWindow.py则类似于form.designer.cs)
'''
class IWindowEvents(object):
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
        raise NotImplementedError

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        raise NotImplementedError

    '''
        创建窗体线程并进行配置(基于QMainWindow)
        输出参数：QMainWindow,窗体UI定义类,窗体事件抽象类
    '''
    def buildWindowM(parent,event):
        uiDefine = event.getUIDefineObject()
        if cfenv.appObj != None and uiDefine != None and event != None:
            #创建窗体线程
            windowThread = QMainWindow(parent)
            #设置描述类到窗体线程
            uiDefine.setupUi(windowThread)
            #初始化窗体事件类
            event.initWindow(cfenv.appObj,windowThread,uiDefine)
            #返回对象
            return windowThread,ui,event
        else:
            return None,None,None

    '''
        创建窗体线程并进行配置(基于QWidget)
        输出参数：QWidget,窗体UI定义类,窗体事件抽象类
    '''
    def buildWindowW(parent,event):
        uiDefine = event.getUIDefineObject()
        if cfenv.appObj != None and uiDefine != None and event != None:
            #创建窗体线程
            windowThread = QWidget(parent)
            #设置描述类到窗体线程
            uiDefine.setupUi(windowThread)
            #初始化窗体事件类
            event.initWindow(cfenv.appObj,windowThread,uiDefine)
            #返回对象
            return windowThread,ui,event
        else:
            return None,None,None

    '''
        创建窗体线程并进行配置(基于QDialog)
        输出参数：QDialog,窗体UI定义类,窗体事件抽象类
    '''
    def buildWindowD(parent,event):
        uiDefine = event.getUIDefineObject()
        if cfenv.appObj != None and uiDefine != None and event != None:
            #创建窗体线程
            windowThread = QDialog(parent)
            #设置描述类到窗体线程
            uiDefine.setupUi(windowThread)
            #初始化窗体事件类
            event.initWindow(cfenv.appObj,windowThread,uiDefine)
            #返回对象
            return windowThread,ui,event
        else:
            return None,None,None