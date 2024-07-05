# Using `Decimal.quantize` 

## Links 

- [decimal — Decimal fixed point and floating point arithmetic — Python 3.12.4 documentation](https://docs.python.org/3/library/decimal.html)

## `quantize` 

From the docs: 

> The quantize() method rounds a number to a fixed exponent. This method is useful for monetary applications that often round results to a fixed number of places:

```python
from decimal import Decimal

Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)
Decimal('7.32')

Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)
Decimal('8')
```

## Notes

You have to call `quantize` on a `Decimal` object. You also pass it another `Decimal` object. The number of decimal places in the `Decimal` you pass to `quantize` determines the number of decimal places in your result. 

To use this with money, you might have something like: 

```python
>>> from decimal import Decimal
>>> Decimal(1989)
Decimal('1989')
>>> Decimal(1989).quantize(Decimal("00"))
Decimal('1989')
>>> Decimal(1989).quantize(Decimal(".00"))
Decimal('1989.00')
>>> Decimal(19.89).quantize(Decimal(".00"))
Decimal('19.89')
>>> Decimal(19.89).quantize(Decimal(".013"))
Decimal('19.890')
```

I don't love working with Decimals. But needs must, and discovering `quantize` was nice. 
