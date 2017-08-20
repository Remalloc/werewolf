# coding = utf-8
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QListWidget, QInputDialog, QLineEdit
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
        new_game = ControlGameSetForm()
        new_game.show()
        self.hide()


class ControlGameSetForm(QWidget, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)
        self.total_player = app.global_list.TOTAL_PLAYER
        self.select_role = app.global_list.ROLE_TYPE_LIST
        self.all_role = [role for role in app.global_list.ALL_ROLE if not role in self.select_role ]
        self.init_button_connect()
        self.init_role_list()

    def init_button_connect(self):
        def change_spinbox():
            self.total_player=self.totalSetSpinBox.value()

        def click_default_button():
            self.allRoleList.clear()
            self.init_all_role_list()
            self.select_role.clear()

        def click_determine_button():
                self.close()

        def click_right_button():
            role_list = self.allRoleList.selectedItems()
            for item in role_list:
                index = self.allRoleList.row(item)
                item_text = self.allRoleList.takeItem(index).text()
                self.select_role.append(item_text)
                self.all_role.remove(item_text)
            self.update_data()

        def click_left_button():
            role_list = self.selectRoleList.selectedItems()
            for item in role_list:
                index = self.selectRoleList.row(item)
                item_text = self.selectRoleList.takeItem(index).text()
                self.all_role.append(item_text)
                self.select_role.remove(item_text)
            self.update_data()

        def click_add_button():
            text, flag = QInputDialog.getText(self, "添加自定义角色", "角色名字：", QLineEdit.Normal)
            text = text.strip()
            if flag and text != '' and len(text) < 15:
                if text not in self.select_role:
                    self.select_role.append(text)
                    app.global_list.ALL_ROLE.append(text)
                    self.update_data()
            elif flag:
                msg = QMessageBox()
                msg.setWindowTitle("输入错误")
                msg.setText("名字不能为空且长度不能超过15个字符！")
                msg.exec()

        self.totalSetSpinBox.valueChanged.connect(change_spinbox)
        self.defaultButton.clicked.connect(click_default_button)
        self.determineButton.clicked.connect(click_determine_button)
        self.rightButton.clicked.connect(click_right_button)
        self.leftButton.clicked.connect(click_left_button)
        self.addButton.clicked.connect(click_add_button)

    def init_role_list(self):
        self.allRoleList.setSelectionMode(QListWidget.MultiSelection)
        self.selectRoleList.setSelectionMode(QListWidget.MultiSelection)
        self.update_data()

    def update_data(self):
        def update_total():
            value = self.total_player
            min_value = self.totalSetSpinBox.minimum()
            max_value = self.totalSetSpinBox.maximum()
            self.totalSetSpinBox.setValue(value if value in range(min_value - 1, max_value+1) else min_value)

        def update_all_role():
            self.allRoleList.clear()
            self.allRoleList.addItems(self.all_role)

        def update_select_role():
            self.selectRoleList.clear()
            self.selectRoleList.addItems(self.select_role)

        update_total()
        update_all_role()
        update_select_role()

    def save_option(self):
        if not self.select_role:
            return False

        app.global_list.TOTAL_PLAYER = self.total_player
        app.global_list.ROLE_TYPE_LIST = self.select_role
        return True

    def closeEvent(self, close_event):
        flag=True
        msg = QMessageBox()
        msg.setWindowTitle('保存')
        msg.setText('是否保存设置？')
        msg.setIcon(QMessageBox.Question)
        msg.addButton('确定', QMessageBox.YesRole)
        msg.addButton('取消', QMessageBox.NoRole)
        reply = msg.exec()
        if reply == QMessageBox.AcceptRole:
            if not self.save_option():
                msg = QMessageBox()
                msg.setWindowTitle('设置错误')
                msg.setText('没有选择玩家类型！')
                msg.setIcon(QMessageBox.Information)
                msg.addButton('确定', QMessageBox.YesRole)
                msg.exec()
                close_event.ignore()
                flag=False

        if main_win and flag:
            main_win.show()

