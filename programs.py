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

'''
    启动类
'''
class Program:
    '''
        启动函数，类似于C#中的Program.Main(命令行参数)
    '''
    def main(args):
        #创建窗体        
        windowThread,uiDefine,eventObj = EventMainWindowImpl.buildWindowM(None,EventMainWindowImpl())
        #窗体显示
        windowThread.show()
