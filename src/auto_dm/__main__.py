import sys

from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

from auto_dm.ui.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_pink.xml')
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
