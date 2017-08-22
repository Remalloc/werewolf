# coding = utf-8
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QListWidget, \
    QInputDialog, QLineEdit, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
from app.model import Users
import app.global_list

MAIN_WIN = None
NORMAL_EVENT = 1
TARGET_EVENT = 2
CLICK_EVENT = NORMAL_EVENT
EVENT = None


def change_click_event(event_type):
    global CLICK_EVENT
    CLICK_EVENT = event_type


def change_event(event):
    global EVENT
    EVENT = event


class ControlMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)
        global MAIN_WIN
        MAIN_WIN = self
        self.init_player()
        self.init_tool_bar()
        self.newGame.triggered.connect(self.open_new_game)

    def init_player(self):
        def set_button_icon(btn):
            btn.setStyleSheet(app.global_list.ROLE_STYLE.get('未知'))

        def set_btn_menu(btn):
            def create_menu():
                btn.setContextMenuPolicy(Qt.CustomContextMenu)
                btn.customContextMenuRequested.connect(show_menu)
                btn.right_menu = QMenu(self)
                for role in app.global_list.ROLE_TYPE_LIST:
                    action = btn.right_menu.addAction(role)
                    action.triggered.connect(change_role)

            def show_menu():
                btn.right_menu.exec_(QCursor().pos())

            def change_role():
                sender = btn.sender()
                player_id = button_to_mid(btn)
                player = app.global_list.USER_DB.get(player_id)
                player.get_set_role(sender.text())
                btn.setStyleSheet(return_style(player_id))
                if button_to_mid(btn) == app.global_list.NOW_PLAYER:
                    btn.clicked.emit()

            create_menu()

        def btn_lab_enabled(btn, lab):
            btn.setEnabled(True)
            lab.setEnabled(True)
            btn.setFlat(False)
            lab.show()

        def btn_lab_disabled(btn, lab):
            btn.setEnabled(False)
            lab.setEnabled(False)
            btn.setFlat(True)
            lab.hide()

        # init USER_DB
        app.global_list.USER_DB.clear()
        for mid in range(app.global_list.TOTAL_PLAYER):
            Users(mid + 1, '未知')

        # set all player icon,menu and connect button function
        for mid in range(app.global_list.TOTAL_PLAYER):
            button = "playerButton_" + str(mid + 1)
            label = "playerLabel_" + str(mid + 1)
            player_button = self.__dict__.get(button)
            player_label = self.__dict__.get(label)
            if player_button and player_label:
                btn_lab_enabled(player_button, player_label)
                player_button.disconnect()
                player_button.clicked.connect(self.click_player_button)
                player_button.clicked.connect(self.click_target_player)
                set_btn_menu(player_button)
                set_button_icon(player_button)

        # hide not use player widget
        for mid in range(app.global_list.TOTAL_PLAYER, 12):
            button = "playerButton_" + str(mid + 1)
            label = "playerLabel_" + str(mid + 1)
            player_button = self.__dict__.get(button)
            player_label = self.__dict__.get(label)
            if player_button and player_label:
                btn_lab_disabled(player_button, player_label)

    def click_player_button(self):
        if CLICK_EVENT == NORMAL_EVENT:
            sender = self.sender()
            now_player = app.global_list.NOW_PLAYER

            if now_player != 0:
                player = "playerButton_" + str(now_player)
                style = return_style(now_player)
                if style:
                    self.__dict__[player].setStyleSheet(style)
            mid = button_to_mid(sender)
            app.global_list.set_now_player(mid)

            style = return_style(mid)
            if style:
                style_sheet = style + 'border-width:12;'
                sender.setStyleSheet(style_sheet)

            self.update_player_info(mid)

    def click_target_player(self):
        if CLICK_EVENT == TARGET_EVENT:
            user_db = app.global_list.USER_DB
            now_player = app.global_list.NOW_PLAYER
            player = user_db.get(now_player)
            target_player = user_db.get(button_to_mid(self.sender()))

            player.add_act_record(EVENT, target_player)
            self.update_player_info(now_player)
            self.cancel_target()

    def cancel_target(self):
        change_click_event(NORMAL_EVENT)
        change_event(None)
        self.unsetCursor()

    def mouseReleaseEvent(self, *args, **kwargs):
        self.cancel_target()

    def update_player_info(self, mid: int):
        user = app.global_list.USER_DB.get(mid)

        def update_record_list():
            self.recordList.clear()
            for act, obj in user.get_act_record():
                self.recordList.addItem(str(mid) + "号" + " " + act + " " + str(obj) + "号")

        def update_info_list():
            self.infoList.clear()
            info = user.get_info()
            for name, value in info.items():
                self.infoList.addItem(name + str(value))

        update_info_list()
        update_record_list()

    def init_tool_bar(self):
        def click_sheriff():
            now_player = app.global_list.NOW_PLAYER
            if now_player != 0:
                lab = self.__dict__['playerLabel_' + str(now_player)]
                sheriff_lab = str(lab_to_mid(lab)) + "号" + " (警长)"
                if self.__dict__.get('sheriff'):
                    default_lab = str(lab_to_mid(self.sheriff)) + "号"
                    if lab == self.sheriff:
                        lab.setText(default_lab)
                        self.sheriff = None
                    else:
                        self.sheriff.setText(default_lab)
                        lab.setText(sheriff_lab)
                        self.sheriff = lab
                else:
                    lab.setText(sheriff_lab)
                    self.sheriff = lab

        def check_player():
            now_player = app.global_list.NOW_PLAYER
            if now_player != 0:
                self.setCursor(Qt.CrossCursor)
                change_click_event(TARGET_EVENT)
                return True
            return False

        def click_strong_support():
            if check_player():
                change_event('明捞')

        def click_weak_support():
            if check_player():
                change_event('暗捞')

        def click_strong_against():
            if check_player():
                change_event('重踩')

        def click_weak_against():
            if check_player():
                change_event('轻踩')

        sheriff = QAction(QIcon(':/img/警长'), '设置选择玩家为警长', self.toolBar)
        strong_support = QAction(QIcon(':/img/明捞'), '选择当前玩家的明捞对象', self.toolBar)
        weak_support=QAction(QIcon(':/img/暗捞'), '选择当前玩家的暗捞对象', self.toolBar)
        weak_against = QAction(QIcon(':/img/轻踩'), '选择当前玩家的轻踩对象', self.toolBar)
        strong_against=QAction(QIcon(':/img/重踩'), '选择当前玩家的重踩对象', self.toolBar)

        sheriff.triggered.connect(click_sheriff)
        strong_support.triggered.connect(click_strong_support)
        weak_support.triggered.connect(click_weak_support)
        weak_against.triggered.connect(click_weak_against)
        strong_against.triggered.connect(click_strong_against)

        self.toolBar.addAction(sheriff)
        self.toolBar.addAction(strong_support)
        self.toolBar.addAction(weak_support)
        self.toolBar.addAction(weak_against)
        self.toolBar.addAction(strong_against)

    def open_new_game(self):
        new_game = ControlGameSetForm()
        new_game.show()
        self.hide()


def return_style(user_id):
    user_db = app.global_list.USER_DB
    player_style = app.global_list.ROLE_STYLE.get(user_db.get(user_id).get_set_role()
                                                  if user_db.get(user_id)
                                                  else None)
    if not player_style:
        player_style = app.global_list.ROLE_STYLE.get('自定义')
    return player_style


def button_to_mid(button):
    return int(button.objectName().split('_')[1])


def lab_to_mid(label):
    return int(label.objectName().split('_')[1])


class ControlGameSetForm(QWidget, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)
        self.total_player = app.global_list.TOTAL_PLAYER
        self.select_role = app.global_list.ROLE_TYPE_LIST[:]
        self.all_role = [role for role in app.global_list.ALL_ROLE if not role in self.select_role]
        self.init_button_connect()
        self.init_role_list()

    def init_button_connect(self):
        def change_spinbox():
            self.total_player = self.totalSetSpinBox.value()

        def click_default_button():
            self.select_role = app.global_list.ROLE_TYPE_LIST[:]
            self.all_role = [role for role in app.global_list.ALL_ROLE if role not in app.global_list.ROLE_TYPE_LIST]
            self.update_data()

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
            text, flag = QInputDialog.getText(self, "添加自定义角色", "角色名字(不能为空且长度小于15)：",
                                              QLineEdit.Normal)
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
            self.totalSetSpinBox.setValue(value if value in range(min_value - 1, max_value + 1) else min_value)

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
        self.total_player = self.totalSetSpinBox.value()
        app.global_list.TOTAL_PLAYER = self.total_player
        app.global_list.ROLE_TYPE_LIST = self.select_role[:]
        return True

    def closeEvent(self, close_event):
        flag = True
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
                flag = False

        if MAIN_WIN and flag:
            MAIN_WIN.init_player()
            MAIN_WIN.show()
