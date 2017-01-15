import re
import argparse


def format_price(price):
    if not isinstance(price, str) or not re.match('[0-9]+([.][0-9]*)?|[.][0-9]+$', price):
        return None

    if float(price).is_integer():
        return '{:,}'.format(int(price)).replace(',', ' ')
    else:
        return '{:,.2f}'.format(float(price)).replace(',', ' ')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=str, help='Input price')

    args = parser.parse_args()
    print(format_price(args.price))
