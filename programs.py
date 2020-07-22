#-*- coding:utf-8 -*-
#
#  程序启动类
#
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from uiUtil.globaltool import *
from uiUtil.envs import *
from uiDefines import *
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

        #创建窗体
        windowThread,uiDefine,eventObj = IWindowEvents.buildWindowM(None,EventMainWindowImpl())
        #窗体显示
        windowThread.show()
