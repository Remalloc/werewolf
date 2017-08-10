# coding = utf-8
from PyQt5 import QtWidgets
from gui.main_window import Ui_MainWindow


class ControlMainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow,self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window=ControlMainWindow()
    main_window.show()
    sys.exit(app.exec_())