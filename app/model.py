# coding = utf-8


class Users:
    def __init__(self, id, role, relation={},act_record=[]):
        self._id = id
        self._role = role
        self._relation = relation
        self._act_record=act_record

    def get_set_id(self, id=None):
        if id is not None:
            check_id_type(id)
            self._id = id
        return self._id

    def get_set_role(self, role=None):
        if role is not None:
            check_role_type(role)
            self._role=role
        return self._role

    def add_relation(self, user, default=0):
        check_user_type(user)
        if self._relation.get(user):
            raise "The connect was build"
        self._relation[user] = default

    def modify_relation(self, user, add_nums):
        check_user_type(user)
        self._relation[user] = self._relation.get(user) + add_nums

    def get_relation(self):
        '''
        :return: One list have more triads. e.g.: [(id,role,relation_num),...]
        '''
        return [(x.get_set_id(), x.get_set_role(), y) for x, y in self._relation.items()]

    def add_act_record(self,act,target):
        '''
        :param act: The action of the current character
        :param target:Action target
        :return:Now action record
        '''
        check_user_type(target)
        self._act_record.append((self,act,target))
        return self._act_record

    def pop_act_record(self,index=-1):
        return self._act_record.pop(index)

def check_user_type(user):
    if type(user) is not Users:
        raise "The parameter user type must be 'Users'"
    return True


def check_id_type(id):
    if type(id) is not int:
        raise "The parameter id type must be 'int'"
    return True


def check_role_type(role):
    if type(role) is not str:
        raise "The parameter role type must be 'str'"
    return True

