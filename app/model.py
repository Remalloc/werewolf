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


class Models:
    """
    All models will extends this class
    """
    pass


class Users(Models):
    @type_check
    def __init__(self, mid: int, role: str, relation: dict = None, act_record: list = None):
        """
        :param relation: {user:relation_num} the relation_num is indicates the intimacy(weight) of the target role
        :param act_record:[(self,action,target)...]
        """
        self._id = mid
        self._role = role
        self._relation = {} if relation is None else relation
        self._act_record =[] if act_record is None else act_record
        USER_DB[mid]=self

    @type_check
    def get_set_id(self, mid: int = -1):
        if mid !=-1:
            self._id = mid
        return self._id

    @type_check
    def get_set_role(self, role: str = None):
        if role is not None:
            self._role = role
        return self._role

    @type_check
    def add_relation(self, user: Models, default: int = 0):
        if not self._relation.get(user):
            self._relation[user] = default
        return self.get_set_id(), user.get_set_id(), self._relation[user]

    @type_check
    def modify_relation(self, user: Models, add_nums: int):
        if self._relation.get(user):
            self._relation[user] = self._relation.get(user) + add_nums
            return self._relation[user]
        else:
            return None

    @type_check
    def get_relation(self, mid: int = None):
        """
        :return: One list have more triads. e.g.: [(id,role,relation_num),...]
        """
        if mid is not None:
            return [(self.get_set_id(), user.get_set_id(), num)
                    for user, num in self._relation.items() if user.get_set_id() == mid]
        return [(self.get_set_id(), user.get_set_id(), num)
                for user, num in self._relation.items()]

    @type_check
    def add_act_record(self, act: str, target: Models):
        """
        :param act: The action of the current character
        :param target:Action target
        :return:Now action record
        """
        self._act_record.append((act, target))
        return self._act_record

    @type_check
    def pop_act_record(self, index: int = -1):
        result = self._act_record.pop(index)
        return result[0], result[1].get_set_id()

    @type_check
    def get_act_record(self, mid: int = None):
        if mid is not None:
            return [(act, tid.get_set_id()) for act, tid in self._act_record if tid.get_set_id() == mid]
        return [(act, tid.get_set_id()) for act, tid in self._act_record]
