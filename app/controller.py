# coding = utf-8
from PyQt5 import QtWidgets, QtCore
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
import app.global_list


class ControlMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)

        total_player = app.global_list.TOTAL_PLAYER
        for mid in range(total_player):
            player = "playerButton_" + str(mid + 1)
            if self.__dict__.get(player):
                self.__dict__[player].clicked.connect(self.click_player_button)

    def click_player_button(self):
        sender = self.sender()
        now_player = app.global_list.NOW_PLAYER

        def return_style(user_id):
            user_db = app.global_list.USER_DB
            player_style = app.global_list.ROLE_STYLE.get(user_db.get(user_id).get_set_role()
                                                          if user_db.get(user_id)
                                                          else None)
            return player_style

        if now_player != 0:
            player = "playerButton_" + str(now_player)
            style = return_style(now_player)
            if style:
                self.__dict__[player].setStyleSheet(style)
        mid = int(sender.objectName().split('_')[1])
        app.global_list.set_now_player(mid)

        style = return_style(mid)
        if style:
            style_sheet = style + 'border-width:12;'
            sender.setStyleSheet(style_sheet)

        self.statusBar().showMessage(str(mid) + ' was clicked!')
        self.change_list_widget(mid)

    def change_list_widget(self, mid: int):
        user = app.global_list.USER_DB.get(mid)

        self.listWidget.clear()
        if user:
            print(mid, user.get_act_record())
            for act, obj in user.get_act_record():
                self.listWidget.addItem(str(mid) + " " + act + " " + str(obj))


class ControlGameSetForm(QtWidgets.QMainWindow, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)

        app.global_list.TOTAL_PLAYER = self.totalSetSpinBox.value()
