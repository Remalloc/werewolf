# coding = utf-8
from PyQt5 import QtWidgets, QtCore
from gui.main_window import Ui_MainWindow
import app.global_list
from app.model import Users


class ControlMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # _signal_player:(int:player_id 1~12,str:type rightClick,leftClick)
    _signal_player = QtCore.pyqtSignal(int)

    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)

        total_player = app.global_list.TOTAL_PLAYER
        for mid in range(total_player):
            player = "playerButton_" + str(mid + 1)
            if self.__dict__.get(player):
                self.__dict__[player].clicked.connect(self.click_player_button)
                # self._signal_player.connect(self.show_player_record)

    def click_player_button(self):
        sender = self.sender()
        now_player = app.global_list.NOW_PLAYER

        if now_player != 0:
            player = "playerButton_" + str(now_player)
            self.__dict__[player].setChecked(False)
        if not sender.isCheckable():
            sender.setCheckable(True)
        if not sender.isChecked():
            sender.setChecked(True)

        mid = int(sender.objectName().split('_')[1])
        app.global_list.set_now_player(mid)
        self.statusBar().showMessage(str(mid) + ' was clicked!')
        self.change_list_widget(mid)

    def change_list_widget(self, mid: int):
        user = app.global_list.USER_DB.get(mid)

        self.listWidget.clear()
        if user:
            print(mid,user.get_act_record())
            for act,obj in user.get_act_record():
                self.listWidget.addItem(str(mid)+" "+act+" "+str(obj))


if __name__ == "__main__":
    import sys

    app.global_list.TOTAL_PLAYER = 12
    user1=Users(1,"wolf")
    user2=Users(2,"human")
    user1.add_act_record("against",user2)
    user1.add_act_record("support",user2)

    win = QtWidgets.QApplication(sys.argv)
    main_window = ControlMainWindow()
    main_window.show()
    sys.exit(win.exec_())
