import unittest
from Lab2_A00354816 import main_pwrLst
from Lab2_A00354816 import main_users


class MyTestCase(unittest.TestCase):
    def test_createNew1(self):
        x = main_pwrLst(1, 4, [])
        self.assertEqual(x, [4])

    def test_createNew2(self):
        x = main_pwrLst(1, 2, [])
        self.assertEqual(x, [4,2])

    def test_createNew3(self):
        x = main_pwrLst(1, 9, [])
        self.assertEqual(x, [4, 2, 9])

    def test_createNew4(self):
        x = main_pwrLst(1, 5, [])
        self.assertEqual(x, [4, 2, 9, 5])

    def test_del_item(self):
        x = main_pwrLst(2, 0, [])
        self.assertEqual(x, [2,9,5])

    def test_sort(self):
        x = main_pwrLst(3, 0, [])
        self.assertEqual(x,[2, 5, 9])


    def test_dbadd(self):
        x = main_users(1, "mayra", "1st Ave", "molina@gmail", "33333333")
        self.assertEqual(x, {'mayra': {'Address': '1st Ave', 'Phone': 'molina@gmail', 'Mail': '33333333'}})

    def test_dbsearch(self):
        x = main_users(4, "mayra", 0, 0, 0)
        self.assertEqual(x, {'Address': '1st Ave', 'Phone': 'molina@gmail', 'Mail': '33333333'})


if __name__ == '__main__':
    unittest.main()
