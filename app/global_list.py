# coding = utf-8
from os.path import join, exists
import gui.img

PATH_CONFIG = join('.', 'config.dat')
SOFTWARE_INFO = "狼人杀记牌器v1.0"
AUTHOR = "邮箱：remalloc.virtual@gmail.com\n" \
         "源码：https://github.com/Remalloc/werewolf"

TOTAL_PLAYER = 0
USER_DB = {}
NOW_PLAYER = 0
CLEAN_MODE = False
GEOMETRY = ()

ROLE_TYPE = []
ALL_ROLE = ['狼人', '村民', '预言家', '丘比特', '猎人', '白痴', '守卫', '盗贼', '村长', '白狼王', '女巫']
CUSTOM_ROLE = []

ACTION_TYPE = ("明捞", "暗捞", "重踩", "轻踩")
DEAD_TYPE = ('未知', '中刀', '中毒', '中枪', '流放', '链接')
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

DEFAULT_THRESHOLD = 2.5
DEFAULT_WEAK_SUPPORT_RANGE = 0.5
DEFAULT_WEAK_OPPOSE_RANGE = -0.5
DEFAULT_STRONG_SUPPORT_RANGE = 1.0
DEFAULT_STRONG_OPPOSE_RANGE = -1.0
DEFAULT_VOTE_RANGE = 2.0
DEFAULT_RATE = 0.5


def read_config():
    if exists(PATH_CONFIG):
        import json

        try:
            with open(PATH_CONFIG, 'r') as file:
                json_data = json.load(file)
        except IOError:
            raise IOError('The file(%s) open error' % PATH_CONFIG)

        for var, value in json_data.items():
            globals()[var] = value


def save_config():
    import json

    save_dict = {'TOTAL_PLAYER': TOTAL_PLAYER,
                 'ROLE_TYPE': ROLE_TYPE,
                 'ALL_ROLE': ALL_ROLE,
                 'CUSTOM_ROLE': CUSTOM_ROLE,
                 'DEFAULT_THRESHOLD': DEFAULT_THRESHOLD,
                 'DEFAULT_WEAK_SUPPORT_RANGE': DEFAULT_WEAK_SUPPORT_RANGE,
                 'DEFAULT_WEAK_OPPOSE_RANGE': DEFAULT_WEAK_OPPOSE_RANGE,
                 'DEFAULT_STRONG_SUPPORT_RANGE': DEFAULT_STRONG_SUPPORT_RANGE,
                 'DEFAULT_STRONG_OPPOSE_RANGE': DEFAULT_STRONG_OPPOSE_RANGE,
                 'DEFAULT_VOTE_RANGE': DEFAULT_VOTE_RANGE,
                 'DEFAULT_RATE': DEFAULT_RATE,
                 'CLEAN_MODE': CLEAN_MODE,
                 'GEOMETRY': GEOMETRY
                 }
    try:
        with open(PATH_CONFIG, 'w') as file:
            json.dump(save_dict, file)
    except IOError:
        raise IOError('The file(%s) open error' % PATH_CONFIG)


def get_geometry():
    return GEOMETRY


def set_geometry(*geometry):
    if len(geometry) == 4:
        global GEOMETRY
        GEOMETRY = geometry


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


def get_clean_mode():
    return CLEAN_MODE


def set_clean_mode(tf: bool):
    global CLEAN_MODE
    CLEAN_MODE = tf


def get_user_db(user: int):
    return USER_DB.get(user)


def get_all_user_db():
    return USER_DB


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


def get_custom_role():
    return CUSTOM_ROLE


def get_role_style(role: str):
    return ROLE_STYLE.get(role)


def get_default_range():
    return {'teamThreshold': DEFAULT_THRESHOLD,
            'weakSupport': DEFAULT_WEAK_SUPPORT_RANGE,
            'weakOppose': DEFAULT_WEAK_OPPOSE_RANGE,
            'strongSupport': DEFAULT_STRONG_SUPPORT_RANGE,
            'strongOppose': DEFAULT_STRONG_OPPOSE_RANGE,
            'voteRange': DEFAULT_VOTE_RANGE,
            'rate': DEFAULT_RATE}


def set_default_range(**kwargs):
    switch_name = {'teamThreshold': 'DEFAULT_THRESHOLD',
                   'weakSupport': 'DEFAULT_WEAK_SUPPORT_RANGE',
                   'weakOppose': 'DEFAULT_WEAK_OPPOSE_RANGE',
                   'strongSupport': 'DEFAULT_STRONG_SUPPORT_RANGE',
                   'strongOppose': 'DEFAULT_STRONG_OPPOSE_RANGE',
                   'voteRange': 'DEFAULT_VOTE_RANGE',
                   'rate': 'DEFAULT_RATE'}
    for key, value in kwargs.items():
        key = switch_name.get(key)
        if globals().get(key):
            globals()[key] = value
