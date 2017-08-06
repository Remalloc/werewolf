# coding = utf-8


class Users:
    def __init__(self, mid, role, relation={}, act_record=[]):
        '''
        :param relation: {user:relation_num} the relation_num is indicates the intimacy(weight) of the target role
        :param act_record:[(self,action,target)...]
        '''
        self._id = mid
        self._role = role
        self._relation = relation
        self._act_record = act_record

    def get_set_id(self, mid=None):
        if mid is not None:
            check_id_type(mid)
            self._id = mid
        return self._id

    def get_set_role(self, role=None):
        if role is not None:
            check_role_type(role)
            self._role = role
        return self._role

    def add_relation(self, user, default=0):
        check_user_type(user)
        if not self._relation.get(user):
            self._relation[user] = default
        return self.get_set_id(), user.get_set_id(), self._relation[user]

    def modify_relation(self, user, add_nums):
        check_user_type(user)
        if self._relation.get(user):
            self._relation[user] = self._relation.get(user) + add_nums
            return self._relation[user]
        else:
            return None

    def get_relation(self, mid=None):
        '''
        :return: One list have more triads. e.g.: [(id,role,relation_num),...]
        '''
        if mid is not None:
            return [(self.get_set_id(), user.get_set_id(), num)
                    for user, num in self._relation.items() if user.get_set_id() == mid]
        return [(self.get_set_id(), user.get_set_id(), num)
                for user, num in self._relation.items()]

    def add_act_record(self, act, target):
        '''
        :param act: The action of the current character
        :param target:Action target
        :return:Now action record
        '''
        check_user_type(target)
        self._act_record.append((act, target))
        return self._act_record

    def pop_act_record(self, index=-1):
        result = self._act_record.pop(index)
        return result[0], result[1].get_set_id()

    def get_act_record(self, mid=None):
        if mid is not None:
            return [(act, tid.get_set_id()) for act, tid in self._act_record if tid.get_set_id() == mid]
        return [(act, tid.get_set_id()) for act, tid in self._act_record]


def check_user_type(user):
    if not isinstance(user, Users):
        raise TypeError("The parameter user type must be 'Users'")
    return True


def check_id_type(mid):
    if not isinstance(mid, int):
        raise TypeError("The parameter id type must be 'int'")
    return True


def check_role_type(role):
    if not isinstance(role, str):
        raise TypeError("The parameter role type must be 'str'")
    return True
