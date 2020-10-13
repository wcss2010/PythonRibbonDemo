#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uievents.awindowbase import *
from uievents.fribbonwindow import *
from uievents.eventsplashwindow import *
from PyQt5.QtCore import Qt
from uiutil.envs import *
import os
import sys
import pathlib
import datetime

'''
    这是MainWindow窗体的实现类
'''
class FMainWindow(FRibbonWindowBase):
    '''
        获得窗体基本信息
    '''
    def getWIndowInfo(self):
        return 'xxx软件', 1280, 800, 'icon'

    '''
        初始化Ribbon界面
    '''
    def initRibbonUI(self):
        #-----初始化Tree
        self.uiObj._tree_widget = QTreeWidget(self)
        # self.uiObj._tree_widget.setHeaderHidden(True)
        self.uiObj._tree_widget.setHeaderLabel('树标题')
        self.uiObj._tree_widget.clear()
        #设置根节点
        root = QTreeWidgetItem(self.uiObj._tree_widget)
        root.setText(0, '根节点')
        #设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, '子节点1')
        child1.setCheckState(0, Qt.Checked)
        root.addChild(child1)
        #设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        #设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点3')
        #加载根节点的所有属性与子控件
        self.uiObj._tree_widget.addTopLevelItem(root)
        #为TreeWidget创建一个DockWidget容器
        treeDockWidget = self.buildDockWidget(Qt.LeftDockWidgetArea, 'TreeDock', '目录树', self.uiObj._tree_widget)
        #设置DockWidget的宽度
        treeDockWidget.setFixedWidth(300)
        #------初始化显示Label
        self.uiObj._label_widget = QLabel('', self)
        labelDockWidget = self.buildDockWidget(Qt.RightDockWidgetArea, 'ContentDock', '工作区', self.uiObj._label_widget)
        labelDockWidget.setFixedWidth(1280 - 310)
        #------初始化菜单
        kvv = {}
        kvv['新建'] = '文件-新建'
        kvv['打开'] = '文件-打开'
        kvv['关闭所有'] = '文件-关闭所有'
        kvv['最近访问'] = '文件-最近访问'
        kvv['查找'] = '文件-查找'
        kvv['帮助'] = '文件-帮助'
        self.buildSubMenu('文件', '', kvv)

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        pass

    '''
        执行动作事件
    '''
    def processAction(self, panelName, actionName):
        print(panelName + ',' + actionName)
        #self.uiObj._label_widget.setText(panelName + ',' + actionName)
        #拼装路径
        imgPath = os.path.join(CFEnv.dataDir, 'bgImages', panelName, actionName + '.png')
        print(imgPath)
        if pathlib.Path(imgPath).exists():
            #显示Gif的方法如下：
            #self.gif = QMovie('qq.gif')
            #self.labelWidget.setMovie(self.gif)
            #self.gif.start()
            #显示一般图片
            pixmap = QPixmap(imgPath)
            laSize = self.uiObj._label_widget.size()
            scaredPixmap = pixmap.scaled(laSize, Qt.IgnoreAspectRatio)
            self.uiObj._label_widget.setPixmap(scaredPixmap)
