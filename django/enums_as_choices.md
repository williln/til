# Using Enums in a Django Model ChoiceField (Django 2.2)

## What is an Enum?

An enum, short for "enumeration," is a set of related values. To collect all the sizes of pizza that a restaurant offers, you might use an enum `PizzaSizes`:

```python
from enum import Enum


class PizzaSizes(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
```

By convention, the members (`SMALL`, `LARGE`, etc.) of an enum class are in all-caps; they're treated kin of like constants this way.

The values of the enum members can be any valid Python "thing": a string, int, dictionary, whatever.

Each member of the enum is its own instance, so `PizzaSizes.SMALL` won't return `"small"`. It will return `<PizzaSizes.SMALL: 'small'>`. To get to the value of the member, you need to access `PizzaSizes.SMALL.name`.

```bash
>>> PizzaSizes.LARGE
<PizzaSizes.LARGE: 'large'>
>>> PizzaSizes.LARGE.name
'LARGE'
```

## Using for Django's ModelChoiceFields

I've always used model-level constants for ChoiceFields in Django models, something like:

```python
class Pizza(models.Model):
    PIZZA_SMALL = "small"
    PIZZA_MEDIUM = "medium"
    PIZZA_LARGE = "large"
    PIZZA_SIZES = (
        (PIZZA_SMALL, "Small"),
        (PIZZA_MEDIUM, "Medium"),
        (PIZZA_LARGE, "Large")
    )

    name = models.CharField(max_length=50)
    size = models.CharField(choices=PIZZA_SIZES)
```

But in the situation where you want to reuse these values in other places, and/or the values aren't specific to this model class, you can use enums instead.

```python
class Pizza(models.Model):

    name = models.CharField(max_length=50)
    size = models.CharField(choices=[
        (enums.PizzaSizes.SMALL, "Small"),
        (enums.PizzaSizes.MEDIUM, "Medium"),
        (enums.PizzaSizes.LARGE, "Large")
    ])
```

## In Django 3.0

Django 3.0 does even better: It allows you to set enum-like choices at the model level that include the display text:

```python
from django.utils.translation import gettext_lazy as _


class Pizza(models.Model):

    class PizzaSizes(models.TextChoices):
        SMALL = "small", _("Small")
        MEDIUM = "medium", _("Medium")
        LARGE = "large", _("Large")

    name = models.CharField(max_length=50)
    size = models.CharField(choices=PizzaSizes.choices)
```

## Further Reading

- [Python Docs: `enum`](https://docs.python.org/3/library/enum.html)
- [Django Docs: `choices`](https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices)
- [Django 3.0 Docs on Enumeration Types](https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types)
