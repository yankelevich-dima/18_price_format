# 18_price_format

## About:

This script converts string like `19234.000` into nice looking price format `19 234`  
Also float price will round to 2 digits:

## Usage:

 - Import price format function using `from format_price import format_price`
 - Or run script `python format_price.py <price>`

Note that incorrect value passed in `format_price` function will return `None`.


## Examples:

```
python format_price.py 19234.000
19 234

python format_price.py 19234.1
19 234.10

python format_price.py 19234.119
19 234.12
```


## How to run tests:

 - Run `python tests.py`
