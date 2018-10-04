# coding = utf-8
import functools
from enum import Enum, auto, unique
from operator import itemgetter

from PyQt5.QtWidgets import QWidget, QDialog, QMainWindow, QMessageBox, QListWidget, \
    QInputDialog, QLineEdit, QMenu, QAction, QCheckBox, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QIcon
from gui.main_window import Ui_MainWindow
from gui.game_set_form import Ui_GameSetForm
from gui.filter_dialog import Ui_FliterDialog
from gui.default_option import Ui_defaultOption

from app.model import Users
from app.global_list import *


@unique
class EventType(Enum):
    NORMAL_EVENT = auto()
    TARGET_EVENT = auto()
    VOTE_EVENT = auto()
    SHERIFF_EVENT = auto()
    WATER_EVENT = auto()
    DEAD_EVENT = auto()
    IDENTIFY_EVENT = auto()


MAIN_WIN = None
CLICK_EVENT = EventType.NORMAL_EVENT
EVENT = None


def change_click_event(event_type: EventType):
    global CLICK_EVENT
    CLICK_EVENT = event_type


def change_event(event: tuple):
    global EVENT
    EVENT = event


def clear_event():
    global EVENT
    EVENT = None


class ControlMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ControlMainWindow, self).__init__()
        self.setupUi(self)
        global MAIN_WIN
        MAIN_WIN = self
        self.init_menu()
        self.init_player()
        self.init_tool_bar()
        self.filterButton.clicked.connect(self.click_filter_button)
        read_config()

    def init_menu(self):
        self.newGame.triggered.connect(self.open_new_game)
        self.viewVote.triggered.connect(self.view_vote)
        self.setDefault.triggered.connect(self.open_set_default)
        self.teamAnalysis.triggered.connect(self.analyse_team)
        self.cleanMode.triggered.connect(self.clean_mode)
        self.contactAuthor.triggered.connect(self.contact_author)
        self.softwareInfo.triggered.connect(self.software_info)

    def contact_author(self):
        show_tip_msg(self, self.contactAuthor.text(), AUTHOR)

    def software_info(self):
        show_tip_msg(self, self.softwareInfo.text(), SOFTWARE_INFO)

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

        # Init USER_DB, info, record
        self.infoList.clear()
        self.recordList.clear()
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
                player_label.setText(str(mid + 1) + "号")
                player_button.disconnect()
                player_button.clicked.connect(self.click_player_button)
                set_btn_menu(player_button)
                set_button_icon(player_button)

        # Hide not use player widget
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
        clean_filter()

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
            change_event(('警长', 'sheriff'))

        @check_player
        def click_sheriff_vote():
            change_click_event(EventType.VOTE_EVENT)
            change_event(('收到投票(上警)', 'sheriffVote'))

        @check_player
        def click_strong_support():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('明捞', 'strongSupport'))

        @check_player
        def click_weak_support():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('暗捞', 'weakSupport'))

        @check_player
        def click_strong_against():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('重踩', 'strongOppose'))

        @check_player
        def click_weak_against():
            change_click_event(EventType.TARGET_EVENT)
            change_event(('轻踩', 'weakOppose'))

        @check_player
        def click_vote():
            change_click_event(EventType.VOTE_EVENT)
            change_event(('收到投票(流放)', 'voteRange'))

        @check_player
        def click_dead():
            change_click_event(EventType.DEAD_EVENT)
            change_event((dead,))

        @check_player
        def click_gold_water():
            change_click_event(EventType.WATER_EVENT)
            change_event(('金水', 'goldWater'))

        @check_player
        def click_silver_water():
            change_click_event(EventType.WATER_EVENT)
            change_event(('银水', 'silverWater'))

        @check_player
        def click_identity():
            change_click_event(EventType.IDENTIFY_EVENT)
            change_event((identity,))

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
        gold_water = create_action(':/img/金水', '选择金水玩家')
        silver_water = create_action(':/img/银水', '选择银水玩家')
        identity = create_action(':/img/指认', '指认玩家角色')
        vote = create_action(':/img/投票', '(流放)选择给当前玩家投票的对象')
        sheriff_vote = create_action(':/img/警长-投票', '(上警)选择给当前玩家投票的对象')
        dead = create_action(':/img/死亡', '选择死亡玩家')

        triggered_connect((sheriff, click_sheriff),
                          (strong_support, click_strong_support),
                          (weak_support, click_weak_support),
                          (weak_against, click_weak_against),
                          (strong_against, click_strong_against),
                          (gold_water, click_gold_water),
                          (silver_water, click_silver_water),
                          (identity, click_identity),
                          (vote, click_vote),
                          (sheriff_vote, click_sheriff_vote),
                          (dead, click_dead))

        toolbar_add_actions(sheriff, sheriff_vote, strong_support,
                            weak_support, weak_against, strong_against,
                            gold_water, silver_water, identity,
                            vote, dead)

    def toolbar_act(self):
        """
        Calling this function completes the current toolbar event,
        the event type is EventType(global enum),
        current event is CLICK_EVENT(global var)
        """
        now_player = get_now_player()
        sender = get_user_db(now_player)
        btn = self.sender()
        recipient = get_user_db(button_to_mid(btn))
        recipient_lab = self.__dict__['playerLabel_' + str(recipient.id)]
        default_range = get_default_range()

        # To determine whether the player is dead
        if CLICK_EVENT is not EventType.DEAD_EVENT:
            if CLICK_EVENT is EventType.SHERIFF_EVENT and not recipient.dead:
                pass
            elif sender.dead or recipient.dead:
                self.cancel_target()
                return

        def is_self():
            if sender.id == recipient.id:
                self.cancel_target()
                return True
            return False

        # Determine the type of event
        if CLICK_EVENT is EventType.TARGET_EVENT:
            if is_self():
                return
            sender.add_act_record(EVENT[0], recipient)
            sender.add_relation(recipient, default_range[EVENT[1]])
            self.update_player_info(now_player)
            self.cancel_target()

        elif CLICK_EVENT is EventType.VOTE_EVENT:
            if is_self():
                return
            sender.add_act_record(EVENT[0], recipient)
            if EVENT[0].endswith('(流放)'):
                sender.add_vote(recipient.id)
            else:
                sender.add_sf_vote(recipient.id)
            recipient.add_relation(sender, default_range[EVENT[1]])
            self.update_player_info(now_player)

        elif CLICK_EVENT is EventType.SHERIFF_EVENT:
            sheriff_lab = str(lab_to_mid(recipient_lab)) + "号" + " (警长)"
            if self.__dict__.get('sheriff'):
                default_lab = str(lab_to_mid(self.sheriff)) + "号"
                if recipient_lab == self.sheriff:
                    recipient_lab.setText(default_lab)
                    self.sheriff = None
                else:
                    if self.sheriff.text().split()[1] != '(死亡)':
                        self.sheriff.setText(default_lab)
                    recipient_lab.setText(sheriff_lab)
                    self.sheriff = recipient_lab
            else:
                recipient_lab.setText(sheriff_lab)
                self.sheriff = recipient_lab
            self.cancel_target()

        elif CLICK_EVENT is EventType.DEAD_EVENT:
            tool = EVENT[0]

            def create_menu():
                tool.menu = QMenu(self)
                for dead in DEAD_TYPE:
                    action = tool.menu.addAction(dead)
                    action.triggered.connect(change_dead)
                show_dead_menu()

            def show_dead_menu():
                tool.menu.exec_(QCursor().pos())

            def change_dead():
                dead_lab = str(lab_to_mid(recipient_lab)) + "号" + " (死亡)"
                recipient_lab.setText(dead_lab)
                dead_type = self.sender().text()
                recipient.dead = True, dead_type

            create_menu()
            self.update_player_info(recipient.id)
            self.cancel_target()

        elif CLICK_EVENT is EventType.WATER_EVENT:
            if is_self():
                return
            sender.add_act_record(EVENT[0], recipient)
            sender.add_relation(recipient, default_range[EVENT[1]])
            self.update_player_info(now_player)
            self.cancel_target()

        elif CLICK_EVENT is EventType.IDENTIFY_EVENT:
            tool = EVENT[0]

            def create_menu():
                tool.menu = QMenu(self)
                for dead in get_role_type():
                    action = tool.menu.addAction(dead)
                    action.triggered.connect(add_record)
                show_id_menu()

            def show_id_menu():
                tool.menu.exec_(QCursor().pos())

            def add_record():
                msg = ' 指认 ' + self.sender().text() + ' 是 '
                sender.add_act_record(msg, recipient)

            create_menu()
            self.update_player_info(now_player)
            self.cancel_target()

    def open_new_game(self):
        new_game = ControlGameSetForm()
        new_game.show()
        self.hide()

    def view_vote(self):
        self.cancel_target()
        user_db = get_all_user_db()
        result = []
        for user in user_db.values():
            if user.vote or user.sf_vote:
                string = str(user.id) + ' ← 流放：'+' '.join(str(i) for i in user.vote) + \
                         "\n   ↖ 上警：" + ' '.join(str(i) for i in user.sf_vote)
                result.append(string)
        show_tip_msg(self, "投票结果(流放|上警)", '\n'.join(result))

    def analyse_team(self):
        def get_max(member):
            max_value = max(member.relation, key=itemgetter(1))[1] if member.relation else 0
            if max_value < default_range['teamThreshold']:
                return {}
            return {mid: value for mid, value in member.relation if value == max_value}

        def get_min(member):
            min_value = min(member.relation, key=itemgetter(1))[1] if member.relation else 0
            if min_value > -default_range['teamThreshold']:
                return {}
            return {mid: value for mid, value in member.relation if value == min_value}

        def add_member(team: list, all_member: dict):
            if not all_member:
                return
            for mid, value in all_member.items():
                if mid in team:
                    continue
                team.append(mid)
                member = get_user_db(mid)
                add_member(team, get_max(member))

        def filter_member(team: list):
            for member_id in team:
                member = get_user_db(member_id)
                min_values = get_min(member)
                for mid in min_values.keys():
                    if mid in team:
                        team.remove(member_id)

        def calculate_probability(team: list):
            threshold = default_range['teamThreshold']
            total = 0
            cnt = 0
            for mid in team:
                member = get_user_db(mid)
                other = [oid for oid in team if oid != member.id]
                for oid in other:
                    value = member.find_relation(oid)
                    if value:
                        total += (value - threshold) / threshold
                        cnt += 1
            init_value = default_range['rate'] / get_total_player() if get_total_player() != 0 else 0
            return init_value + (total / cnt if cnt != 0 else 0)

        self.cancel_target()
        all_team = []
        all_probability = []
        users = get_all_user_db()
        default_range = get_default_range()
        for user in users.values():
            all_users = functools.reduce(lambda x, y: x + y, all_team) if all_team else []
            max_user = get_max(user)
            if not [x for x in max_user.keys() if x in all_users]:
                now_team = [user.id]
                add_member(now_team, max_user)
                filter_member(now_team)
                if len(now_team) > 1:
                    all_team.append(now_team)
        for now_team in all_team:
            all_probability.append(calculate_probability(now_team))

        text = list(zip(all_team, all_probability))
        if text:
            result = ["可能团队及概率："]
        else:
            result = []
        for now_team, prob in text:
            string = str(now_team) + " → " + str(round(prob * 100, 3)) + r"%"
            result.append(string)
        show_tip_msg(self, self.teamAnalysis.text(), '\n'.join(result))

    def click_filter_button(self):
        self.cancel_target()
        filter_dialog = FilterDialog()
        filter_dialog.exec()

    def open_set_default(self):
        self.cancel_target()
        default_option = DefaultOption()
        default_option.exec()

    def clean_mode(self):
        if not self.sender().isChecked():
            set_clean_mode(False)
            self.toolBar.show()
            self.infoList.show()
            self.infoLabel.show()
            self.recordList.show()
            self.recordLabel.show()
            self.filterButton.show()
            if self.width() - self.height() != 268:
                self.setGeometry(self.x(), self.y(), self.height() + 268, self.height())
        else:
            set_clean_mode(True)
            self.toolBar.hide()
            self.infoList.hide()
            self.infoLabel.hide()
            self.recordList.hide()
            self.recordLabel.hide()
            self.filterButton.hide()
            self.setGeometry(self.x(), self.y(), self.height(), self.height())

    def closeEvent(self, *args, **kwargs):
        set_geometry(self.x(), self.y(), self.width(), self.height())
        save_config()

    def init_view(self):
        geometry = get_geometry()
        if geometry:
            self.setGeometry(*geometry)
        if get_clean_mode():
            self.cleanMode.setChecked(True)
            self.cleanMode.triggered.emit()


class ControlGameSetForm(QWidget, Ui_GameSetForm):
    def __init__(self):
        super(ControlGameSetForm, self).__init__()
        self.setupUi(self)
        self._total_player = get_total_player()
        self._select_role = get_role_type()[:]
        self._all_role = [role for role in get_all_role() if role not in self._select_role]
        self._custom_role = get_custom_role()
        self.init_button_connect()
        self.init_role_list()

    def init_button_connect(self):
        def change_spinbox():
            self._total_player = self.totalSetSpinBox.value()

        def click_default_button():
            self._select_role = get_role_type()[:]
            self._all_role = [role for role in get_all_role() if role not in get_role_type()]
            self.update_data()

        def click_determine_button():
            self.close()

        def click_right_button():
            role_list = self.allRoleList.selectedItems()
            for item in role_list:
                index = self.allRoleList.row(item)
                item_text = self.allRoleList.takeItem(index).text()
                self._select_role.append(item_text)
                self._all_role.remove(item_text)
            self.update_data()

        def click_left_button():
            role_list = self.selectRoleList.selectedItems()
            for item in role_list:
                index = self.selectRoleList.row(item)
                item_text = self.selectRoleList.takeItem(index).text()
                self._all_role.append(item_text)
                self._select_role.remove(item_text)
            self.update_data()

        def click_add_button():
            text, flag = QInputDialog.getText(self, "添加自定义角色", "角色名字(不能为空且长度小于15)：",
                                              QLineEdit.Normal)
            text = text.strip()
            if flag and text != '' and len(text) < 15:
                if text not in self._select_role:
                    self._select_role.append(text)
                    self._custom_role.append(text)
                    add_all_role(text)
                    self.update_data()
            elif flag:
                show_tip_msg(self, "输入错误", "名字不能为空且长度不能超过15个字符！")

        def click_del_button():
            reply = show_select_msg(self, "删除", "是否删除选定角色？(只能删除自定义角色)")
            if reply != QMessageBox.AcceptRole:
                return
            all_role_list = self.allRoleList.selectedItems()
            select_role_list = self.selectRoleList.selectedItems()

            for item in all_role_list:
                index = self.allRoleList.row(item)
                item_text = self.allRoleList.takeItem(index).text()
                if item_text in self._custom_role:
                    self._all_role.remove(item_text)
                    self._custom_role.remove(item_text)
                    del_all_role(item_text)

            for item in select_role_list:
                index = self.selectRoleList.row(item)
                item_text = self.selectRoleList.takeItem(index).text()
                if item_text in self._custom_role:
                    self._select_role.remove(item_text)
                    self._custom_role.remove(item_text)
                    del_all_role(item_text)
            self.update_data()

        self.totalSetSpinBox.valueChanged.connect(change_spinbox)
        self.defaultButton.clicked.connect(click_default_button)
        self.determineButton.clicked.connect(click_determine_button)
        self.rightButton.clicked.connect(click_right_button)
        self.leftButton.clicked.connect(click_left_button)
        self.addButton.clicked.connect(click_add_button)
        self.delButton.clicked.connect(click_del_button)

    def init_role_list(self):
        self.allRoleList.setSelectionMode(QListWidget.MultiSelection)
        self.selectRoleList.setSelectionMode(QListWidget.MultiSelection)
        self.update_data()

    def update_data(self):
        def update_total():
            value = self._total_player
            min_value = self.totalSetSpinBox.minimum()
            max_value = self.totalSetSpinBox.maximum()
            self.totalSetSpinBox.setValue(value if value in range(min_value - 1, max_value + 1) else min_value)

        def update_all_role():
            self.allRoleList.clear()
            self.allRoleList.addItems(self._all_role)

        def update_select_role():
            self.selectRoleList.clear()
            self.selectRoleList.addItems(self._select_role)

        update_total()
        update_all_role()
        update_select_role()

    def save_option(self):
        if not self._select_role:
            return False
        self._total_player = self.totalSetSpinBox.value()
        set_total_player(self._total_player)
        set_role_type(self._select_role[:])
        return True

    def closeEvent(self, close_event):
        flag = True
        reply = show_save_msg(self)
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


class FilterDialog(QDialog, Ui_FliterDialog):
    def __init__(self):
        super(FilterDialog, self).__init__()
        self.setupUi(self)
        self._total_player = get_total_player()
        self._now_player = get_user_db(get_now_player())
        self.init_items()
        self.init_button()

    def init_items(self):
        if not self._now_player:
            return
        group_box = self.playerList
        button_box = QVBoxLayout()
        if self._now_player.__dict__.get('filter_list'):
            for index, choose in self._now_player.filter_list:
                check_box = QCheckBox(str(index) + "号")
                check_box.setObjectName(str(index))
                check_box.setChecked(choose)
                check_box.stateChanged.connect(self.check_box_changed)
                button_box.addWidget(check_box)
        else:
            self._now_player.filter_list = []
            for index in range(self._total_player):
                result = self._now_player.find_record(index + 1)
                if result:
                    check_box = QCheckBox(group_box)
                    check_box.setObjectName(str(index + 1))
                    check_box.setText(str(index + 1) + "号")
                    check_box.setChecked(True)
                    check_box.stateChanged.connect(self.check_box_changed)
                    button_box.addWidget(check_box)
                    self._now_player.filter_list.append((index + 1, True))
        group_box.setLayout(button_box)

    def init_button(self):
        self.selectAllButton.clicked.connect(self.click_all_select)
        self.determineButton.clicked.connect(self.click_determine_button)
        self.antiElectionButton.clicked.connect(self.click_anti_election)

    def click_determine_button(self):
        update_filter()
        self.close()

    def click_cancel_button(self):
        pass

    def click_all_select(self):
        for check_box in self.playerList.children():
            if isinstance(check_box, QCheckBox):
                check_box.setChecked(True)

    def click_anti_election(self):
        for check_box in self.playerList.children():
            if isinstance(check_box, QCheckBox):
                check_box.setChecked(False)

    def check_box_changed(self):
        sender = self.sender()
        mid = int(sender.objectName())
        filter_list = self._now_player.filter_list
        if isinstance(sender, QCheckBox):
            if sender.isChecked():
                if (mid, False) in filter_list:
                    index = self._now_player.filter_list.index((mid, False))
                    self._now_player.filter_list[index] = (mid, True)
            elif (mid, True) in filter_list:
                index = self._now_player.filter_list.index((mid, True))
                self._now_player.filter_list[index] = (mid, False)


def update_filter():
    now_player = get_user_db(get_now_player())
    if not now_player or not now_player.__dict__.get('filter_list'):
        return
    MAIN_WIN.filterButton.setText("筛选")
    record_list = MAIN_WIN.recordList
    filter_list = now_player.filter_list

    record_list.clear()
    flag = False
    for act, obj in now_player.act_record:
        if (obj, True) in filter_list:
            record_list.addItem(str(get_now_player()) + "号" + " " + act + " " + str(obj) + "号")
        else:
            flag = True
    if flag:
        MAIN_WIN.filterButton.setText("筛选*")


def clean_filter():
    now_player = get_user_db(get_now_player())
    MAIN_WIN.filterButton.setText("筛选")
    if not now_player or not now_player.__dict__.get('filter_list'):
        return
    now_player.__dict__['filter_list'] = []
    update_filter()


class DefaultOption(QDialog, Ui_defaultOption):
    def __init__(self):
        super(DefaultOption, self).__init__()
        self.setupUi(self)
        self._config = get_default_range()
        self.read_config()

    def read_config(self):
        for key, value in self._config.items():
            self.__dict__.get(key).setValue(value)

    def closeEvent(self, close_event):
        reply = show_save_msg(self)
        if reply == QMessageBox.AcceptRole:
            for key, value in self._config.items():
                if self._config.get(key):
                    self._config[key] = self.__dict__.get(key).value()
            set_default_range(**self._config)


def show_save_msg(parent):
    return show_select_msg(parent, "保存", "是否保存设置？")


def show_select_msg(parent, title, text):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setIcon(msg.Question)
    msg.setText(text)
    msg.addButton('确定', QMessageBox.YesRole)
    msg.addButton('取消', QMessageBox.NoRole)
    return msg.exec()


def show_tip_msg(parent, title, text):
    msg = QMessageBox(parent)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Information)
    if not text:
        text = '    无       '
    msg.setText(text)
    msg.exec()
