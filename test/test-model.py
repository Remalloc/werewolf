# coding = utf-8
import unittest
from app.model import *


class TestModel(unittest.TestCase):
    def setUp(self):
        self.wolf = Users(0, 'wolf')
        self.god = Users(2, 'god', {self.wolf: -5})
        self.human = Users(1, 'human',
                           {self.wolf: 1, self.god: -1},
                           [('support', self.wolf)])

    def test_get_set(self):
        # test get_set_id
        self.assertEqual(self.wolf.get_set_id(), 0)
        self.assertEqual(self.wolf.get_set_id(1), 1)

        # test get_set_role
        self.assertEqual(self.wolf.get_set_role(), 'wolf')
        self.assertEqual(self.wolf.get_set_role('god'), 'god')

    def test_check_type(self):
        @type_check
        def fun(user: Models, mid: int, role: str, relation: dict, record: list) -> bool:
            return True

        self.assertTrue(fun(Users(0, ""), 0, "", {}, []))

    def test_get_relation(self):
        self.assertListEqual(self.human.get_relation(), [(1, 0, 1), (1, 2, -1)])
        self.assertListEqual(self.human.get_relation(2), [(1, 2, -1)])
        self.assertListEqual(self.human.get_relation(3), [])

    def test_add_relation(self):
        self.assertTupleEqual(self.wolf.add_relation(self.human), (0, 1, 0))
        self.assertListEqual(self.wolf.get_relation(), [(0, 1, 0)], 'add relation error')
        self.assertTupleEqual(self.wolf.add_relation(self.god, 5), (0, 2, 5))
        self.assertListEqual(self.wolf.get_relation(2), [(0, 2, 5)])

    def test_modify_relation(self):
        self.assertEqual(self.god.modify_relation(self.wolf, 5), 0)
        self.assertEqual(self.human.modify_relation(self.human, 6), None)

    def test_get_act_record(self):
        self.assertListEqual(self.human.get_act_record(), [('support', 0)])
        self.assertListEqual(self.human.get_act_record(0), [('support', 0)])

    def test_add_act_record(self):
        self.god.add_act_record('against', self.wolf)
        self.god.add_act_record('support', self.human)
        self.assertListEqual(self.god.get_act_record(), [('against', 0), ('support', 1)])

    def test_pop_act_record(self):
        self.human.add_act_record('against', self.god)
        self.assertTupleEqual(self.human.pop_act_record(0), ('support', self.wolf.get_set_id()))
        self.assertTupleEqual(self.human.pop_act_record(), ('against', self.god.get_set_id()))


if __name__ == '__main__':
    unittest.main()
