# coding = utf-8
from os.path import join, exists

PATH_CONFIG = join('..', 'config.json')

TOTAL_PLAYER = 0
USER_DB = {}

NOW_ROUND = 0
NOW_PLAYER = 0

ROLE_TYPE_LIST = []
ACTION_TYPE = ("strong support", "weak support", "strong against", "weak against")


def set_now_player(value: int):
    global NOW_PLAYER
    NOW_PLAYER = value


if exists(PATH_CONFIG):
    import json
    try:
        jsonData = json.load(open(PATH_CONFIG))
    except IOError:
        raise IOError('The file(%s) open error'% PATH_CONFIG)

    all_var = globals()
    for var, value in jsonData.item():
        if all_var.get(var):
            all_var[var] = value


