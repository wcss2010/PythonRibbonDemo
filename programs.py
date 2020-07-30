#-*- coding:utf-8 -*-
#
#  程序启动类
#
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from uiUtil.globaltool import *
from uiUtil.envs import *
from uiEvents.eventMainWindow import *
from uiEvents.AWindowBase import *

'''
    启动类
'''
class Program:
    '''
        启动函数，类似于C#中的Program.Main(命令行参数)
    '''
    def main(args):
        #打印环境变量
        print("Bin:" + cfenv.binDir)
        print("Data:" + cfenv.dataDir)
        print("Plugin:" + cfenv.pluginDir)
        print("Script:" + cfenv.scriptDir)
        print("ConfigFile:" + cfenv.configFilePath)

        #创建QT的Application对象,每一个pyqt程序中都需要有一个QApplication对象(不可删除!!!!!!!!!)
        cfenv.appObj = QApplication(args)

        #创建窗体
        #mainWindow,uiDefine,eventObj = WindowBuilder.buildWindow(QMainWindow(), FMainWindow())
        mainWindow, uiDefine, eventObj = WindowBuilder.buildWindow(None, FMainWindow())
        #窗体显示
        mainWindow.show()

        #进入程序的主循环，遇到退出情况，终止程序(不可删除!!!!!!!!!)
        sys.exit(cfenv.appObj.exec_())
