# coding = utf-8
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
import app.global_list

main_win = None


class ControlMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)
        self.new_game = ControlGameSetForm()
        global main_win
        main_win = self
        total_player = app.global_list.TOTAL_PLAYER

        for mid in range(total_player):
            player = "playerButton_" + str(mid + 1)
            if self.__dict__.get(player):
                self.__dict__[player].clicked.connect(self.click_player_button)
        self.newGame.triggered.connect(self.open_new_game)

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
        self.update_player_info(mid)

    def update_player_info(self, mid: int):
        user = app.global_list.USER_DB.get(mid)

        def update_record_list():
            self.recordList.clear()
            for act, obj in user.get_act_record():
                self.recordList.addItem(str(mid) + " " + act + " " + str(obj))

        def update_info_list():
            self.infoList.clear()
            info = user.get_info()
            for name, value in info.items():
                self.infoList.addItem(name + str(value))

        update_info_list()
        update_record_list()

    def open_new_game(self):
        self.new_game.show()
        self.hide()


class ControlGameSetForm(QWidget, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)
        self.total_player = self.totalSetSpinBox.value()
        self.select_role = []

        self.determineButton.clicked.connect(self.close)

    def save_option(self):
        if not self.select_role:
            return False
        app.global_list.TOTAL_PLAYER = self.total_player
        app.global_list.ROLE_TYPE_LIST = self.select_role
        return True

    def closeEvent(self, close_event):
        sender = self.sender()
        flag = True
        if sender:
            if not self.save_option():
                msg = QMessageBox()
                msg.setWindowTitle('设置错误')
                msg.setText('没有选择玩家类型！')
                msg.setIcon(QMessageBox.Information)
                msg.addButton('确定', QMessageBox.YesRole)
                msg.exec()
                close_event.ignore()
                flag = False
        elif self.select_role:
            msg = QMessageBox()
            msg.setWindowTitle('保存')
            msg.setText('是否保存设置？')
            msg.setIcon(QMessageBox.Question)
            msg.addButton('确定', QMessageBox.YesRole)
            msg.addButton('取消', QMessageBox.NoRole)
            reply = msg.exec()
            if reply == QMessageBox.YesRole:
                self.save_option()
        if flag and main_win:
            main_win.show()
