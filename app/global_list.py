# coding = utf-8
from os.path import join, exists

PATH_CONFIG = join('..', 'config.json')

TOTAL_PLAYER = 0
USER_DB = {}

NOW_ROUND = 0
NOW_PLAYER = 0

ROLE_TYPE_LIST = []
ACTION_TYPE = ("strong support", "weak support", "strong against", "weak against")

DEFAULT_STYLE='border-image:url(:/img/Unknown);border-radius:10px;'

if exists(PATH_CONFIG):
    import json

    try:
        with open(PATH_CONFIG, 'r') as file:
            jsonData = json.load(file)
    except IOError:
        raise IOError('The file(%s) open error' % PATH_CONFIG)

    all_var = globals()
    for var, value in jsonData.items():
        if all_var.get(var) is not None:
            all_var[var] = value


def set_now_player(player: int):
    global NOW_PLAYER
    NOW_PLAYER = player

