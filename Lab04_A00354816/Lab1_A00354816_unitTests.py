import unittest
from Lab1_A00354816 import lab1_9
from Lab1_A00354816 import lab1_8


class MyTestCase(unittest.TestCase):
    def test_lab1_8_samplemean(self):
        x =  lab1_8(1,[10, 12, 23, 23, 16, 23, 21, 16],0)
        self.assertEqual(x, 18)

    def test_lab1_8_samplestd(self):
        x =  lab1_8(2,[10, 12, 23, 23, 16, 23, 21, 16],0)
        self.assertEqual(x,  5.237229365663817)

    def test_lab1_8_median(self):
        x =  lab1_8(3,[10, 12, 23, 23, 16, 23, 21, 16],0)
        self.assertEqual(x, 18.5)

    def test_lab1_8_median_odd(self):
        x =  lab1_8(3,[10, 12, 23, 23, 16, 23, 21, 16, 10],0)
        self.assertEqual(x, 16)

    def test_lab1_8_quartil1(self):
        x =  lab1_8(4,[10, 12, 23, 23, 16, 23, 21, 16, 10],1)
        self.assertEqual(x, 11)

    def test_lab1_8_quartil2(self):
        x = lab1_8(4, [10, 12, 23, 23, 16, 23, 21, 16, 10], 2)
        self.assertEqual(x, 16)

    def test_lab1_8_quartil3(self):
        x = lab1_8(4, [10, 12, 23, 23, 16, 23, 21, 16, 10], 3)
        self.assertEqual(x, 23)

    def test_lab1_8_quartil_invalid(self):
        self.assertRaises(ValueError, lab1_8, 7, [10, 12, 23, 23, 16, 23, 21, 16, 10],5)

    def test_lab1_8_percentile(self):
        x =  lab1_8(5,[10, 12, 23, 23, 16, 23, 21, 16, 10],30)
        self.assertEqual(x, 12)

    def test_lab1_8_percentile_invalid(self):
        self.assertRaises(ValueError, lab1_8, 7, [10, 12, 23, 23, 16, 23, 21, 16, 10],120)

    def test_lab1_8_invalid_num(self):
        self.assertRaises(ValueError, lab1_8, 7, [10, 12, 23, 23, 16, 23, 21, 16, 10],0)

    def test_lab1_9_big_num(self):
        x = lab1_9(1590)
        self.assertEqual(x, "MDXC")


if __name__ == '__main__':
    unittest.main()
