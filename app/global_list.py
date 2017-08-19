# coding = utf-8
from os.path import join, exists
import gui.img

PATH_CONFIG = join('.', 'config.json')

TOTAL_PLAYER = 12
USER_DB = {}

NOW_ROUND = 0
NOW_PLAYER = 0

ROLE_TYPE_LIST = []
SPECIAL_ROLE=set(['警长','未知'])
ACTION_TYPE = ("strong support", "weak support", "strong against", "weak against")

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
              '警长': DEFAULT_STYLE % ':/img/警长',
              '未知': DEFAULT_STYLE % ':/img/未知',
              '自定义':DEFAULT_STYLE % ':/img/自定义'
              }

all_var = globals()
if exists(PATH_CONFIG):
    import json
    from app.model import Users

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
                    USER_DB[mid] = Users(mid, role)
            else:
                all_var[var] = value


def set_now_player(player: int):
    global NOW_PLAYER
    NOW_PLAYER = player
