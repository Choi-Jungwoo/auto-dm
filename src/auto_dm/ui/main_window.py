import os.path

from PyQt5 import QtWidgets, uic

UI_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'resources', 'main.ui')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(UI_FILE_PATH, self)
