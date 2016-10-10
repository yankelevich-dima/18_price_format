import re
import argparse


def format_price(price):
    if not isinstance(price, str):
        raise TypeError('Price should be str')
    if not re.match('[0-9]+([.][0-9]*)?|[.][0-9]+$', price):
        raise ValueError('Price should be int or float format')
    price = int(float(price))
    return '{:,}'.format(price).replace(',', ' ')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=str, help='Input price')

    args = parser.parse_args()
    print(format_price(args.price))
