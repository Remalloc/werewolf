# coding = utf-8
from app.controller import *
import app.global_list
import gui.img


def set_button_icon(btn):
    btn.setText('')
    btn.setStyleSheet(app.global_list.DEFAULT_STYLE)


def init_win(window: ControlMainWindow):
    set_button_icon(window.playerButton_1)


if __name__ == '__main__':
    import sys

    app.global_list.TOTAL_PLAYER=4
    win = QtWidgets.QApplication(sys.argv)
    main_win = ControlMainWindow()
    main_win.show()
    init_win(main_win)
    sys.exit(win.exec_())
