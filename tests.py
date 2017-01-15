import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_not_correct_value(self):
        price = 'NotCorrectValue'
        self.assertIsNone(format_price(price))

    def test_not_correct_type(self):
        price = [192, 00]
        self.assertIsNone(format_price(price))

    def test_correct_formatting_int(self):
        price = '109961'
        result_price = '109 961'
        self.assertEqual(format_price(price), result_price)

    def test_correct_formatting_float(self):
        price = '109961.1'
        result_price = '109 961.10'
        self.assertEqual(format_price(price), result_price)

    def test_correct_rounding_float(self):
        price = '109961.119'
        result_price = '109 961.12'
        self.assertEqual(format_price(price), result_price)

if __name__ == '__main__':
    unittest.main()
