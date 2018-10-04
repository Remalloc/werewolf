# coding = utf-8
import functools
from app.global_list import USER_DB


def type_check(fun):
    def do_type_check(name, arg):
        expected_type = fun.__annotations__.get(name, None)
        if expected_type and not isinstance(arg, expected_type):
            raise RuntimeError("{} should be of type {} instead of {}"
                               .format(name, expected_type.__name__, type(arg).__name__))

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args[:fun.__code__.co_nlocals]):
            do_type_check(fun.__code__.co_varnames[i], arg)
        for name, arg in kwargs.items():
            do_type_check(name, arg)
        result = fun(*args, **kwargs)
        do_type_check('return', result)
        return result

    return wrapper


class Users:
    @type_check
    def __init__(self, mid: int, role: str):
        self._id = mid
        self._role = role
        self._relation = {}
        self._act_record = []
        self._vote = []
        self._sf_vote = []
        self._info = {}
        self._dead = False, ''
        USER_DB[mid] = self

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, mid: int):
        self._id = mid

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role: str = None):
        if role is not None:
            self._role = role

    @property
    def relation(self):
        return [(user.id, value) for user, value in self._relation.items()]

    @type_check
    def add_relation(self, user, value: float = 0):
        if not self._relation.get(user):
            self._relation[user] = value
        else:
            self._relation[user] += value
        return value

    @type_check
    def modify_relation(self, user, value: float):
        if self._relation.get(user):
            self._relation[user] = value
            return value
        else:
            return None

    @type_check
    def find_relation(self, mid: int):
        for user, value in self._relation.items():
            if user.id == mid:
                return value
        return None

    @property
    def act_record(self):
        return [(act, obj.id) for act, obj in list(self._act_record)]

    @type_check
    def add_act_record(self, act: str, target):
        """
        :param act: The action of the current character
        :param target:Action target(type is User)
        :return:Now action record
        """
        self._act_record.append((act, target))
        return self._act_record

    @type_check
    def pop_act_record(self, index: int = -1):
        return self._act_record.pop(index)

    @type_check
    def find_record(self, mid: int):
        result = []
        for act, obj in list(self._act_record):
            if obj.id == mid:
                result.append((act, obj))
        return result

    @property
    def dead(self):
        return self._dead[0]

    @dead.setter
    def dead(self, args):
        if len(args) != 2:
            raise AttributeError("Function dead(args) have %s parameters not 2" % len(args))
        if not isinstance(args[0], bool):
            raise TypeError("First parameter %s is not bool" % type(args[0]))
        if not isinstance(args[1], str):
            raise TypeError("Second parameter type is not str")
        self._dead = args

    @property
    def info(self):
        self._info = {'位置：': self._id,
                      '角色：': self._role,
                      '收到投票(流放)：': self._vote if self._vote else '无',
                      '收到投票(上警)：': self._sf_vote if self._sf_vote else '无',
                      '死亡：': '是 ' + self._dead[1] if self._dead[0] else '否 '}
        return self._info

    @property
    def vote(self):
        return self._vote

    @type_check
    def add_vote(self, mid: int):
        self._vote.append(mid)
        return mid

    @property
    def sf_vote(self):
        return self._sf_vote

    @type_check
    def add_sf_vote(self, mid: int):
        self._sf_vote.append(mid)
        return mid
