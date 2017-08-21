# coding = utf-8
from app.controller import ControlMainWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    import sys

    win = QApplication(sys.argv)
    main_win = ControlMainWindow()
    main_win.show()
    sys.exit(win.exec_())
