import unittest
from Lab5_A00354816 import Lab5


class MyTestCase(unittest.TestCase):
    def test_input_num(self):
        un_list_int = Lab5.set_input_data(Lab5, "unsorted_list.csv", True)
        self.assertEqual(un_list_int, [5, 2, 3, 7, 1, 20, 3, 7, 100, 3, 1, 0])

    def test_merge_int(self):
        Lab5.set_input_data(Lab5, "unsorted_list.csv", True)
        sorted_list_int = Lab5.execute_merge_sort(Lab5)
        self.assertEqual(sorted_list_int, [0, 1, 1, 2, 3, 3, 3, 5, 7, 7, 20, 100])

    def test_input_str(self):
        un_list = Lab5.set_input_data(Lab5, "unsorted_list.csv", False)
        self.assertEqual(un_list, ['5', '2', '3', '7', '1', '20', '3', '7', '100', '3', '1', '0'])

    def test_merge_str(self):
        Lab5.set_input_data(Lab5, "unsorted_list.csv", False)
        sorted_list = Lab5.execute_merge_sort(Lab5)
        self.assertEqual(sorted_list, ['0', '1', '1', '100', '2', '20', '3', '3', '3', '5', '7', '7'])


if __name__ == '__main__':
    unittest.main()
