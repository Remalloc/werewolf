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


class Users():
    @type_check
    def __init__(self, mid: int, role: str):
        """
        :param relation: {user:relation_num} the relation_num is indicates the intimacy(weight) of the target role
        :param act_record:[(self,action,target)...]
        """
        self._id = mid
        self._role = role
        self._relation = {}
        self._act_record = []
        self._reliable = 0
        self._vote = []
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
        return [(self.id, user.id, value) for user, value in self._relation.items()]

    @type_check
    def add_relation(self, user, value: int = 0):
        if not self._relation.get(user):
            self._relation[user] = value
        return value

    @type_check
    def modify_relation(self, user, value: int):
        if self._relation.get(user):
            self._relation[user] = value
            return value
        else:
            return None

    @type_check
    def find_relation(self, mid: int):
        for user, value in self.relation:
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
        for act, obj in list(self._act_record):
            if obj.id == mid:
                return act, obj
        return None

    @property
    def reliable(self):
        return self._reliable

    @reliable.setter
    def reliable(self, value: int):
        self._reliable = value

    @type_check
    def add_reliable(self, value: int):
        self._reliable += value
        return self._reliable

    @property
    def dead(self):
        return self._dead

    @dead.setter
    def dead(self, *args):
        if len(args) != 2:
            raise AttributeError("Function dead(args) must have 2 parameters")
        if isinstance(args[0], bool):
            raise TypeError("First parameter type is not bool")
        if isinstance(args[1], str):
            raise TypeError("Second parameter type is not str")
        self._dead = args

    @property
    def info(self):
        self._info = {'位置：': self._id,
                      '角色：': self._role,
                      '可信度：': self._reliable,
                      '死亡：': '是 ' if self._dead[0] else '否 ' + self._dead[1]}
        return self._info

    @property
    def vote(self):
        return self._vote

    @type_check
    def add_vote(self, mid: int):
        self._vote.append(mid)
        return mid
