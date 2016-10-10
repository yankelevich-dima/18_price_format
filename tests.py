import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):

    def test_not_correct_value(self):
        price = 'NotCorrectValue'
        with self.assertRaises(ValueError):
            format_price(price)

    def test_not_correct_type(self):
        price = [192, 00]
        with self.assertRaises(TypeError):
            format_price(price)

    def test_correct_formatting(self):
        price = '109961'
        result_price = '109 961'
        self.assertEqual(format_price(price), result_price)


if __name__ == '__main__':
    unittest.main()
