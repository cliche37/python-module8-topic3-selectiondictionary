import unittest
from more_functions.assign_average import switch_average


class FunctionTests(unittest.TestCase):

    def test_Aanda_return_value(self):
        self.assertEqual('first', switch_average('A'))
        self.assertEqual('first', switch_average('a'))

    def test_Bandb_return_value(self):
        self.assertEqual('second', switch_average('B'))
        self.assertEqual('second', switch_average('b'))

    def test_Candc_return_value(self):
        self.assertEqual('third', switch_average('C'))
        self.assertEqual('third', switch_average('c'))

    def test_Dandd_return_value(self):
        self.assertEqual('fourth', switch_average('D'))
        self.assertEqual('fourth', switch_average('d'))

    def test_Eande_return_value(self):
        self.assertEqual('fifth', switch_average('E'))
        self.assertEqual('fifth', switch_average('e'))

    def test_nonkey_input(self):
        self.assertEqual('Input not found', switch_average('z'))

if __name__ == "__main__":
    unittest.main()