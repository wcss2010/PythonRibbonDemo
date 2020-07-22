#-*- coding:utf-8 -*-
#
#  Python启动入口
#
import sys

from PyQt5.QtWidgets import QApplication
from uiUtil.globaltool import *
from uiUtil.envs import *
from programs import *

#***************下面这段是启动代码，绝对不能删除！！！也不建议修改***************
if __name__ == '__main__':
    #创建目录以及载入配置(不可删除!!!!!!!!!)
    cfenv.initEnvData()
    #创建QT的Application对象(不可删除!!!!!!!!!)
    cfenv.appObj = QApplication(sys.argv)
    #调用Program类中的main函数，启动程序
    Program.main(sys.argv)
    #退出程序(不可删除!!!!!!!!!)
    sys.exit(cfenv.appObj.exec_())