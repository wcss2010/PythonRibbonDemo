#-*- coding:utf-8 -*-
#
#  程序入口文件
#
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from uiUtil.globaltool import *
from uiUtil.envs import *
from uiDefines import *
from uiEvents import *

'''
    启动类
'''
class Program:
    '''
        启动函数，类似于C#中的Program.Main(命令行参数)
    '''
    def main(args):
        #创建目录以及载入配置
        cfenv.initEnvData()        
        #启动程序
        #创建QT的Application对象
        app = QApplication(args)
        #创建窗体线程
        MainWindow = QMainWindow()
        #创建窗体描述类(类似于C#中的form.designer.cs)
        ui = Ui_MainWindow()
        #创建窗体事件类(类似于C#中的form.cs)
        uiEvent = EventMainWindowImpl()
        #初始化窗体事件类
        uiEvent.initWindow(MainWindow,ui)
        #设置描述类到窗体线程
        ui.setupUi(MainWindow)
        #窗体显示(阻塞)
        MainWindow.show()
        #退出程序
        sys.exit(app.exec_())





#下面这段是启动代码，绝对不能删除！！！
if __name__ == '__main__':
    #调用Program类中的main函数，启动程序
    Program.main(sys.argv)