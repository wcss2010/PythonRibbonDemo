#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uievents.awindowbase import *
from uidefines.Ui_MainWindow import *
from uievents.eventsplashwindow import *
from uievents.ribbonwidgets import *
from uievents.ribbonwidgets.ribbonbutton import RibbonButton
from uidefines.Icons import get_icon
from uievents.ribbonwidgets.ribbontextbox import RibbonTextbox
from uievents.ribbonwidgets.ribbonwidget import *
import os
import sys
import pathlib
import datetime

class FRibbonWindowBase(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initUI()
        self.msgWorker = QTInvokeQueueWorker(self)
        self.msgWorker.start()

    '''
        获得窗体基本信息
    '''
    def getWIndowInfo(self):
        return 'xxx软件', 1280, 800, 'icon'

    '''
        初始化界面
    '''
    def initUI(self):
        self.ribbonTabDict = {}
        #初始化基本信息
        wName, wWidth, wHeight, iName = self.getWIndowInfo()
        #self.windowObj.resize(wWidth, wHeight)
        self.windowObj.setFixedWidth(wWidth)
        self.windowObj.setFixedHeight(wHeight)
        self.windowObj.setWindowTitle(wName)
        self.windowObj.setDockNestingEnabled(True)
        self.windowObj.setWindowIcon(get_icon(iName))
        #初始化基本架构
        self.uiObj._ribbon = RibbonWidget(self)
        self.windowObj.addToolBar(self.uiObj._ribbon)
        self.initRibbonUI()

    '''
        初始化Ribbon界面
    '''
    def initRibbonUI(self):
        pass

    '''
        添加动作
    '''
    def add_action(self, caption, icon_name, status_tip, icon_visible, connection, shortcut=None):
        action = QAction(get_icon(icon_name), caption, self)
        action.setStatusTip(status_tip)
        action.triggered.connect(connection)
        action.setIconVisibleInMenu(icon_visible)
        if shortcut is not None:
            action.setShortcuts(shortcut)
        self.windowObj.addAction(action)
        return action

    '''
        创建子菜单
    '''
    def buildSubMenuPanel(self, menuName, subTitle):
        home_tab = None
        if self.ribbonTabDict.__contains__(menuName) == True:
            home_tab = self.ribbonTabDict.get(menuName)
        else:
            home_tab = self.uiObj._ribbon.add_ribbon_tab(menuName)
            self.ribbonTabDict[menuName] = home_tab
        jm_pane = home_tab.add_ribbon_pane(subTitle)
        return jm_pane

    '''
        创建子菜单
    '''
    def buildSubMenu(self, menuName, subTitle, actions):
        jm_pane = self.buildSubMenuPanel(menuName, subTitle)
        for k, v in actions.items():
            tempDelegate = QActionClickedDelegate(menuName, k, self)
            tButton = RibbonButton(self, self.add_action(k, v, k, True, tempDelegate.on_action_click, None), True)
            tButton.tempDelegate = tempDelegate
            jm_pane.add_ribbon_widget(tButton)

    '''
        创建Dock控件
    '''
    def buildDockWidget(self, QTDockWidgetArea, widgetNameEN, widgetNameCN, widget):
        dockWidget = QDockWidget(self)
        dockWidget.setObjectName(widgetNameEN)
        dockWidget.setWindowTitle(widgetNameCN)
        dockWidget.setWidget(widget)
        self.windowObj.addDockWidget(QTDockWidgetArea, dockWidget)
        return dockWidget

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_MainWindow()

    '''
        InvokeUI的实现(用于跨线程操作UI内容)
    '''
    def runUIImpl(self, uiArgs):
        pass

    '''
        执行动作事件
    '''
    def processAction(self, panelName, actionName):
        pass

'''
    菜单项事件类
'''
class QActionClickedDelegate(object):
    def __init__(self, pName, aName, wObj):
        super().__init__()
        self.panelName = pName
        self.actionName = aName
        self.windowObj = wObj

    def on_action_click(self):
        self.windowObj.processAction(self.panelName, self.actionName)
