# coding = utf-8

TOTAL_PLAYER = 0
USER_DB = {}
NOW_ROUND = 0
NOW_PLAYER = 0
ROLE_TYPE_LIST = []


def set_now_player(value: int):
    global NOW_PLAYER
    NOW_PLAYER = value
