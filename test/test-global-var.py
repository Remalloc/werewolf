# coding = utf-8
import unittest
from os.path import join


class TestGlobalVar(unittest.TestCase):
    def setUp(self):
        self.PATH_CONFIG = join('..', 'config.json')

        self.TOTAL_PLAYER = 5
        self.USER_DB = {1: "a", 2: "b", 3: "c"}

        self.NOW_ROUND = 2
        self.NOW_PLAYER = 5

        self.ROLE_TYPE_LIST = ['wolf', 'god', 'human']
        self.ACTION_TYPE = ("strong support", "weak support", "strong against", "weak against")

    def test_read_config(self):
        import json
        data = {'PATH_CONFIG': self.PATH_CONFIG,
                'TOTAL_PLAYER': self.TOTAL_PLAYER,
                'USER_DB': self.USER_DB,
                'NOW_PLAYER': self.NOW_PLAYER,
                'NOW_ROUND': self.NOW_ROUND,
                'ACTION_TYPE': self.ACTION_TYPE}
        with open(self.PATH_CONFIG, 'w') as file:
            json.dump(data, file)

        import app.global_list
        for var, value in data.items():
            if self.assertTrue(app.global_list.all_var.get(var)):
                if isinstance(value, int) or isinstance(value, str):
                    self.assertEqual(app.global_list.all_var.get(var), value)
                elif isinstance(value, list):
                    self.assertListEqual(app.global_list.all_var.get(var), value)
                elif isinstance(value, dict):
                    self.assertDictEqual(app.global_list.all_var.get(var), value)


if __name__ == '__main__':
    unittest.main()
