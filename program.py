#-*- coding:utf-8 -*-
#
#  程序入口文件
#
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic.properties import QtGui
from uiUtil.globaltool import *
from uiUtil.envs import *

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
        app = QApplication(args)
        MainWindow = QMainWindow()
        ui = UI描述类()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())





#下面这段是启动代码，绝对不能删除！！！
if __name__ == '__main__':
    #调用Program类中的main函数，启动程序
    Program.main(sys.argv)