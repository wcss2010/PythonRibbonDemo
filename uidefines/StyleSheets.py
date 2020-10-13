from uidefines.Icons import *

__author__ = 'magnus'

stylesheet_instance = None

def get_stylesheet(name):
    global stylesheet_instance
    if not stylesheet_instance:
        stylesheet_instance = Stylesheets()
    return stylesheet_instance.get_stylesheet(name)

class Stylesheets(object):
    def __init__(self):
        self._stylesheets = {}
        self.make_stylesheet("main", Icons.makeIconPath("stylesheets/main.css"))
        self.make_stylesheet("ribbon", Icons.makeIconPath("stylesheets/ribbon.css"))
        self.make_stylesheet("ribbonPane", Icons.makeIconPath("stylesheets/ribbonPane.css"))
        self.make_stylesheet("ribbonButton", Icons.makeIconPath("stylesheets/ribbonButton.css"))
        self.make_stylesheet("ribbonSmallButton", Icons.makeIconPath("stylesheets/ribbonSmallButton.css"))

    def make_stylesheet(self, name, path):
        with open(path) as data_file:
            stylesheet = data_file.read()

        self._stylesheets[name] = stylesheet

    def get_stylesheet(self, name):
        stylesheet = ""
        try:
            stylesheet = self._stylesheets[name]
        except KeyError:
            print("stylesheet " + name + " not found")
        return stylesheet
