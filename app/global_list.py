# coding = utf-8
from os.path import join, exists
import gui.img

PATH_CONFIG = join('.', 'config.json')

TOTAL_PLAYER = 0
RECORD_VOTE = []
USER_DB = {}

NOW_ROUND = 0
NOW_PLAYER = 0

ROLE_TYPE = []
ALL_ROLE = ['狼人', '村民', '预言家', '丘比特', '猎人', '白痴', '守卫', '盗贼', '村长', '白狼王', '女巫']
ACTION_TYPE = ("明捞", "暗捞", "重踩", "轻踩")

DEFAULT_STYLE = 'border-image:url(%s);border-radius:10px;'
ROLE_STYLE = {'狼人': DEFAULT_STYLE % ':/img/狼人',
              '村民': DEFAULT_STYLE % ':/img/村民',
              '预言家': DEFAULT_STYLE % ':/img/预言家',
              '丘比特': DEFAULT_STYLE % ':/img/丘比特',
              '猎人': DEFAULT_STYLE % ':/img/猎人',
              '白痴': DEFAULT_STYLE % ':/img/白痴',
              '守卫': DEFAULT_STYLE % ':/img/守卫',
              '盗贼': DEFAULT_STYLE % ':/img/盗贼',
              '村长': DEFAULT_STYLE % ':/img/村长',
              '白狼王': DEFAULT_STYLE % ':/img/白狼王',
              '女巫': DEFAULT_STYLE % ':/img/女巫',
              '未知': DEFAULT_STYLE % ':/img/未知',
              '自定义': DEFAULT_STYLE % ':/img/自定义'
              }


def read_config():
    all_var = globals()
    if exists(PATH_CONFIG):
        import json
        import app.model

        try:
            with open(PATH_CONFIG, 'r') as file:
                jsonData = json.load(file)
        except IOError:
            raise IOError('The file(%s) open error' % PATH_CONFIG)

        for var, value in jsonData.items():
            if all_var.get(var) is not None:
                if var == 'USER_DB':
                    for mid, role in value.items():
                        mid = int(mid)
                        app.model.Users(mid, role)
                else:
                    all_var[var] = value


def get_total_player():
    return TOTAL_PLAYER


def set_total_player(total: int):
    global TOTAL_PLAYER
    TOTAL_PLAYER = total


def get_now_player():
    return NOW_PLAYER


def set_now_player(mid: int):
    global NOW_PLAYER
    NOW_PLAYER = mid


def get_user_db(user: int):
    return USER_DB.get(user)


def add_user_db(mid: int, user):
    global USER_DB
    USER_DB[mid] = user
    return mid


def clear_user_db():
    global USER_DB
    USER_DB.clear()


def get_role_type():
    return ROLE_TYPE


def set_role_type(role_type: list):
    global ROLE_TYPE
    ROLE_TYPE = role_type


def get_all_role():
    return ALL_ROLE


def add_all_role(role: str):
    ALL_ROLE.append(role)
    return role


def get_role_style(role: str):
    return ROLE_STYLE.get(role)


def get_now_round():
    return NOW_ROUND


def add_now_round():
    global NOW_ROUND
    NOW_ROUND += 1
    return get_now_round()
