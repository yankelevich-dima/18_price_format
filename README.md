# 18_price_format

## About:

This script converts string like `19234.000` into nice looking price format `19 234`  

## Usage:

 - Import price format function using `from format_price import format_price`
 - Or run script `python format_price.py <price>`

Note that incorrect value passed in `format_price` function will raise ValueError.  
Also incorrect type (all but str) will raise TypeError.

## How to run tests:

 - Run `python tests.py`
