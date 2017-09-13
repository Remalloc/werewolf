# coding = utf-8
from app.controller import ControlMainWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    import sys

    win = QApplication(sys.argv)
    MAIN_WIN = ControlMainWindow()
    MAIN_WIN.show()
    MAIN_WIN.init_view()
    sys.exit(win.exec_())
