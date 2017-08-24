# coding = utf-8
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QListWidget, \
    QInputDialog, QLineEdit, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
from app.model import Users
from app.global_list import *
import functools
from enum import Enum, auto, unique


@unique
class EventType(Enum):
    NORMAL_EVENT = auto()
    TARGET_EVENT = auto()
    VOTE_EVENT = auto()
    SHERIFF_EVENT = auto()
    DEAD_EVENT = auto()


MAIN_WIN = None
CLICK_EVENT = EventType.NORMAL_EVENT
EVENT = None
ROUND_VOTE = {}


def change_click_event(event_type: EventType):
    global CLICK_EVENT
    CLICK_EVENT = event_type


def change_event(event: tuple):
    global EVENT
    EVENT = event


def clear_event():
    global EVENT
    EVENT = None


def add_vote(mid, vote):
    global ROUND_VOTE
    if ROUND_VOTE.get(mid):
        ROUND_VOTE[mid].append(vote)
    else:
        ROUND_VOTE[mid] = [vote]


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
            btn.setStyleSheet(get_role_style('未知'))

        def set_btn_menu(btn):
            def create_menu():
                btn.setContextMenuPolicy(Qt.CustomContextMenu)
                btn.customContextMenuRequested.connect(show_menu)
                btn.right_menu = QMenu(self)
                for role in get_role_type():
                    action = btn.right_menu.addAction(role)
                    action.triggered.connect(change_role)

            def show_menu():
                btn.right_menu.exec_(QCursor().pos())

            def change_role():
                sender = btn.sender()
                player_id = button_to_mid(btn)
                player = get_user_db(player_id)
                player.role = sender.text()
                btn.setStyleSheet(return_style(player_id))
                if button_to_mid(btn) == get_now_player():
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
            btn.setStyleSheet('')
            btn.setFlat(True)
            lab.hide()

        # Init USER_DB
        clear_user_db()
        for mid in range(get_total_player()):
            Users(mid + 1, '未知')

        # Set all player icon,menu and connect button function
        for mid in range(get_total_player()):
            button = "playerButton_" + str(mid + 1)
            label = "playerLabel_" + str(mid + 1)
            player_button = self.__dict__.get(button)
            player_label = self.__dict__.get(label)
            if player_button and player_label:
                btn_lab_enabled(player_button, player_label)
                player_button.disconnect()
                player_button.clicked.connect(self.click_player_button)
                set_btn_menu(player_button)
                set_button_icon(player_button)

        # hide not use player widget
        for mid in range(get_total_player(), 12):
            button = "playerButton_" + str(mid + 1)
            label = "playerLabel_" + str(mid + 1)
            player_button = self.__dict__.get(button)
            player_label = self.__dict__.get(label)
            if player_button and player_label:
                btn_lab_disabled(player_button, player_label)

    def click_player_button(self):
        if CLICK_EVENT == EventType.NORMAL_EVENT:
            sender = self.sender()
            now_player = get_now_player()

            if now_player != 0:
                player = "playerButton_" + str(now_player)
                style = return_style(now_player)
                if style:
                    self.__dict__[player].setStyleSheet(style)
            mid = button_to_mid(sender)
            set_now_player(mid)

            style = return_style(mid)
            if style:
                style_sheet = style + 'border-width:12;'
                sender.setStyleSheet(style_sheet)
            self.update_player_info(mid)
        else:
            self.toolbar_act()

    def cancel_target(self):
        change_click_event(EventType.NORMAL_EVENT)
        clear_event()
        self.unsetCursor()

    def mouseReleaseEvent(self, *args, **kwargs):
        self.cancel_target()

    def update_player_info(self, mid: int):
        user = get_user_db(mid)

        def update_record_list():
            self.recordList.clear()
            for act, obj in user.act_record:
                self.recordList.addItem(str(mid) + "号" + " " + act + " " + str(obj) + "号")

        def update_info_list():
            self.infoList.clear()
            info = user.info
            for name, value in info.items():
                self.infoList.addItem(name + str(value))

        update_info_list()
        update_record_list()

    def init_tool_bar(self):
        def check_player(fun):
            @functools.wraps(fun)
            def wrapper():
                if get_now_player() != 0:
                    self.setCursor(Qt.CrossCursor)
                    fun()

            return wrapper

        @check_player
        def click_sheriff():
            change_click_event(EventType.SHERIFF_EVENT)
            change_event(('警长', ''))

        @check_player
        def click_strong_support():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('明捞', '被明捞'))

        @check_player
        def click_weak_support():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('暗捞', '被暗捞'))

        @check_player
        def click_strong_against():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('重踩', '被重踩'))

        @check_player
        def click_weak_against():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('轻踩', '被轻踩'))

        @check_player
        def click_vote():
            change_click_event(EventType.VOTE_EVENT)
            change_event(('收到投票', '投票给'))

        @check_player
        def click_dead():
            change_click_event(EventType.DEAD_EVENT)
            change_event((dead,))

        def create_action(icon, desc):
            return QAction(QIcon(icon), desc, self.toolBar)

        def triggered_connect(*args):
            for tri, con in args:
                tri.triggered.connect(con)

        def toolbar_add_actions(*args):
            for act in args:
                self.toolBar.addAction(act)

        sheriff = create_action(':/img/警长', '设置选择玩家为警长')
        strong_support = create_action(':/img/明捞', '选择当前玩家的明捞对象')
        weak_support = create_action(':/img/暗捞', '选择当前玩家的暗捞对象')
        weak_against = create_action(':/img/轻踩', '选择当前玩家的轻踩对象')
        strong_against = create_action(':/img/重踩', '选择当前玩家的重踩对象')
        vote = create_action(':/img/投票', '选择给当前玩家投票的对象')
        dead = create_action(':/img/死亡', '选择死亡玩家')

        triggered_connect((sheriff, click_sheriff),
                          (strong_support, click_strong_support),
                          (weak_support, click_weak_support),
                          (weak_against, click_weak_against),
                          (strong_against, click_strong_against),
                          (vote, click_vote),
                          (dead, click_dead))

        toolbar_add_actions(sheriff, strong_support, weak_support,
                            weak_against, strong_against, vote,
                            dead)

    def toolbar_act(self):
        now_player = get_now_player()
        sender = get_user_db(now_player)
        btn = self.sender()
        recipient = get_user_db(button_to_mid(btn))
        if sender.dead[0] or (recipient.dead[0] and CLICK_EVENT is not EventType.DEAD_EVENT):
            self.cancel_target()
            print("no")
            return

        if CLICK_EVENT is EventType.TARGET_EVENT:
            sender.add_act_record(EVENT[0], recipient)
            self.update_player_info(now_player)

        elif CLICK_EVENT is EventType.VOTE_EVENT:
            if sender.id == recipient.id:
                self.cancel_target()
                return
            sender.add_act_record(EVENT[0], recipient)
            recipient.add_act_record(EVENT[1], sender)
            recipient.add_vote(sender.id)
            add_vote(sender.id, recipient.id)
            self.update_player_info(now_player)

        elif CLICK_EVENT is EventType.SHERIFF_EVENT:
            lab = self.__dict__['playerLabel_' + str(recipient.id)]
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
            self.cancel_target()

        elif CLICK_EVENT is EventType.DEAD_EVENT:
            tool = EVENT[0]

            def create_menu():
                tool.menu = QMenu(self)
                for dead in DEAD_TYPE:
                    action = tool.menu.addAction(dead)
                    action.triggered.connect(change_dead)
                show_menu()

            def show_menu():
                tool.menu.exec_(QCursor().pos())

            def change_dead():
                dead_type = self.sender().text()
                recipient.dead = True, dead_type
                btn.setStyleSheet()

            create_menu()

    def open_new_game(self):
        new_game = ControlGameSetForm()
        new_game.show()
        self.hide()


class ControlGameSetForm(QWidget, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)
        self.total_player = get_total_player()
        self.select_role = get_role_type()[:]
        self.all_role = [role for role in get_all_role() if role not in self.select_role]
        self.init_button_connect()
        self.init_role_list()

    def init_button_connect(self):
        def change_spinbox():
            self.total_player = self.totalSetSpinBox.value()

        def click_default_button():
            self.select_role = get_role_type()[:]
            self.all_role = [role for role in get_all_role() if role not in get_role_type()]
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
                    add_all_role(text)
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
        set_total_player(self.total_player)
        set_role_type(self.select_role[:])
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


def return_style(user_id):
    player_style = get_role_style(get_user_db(user_id).role
                                  if get_user_db(user_id)
                                  else None)
    if not player_style:
        player_style = get_role_style('自定义')
    return player_style


def button_to_mid(button):
    return int(button.objectName().split('_')[1])


def lab_to_mid(label):
    return int(label.objectName().split('_')[1])
