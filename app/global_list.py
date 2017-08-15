# coding = utf-8
from os.path import join, exists
import gui.img

PATH_CONFIG = join('.', 'config.json')

TOTAL_PLAYER = 12
USER_DB = {}

NOW_ROUND = 0
NOW_PLAYER = 0

ROLE_TYPE_LIST = []
ACTION_TYPE = ("strong support", "weak support", "strong against", "weak against")

DEFAULT_STYLE = 'border-image:url(%s);border-radius:10px;'
ROLE_STYLE = {'Werewolves': DEFAULT_STYLE % ':/img/Werewolves',
              'Villagers': DEFAULT_STYLE % ':/img/Villagers',
              'Seer': DEFAULT_STYLE % ':/img/Seer',
              'Cupid': DEFAULT_STYLE % ':/img/Cupid',
              'Hunter': DEFAULT_STYLE % ':/img/Hunter',
              'Idiot': DEFAULT_STYLE % ':/img/Idiot',
              'Savior': DEFAULT_STYLE % ':/img/Savior',
              'Thieves': DEFAULT_STYLE % ':/img/Thieves',
              'Ancient': DEFAULT_STYLE % ':/img/Ancient',
              'White Wolf': DEFAULT_STYLE % ':/img/White Wolf',
              'Witch': DEFAULT_STYLE % ':/img/Witch',
              'Sheriff': DEFAULT_STYLE % ':/img/Sheriff',
              'Unknown': DEFAULT_STYLE % ':/img/Unknown'
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
