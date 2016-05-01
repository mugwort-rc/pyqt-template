# -*- coding: utf-8 -*-

from qt import QMainWindow

from ui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
