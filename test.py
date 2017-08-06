# coding = utf-8
import unittest
from app.model import *


class TestModel(unittest.TestCase):
    def setUp(self):
        self.wolf = Users(0, 'wolf')
        self.god = Users(2, 'god')
        self.human = Users(1, 'human', {self.wolf: 1, self.god: -1})


    def test_get_set(self):
        # test get_set_id
        self.assertEqual(self.wolf.get_set_id(), 0)
        self.assertEqual(self.wolf.get_set_id(1), 1)

        # test get_set_role
        self.assertEqual(self.wolf.get_set_role(), 'wolf')
        self.assertEqual(self.wolf.get_set_role('god'), 'god')

    def test_get_relation(self):
        self.assertListEqual(self.human.get_relation(), [(1, 0, 1), (1, 2, -1)])
        self.assertListEqual(self.human.get_relation(2), [(1, 2, -1)])
        self.assertListEqual(self.human.get_relation(3), [])

    def test_add_relation(self):
        self.assertTupleEqual(self.wolf.add_relation(self.human),(0,1,0))
        self.assertListEqual(self.wolf.get_relation(),[(0,1,0)],'add relation error')
        self.assertTupleEqual(self.wolf.add_relation(self.god,5),(0,2,5))
        self.assertListEqual(self.wolf.get_relation(2),[(0,2,5)])



if __name__ == '__main__':
    unittest.main()
