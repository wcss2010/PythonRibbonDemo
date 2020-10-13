from PyQt5.QtGui import *
import os
import pathlib
from uiutil.envs import *

__author__ = 'magnus'

icons_instance = None

def get_icon(name):
    global icons_instance
    if not icons_instance:
        icons_instance = Icons()
    return icons_instance.icon(name)

class Icons(object):
    def __init__(self):
        self._icons = {}        
        self.make_icon("icon",  Icons.makeIconPath("icons/icon.png"))
        self.make_icon("default", Icons.makeIconPath("icons/folder.png"))

    def makeIconPath(subPath):
        return os.path.join(CFEnv.dataDir, subPath)

    def make_icon(self, name, path):
        icon = QIcon()
        icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self._icons[name] = icon

    def icon(self, name):
        icon = self._icons["default"]
        if self._icons.__contains__(name) == True:
            try:
                icon = self._icons[name]
            except KeyError:
                print("icon " + name + " not found")
        else:
            imgPath =  Icons.makeIconPath(os.path.join('icons', name.split('-')[0], name.split('-')[1] + '.ico'))
            if pathlib.Path(imgPath).exists():
                print(imgPath)
                self.make_icon(name, imgPath)
                try:
                    icon = self._icons[name]
                except KeyError:
                    print("icon " + name + " not found")
        return icon
