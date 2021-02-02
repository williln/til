# How to sort a Python dictionary by key or value

To sort a dictionary by key, consider this dictionary:

```python
data = {"bananas": 3, "apples": 5, "cucumbers": 10, "artichokes": 13}
```

To sort by **key**, try using `sorted` together with `lambda`:

```python
>>> sorted_data = dict(sorted(data.items(), key=lambda item: item[0]))

>>> print(sorted_data)
{'apples': 5, 'artichokes': 13, 'bananas': 3, 'cucumbers': 10}
```

To sort by **value**:

```python
>>> sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

>>> print(sorted_data)
{'bananas': 3, 'apples': 5, 'cucumbers': 10, 'artichokes': 13}
```

Note the index at the end of the lambda expression. When you sort by `item[0]`, you're sorting by the first element returned by `data.items()`.

```python
>>> data.items()
dict_items([('bananas', 3), ('apples', 5), ('cucumbers', 10), ('artichokes', 13)])
```

`.items()` returns a list of tuples. The first element in each tuple is the key, and the second is the value. When you sort by `item[0]`, you're sorting by the key (so sorting alphabetically, in our case). When you sort by `item[1]`, you're sorting by the value (so sorting numerically in this example).

## Sorting a dictionary of dictionaries by a value in the nested dictionary

Consider this dictionary:

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
        "count": 13, "price": 2.50
    }
}
```

Say we wanted to sort by price. We can use the same logic as above, but we need to make sure of two things:

- We are accessing the value, since we need to sort by something in the nested dictionary
- We are accessing the `price` element inside that dictionary

```python
>>> dict(sorted(data.items(), key=lambda item: item[1]["price"]))
{
    'apples': {
        'count': 5, 'price': 0.25
    },
    'bananas': {
        'count': 3, 'price': 0.5
    },
    'cucumbers': {
        'count': 10, 'price': 0.75
    },
    'artichokes': {
        'count': 13, 'price': 2.5
    }
}
```

