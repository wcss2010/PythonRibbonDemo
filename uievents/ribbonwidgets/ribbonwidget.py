from PyQt5.QtWidgets import *

from uievents.ribbonwidgets.ribbontab import RibbonTab

from uievents.ribbonwidgets import gui_scale
from uidefines.StyleSheets import get_stylesheet
__author__ = 'magnus'


class RibbonWidget(QToolBar):
    def __init__(self, parent):
        QToolBar.__init__(self, parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(120*gui_scale())
        self._ribbon_widget.setMinimumHeight(110*gui_scale())
        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

    def clearAll(self):
        self._ribbon_widget.clear()

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        ribbon_tab.setObjectName("tab_" + name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab

    def set_active(self, name):
        self.setCurrentWidget(self.findChild("tab_" + name))