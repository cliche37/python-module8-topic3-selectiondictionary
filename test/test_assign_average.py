import unittest
from more_functions.assign_average import switch_average


class FunctionTests(unittest.TestCase):

    def test_Aanda_return_value(self):
        self.assertEqual("first", switch_average('A'))
        self.assertEqual("first", switch_average('a'))

    def test_Bandb_return_value(self):
        self.assertEqual("second", switch_average('B'))
        self.assertEqual("second", switch_average('b'))


if __name__ == "__main__":
    unittest.main()
