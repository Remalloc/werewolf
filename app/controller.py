# coding = utf-8
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QListWidget
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
import app.global_list

main_win = None


class ControlMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)
        global main_win
        main_win = self
        self.new_game = ControlGameSetForm()
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
        self.add_roles = []
        self.init_role_list()
        self.init_button_connect()

    def init_button_connect(self):
        def click_default_button():
            self.allRoleList.clear()
            self.init_all_role_list()
            self.select_role.clear()

        def click_determine_button():
            if not self.save_option():
                msg = QMessageBox()
                msg.setWindowTitle('设置错误')
                msg.setText('没有选择玩家类型！')
                msg.setIcon(QMessageBox.Information)
                msg.addButton('确定', QMessageBox.YesRole)
                msg.exec()
            else:
                self.close()

        def click_right_button():
            role_list = self.allRoleList.selectedItems()
            for item in role_list:
                index = self.allRoleList.row(item)
                item = self.allRoleList.takeItem(index)

                self.select_role.append(item.text())
                self.selectRoleList.addItem(item)
                self.allRoleList.removeItemWidget(item)
            print(self.select_role)

        def click_left_button():
            role_list = self.selectRoleList.selectedItems()
            for item in role_list:
                index = self.selectRoleList.row(item)
                item = self.selectRoleList.takeItem(index)

                self.select_role.remove(item.text())
                self.allRoleList.insertItem(get_all_type_list().index(item.text()), item)
                self.selectRoleList.removeItemWidget(item)
            print(self.select_role)

        self.defaultButton.clicked.connect(click_default_button)
        self.determineButton.clicked.connect(click_determine_button)
        self.rightButton.clicked.connect(click_right_button)
        self.leftButton.clicked.connect(click_left_button)

    def init_role_list(self):
        self.allRoleList.setSelectionMode(QListWidget.MultiSelection)
        self.allRoleList.addItems(get_all_type_list())
        self.selectRoleList.setSelectionMode(QListWidget.MultiSelection)

    def save_option(self):
        if not self.select_role:
            return False
        app.global_list.TOTAL_PLAYER = self.total_player
        app.global_list.ROLE_TYPE_LIST = self.select_role
        return True

    def closeEvent(self, close_event):
        if self.select_role:
            msg = QMessageBox()
            msg.setWindowTitle('保存')
            msg.setText('是否保存设置？')
            msg.setIcon(QMessageBox.Question)
            msg.addButton('确定', QMessageBox.YesRole)
            msg.addButton('取消', QMessageBox.NoRole)
            reply = msg.exec()
            if reply == QMessageBox.YesRole:
                self.save_option()
        if main_win:
            main_win.show()


def get_all_type_list():
    special_role = app.global_list.SPECIAL_ROLE
    result = []
    for key in app.global_list.ROLE_STYLE.keys():
        if key not in special_role:
            result.append(key)
    return result
