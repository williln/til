# How to sort a Python dictionary by multiple values

See [How to sort a Python dictionary by key or value](./sort_dictionary.md) for how to sort a Python dictionary at all.

Let's say we have the following dictionary and we want to sort it first in **descending** order by price, then in **ascending** order by name of the fruit or vegetable. Higher priced items would come first, and in the case of a tie, the results would be alphabetized.

```python
data = {
    "bananas": {
        "count": 3, "price": 0.50
    },
    "apples": {
        "count": 5, "price": 0.25
    },
    "cucumbers": {
        "count": 10, "price": 0.75
    },
    "artichokes": {
        "count": 13, "price": .25
    }
}
```

We follow the same principles as in the first TIL, but after `item:`, we pass a tuple of elements instead of a single element.

```python
>>> sorted_data = dict(sorted(data.items(), key=lambda item: (-item[1]["price"], item[0])))

>>> print(sorted_data)
{
    'cucumbers': {
        'count': 10, 'price': 0.75
    },
    'bananas': {
        'count': 3, 'price': 0.5
    },
    'apples': {
        'count': 5, 'price': 0.25
    },
    'artichokes': {
        'count': 13, 'price': 0.25
    }
}
```

The `-` in front of `item[1]["price"]` indicates that we want this element sorted in descending order. We see that the results of the dictionary are sorted by price from highest to lowest. In the case of a price tie (like with apples and artichokes), the results are alphabetical.
