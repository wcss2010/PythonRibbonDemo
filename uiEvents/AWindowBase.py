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
    这是窗体的实现类接口
    PyQT中一个窗体的结构如下：
       QMainWindow = C#下的Form
            uiDefines中的ui_MainWidow.py=C#下的xxForm.designer.cs
            uiEvents中eventMainWindow.py=C#下的xxForm.cs
'''
class IWindowImpl:
    '''
        窗体初始化
    '''
    def initWindow(self,appObj,windowObj,uiObj):
        #保存引用
        #Application对象
        self.appObj = appObj
        #主窗体线程
        self.windowObj = windowObj
        #窗体定义类
        self.uiObj = uiObj
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
    基于QMainWindow的窗体的实现类接口
'''
class IWIndowImplM(IWindowImpl,QMainWindow):
    pass

'''
    基于QWidget的窗体的实现类接口
'''
class IWindowImplW(IWindowImpl,QWidget):
    pass

'''
    基于QDialog的窗体的实现类接口
'''
class IWindowImplD(IWindowImpl,QDialog):
    pass

'''
    窗体对象生成器(通过QMainWindow或QWidget或QDialog,结合uiDefines和uiEvent配置窗体对象)
'''
class WindowBuilder:
    '''
        创建窗体对象
        windowObj = QMainWindow或QWidget或QDialog的实例,如果为空则使用eventImpl的值充当窗体对象
        eventImpl = 窗体实现类的实例
        输出参数：QMainWindow或QWidget或QDialog的实例,窗体UI定义类的实例,窗体实现类的实例
    '''
    def buildWindow(windowObj,eventImpl):
        if eventImpl != None:
            uiDefine = eventImpl.getUIDefineObject()
            if cfenv.appObj != None and uiDefine != None and eventImpl != None:
                #设置描述类到窗体线程
                if windowObj != None:
                    uiDefine.setupUi(windowObj)
                else:
                    uiDefine.setupUi(eventImpl)
                #初始化窗体事件类
                if windowObj != None:
                    eventImpl.initWindow(cfenv.appObj,windowObj,uiDefine)
                    #返回对象
                    return windowObj,uiDefine,eventImpl
                else:
                    eventImpl.initWindow(cfenv.appObj,eventImpl,uiDefine)
                    #返回对象
                    return eventImpl,uiDefine,eventImpl
            else:
                return None,None,None
        else:
                return None,None,None
