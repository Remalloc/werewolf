# coding = utf-8
from app.controller import *
from PyQt5.QtWidgets import QApplication
import app.global_list
import gui.img


def set_button_icon(btn):
    btn.setStyleSheet(app.global_list.ROLE_STYLE.get('未知'))


def init_win(window: ControlMainWindow):

    for mid in range(app.global_list.TOTAL_PLAYER):
        player = "playerButton_" + str(mid + 1)
        if window.__dict__.get(player):
            set_button_icon(window.__dict__[player])


if __name__ == '__main__':
    import sys

    win = QApplication(sys.argv)
    main_win = ControlMainWindow()
    main_win.show()
    init_win(main_win)

    sys.exit(win.exec_())
