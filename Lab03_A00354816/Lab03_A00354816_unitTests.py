import unittest
from Lab03_A00354816 import factorial
from Lab03_A00354816 import power
from Lab03_A00354816 import filecomp
from Lab03_A00354816 import user_db

class MyTestCase(unittest.TestCase):

    def test1(self):
        f = factorial(5)
        self.assertEqual(f, 120)

    def test_expected_large(self):
        f = factorial(10)
        self.assertEqual(f, 3628800)

    def test_2(self):
        f = factorial(0)
        self.assertEqual(f, 1)

    def testneg_value(self):
        self.assertRaises(ValueError, factorial, -1)

    def test_fraction_value(self):
        self.assertRaises(ValueError, factorial, 0.5)

    # math.pow tests
    def test_expected(self):
        x = power(2,3)
        self.assertEqual(x, 8)

    def test_0pow_value(self):
        x = power(5,0)
        self.assertEqual(x, 1)

    def test_0value(self):
        x = power(0,3)
        self.assertEqual(x, 0)

    def test_double0_value(self):
        x = power(0,0)
        self.assertEqual(x, 1)

    def test_fracpow_value(self):
        x = power(4, 0.5)
        self.assertEqual(x,2.0)

    def test_frac_value(self):
        x = power(0.5, 4)
        self.assertEqual(x, 0.0625)

    def test_neg_value(self):
        x = power(-3, 6)
        self.assertEqual(x,729.0)

    def test_negpow_value(self):
        x = power(8, -1)
        self.assertEqual(x,0.125)

    def test_check_same(self):
        data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit\n'
        for name in ["file1", "file2"]:
            with open(name, 'w') as output:
                output.write(data)

        self.assertTrue(filecomp("file1", "file1"), "File compare fail")
        self.assertTrue(filecomp("file1", "file2"), "File compare fail")

    def test_check_diff(self):
        data = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit\n'
        for name in ["file1", "file2"]:
            with open(name, 'w') as output:
                output.write(data)

        with open("file2", 'a+') as output:
            output.write('Difference is here.\n')

        self.assertFalse(filecomp("file1", "file2"), "File compare fail")

    def test_addrecord(self):
        user_db.newRecord(user_db, "mayra","molina@gmail.com","26","mexico")
        self.assertTrue(user_db.searchRecordName(user_db,"mayra"))

    def test_addrecord2(self):
        user_db.newRecord(user_db, "john","mdoe@gmail.com","30","usa")
        self.assertTrue(user_db.searchRecordName(user_db,"john"))

    def test_removerecord(self):
        user_db.deleteRecord(user_db, "john","mdoe@gmail.com","30","usa")
        self.assertFalse(user_db.searchRecordName(user_db,"john"))

if __name__ == '__main__':
    unittest.main()
