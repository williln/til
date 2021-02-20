# Using Django Aggregation

Another thing I always have to look up.

[Django Aggregation docs](https://docs.djangoproject.com/en/3.1/topics/db/aggregation/)

## What's the highest value of some field?

```python
from django.db.models import Avg, Count, Max, Min, Sum

price_max = Model.objects.aggregate(Max("price"))
```

## What's the lowest value of some field?

```python
from django.db.models import Avg, Count, Max, Min, Sum

price_min = Model.objects.aggregate(Min("price"))
```

## What's the average value of some field?

```python
from django.db.models import Avg, Count, Max, Min, Sum

price_avg = Model.objects.aggregate(Avg("price"))
```

## What's the total of all values of a field?

```python
from django.db.models import Avg, Count, Max, Min, Sum

price_total = Model.objects.aggregate(Sum("price"))
```

## What's the difference between aggregation and annotation?

Aggregation is when you generate data across all objects in a queryset. You're looking at the queryset as a whole.

Annotation is when you generate data for each object in a queryset. You're looking at the objects in the queryset individually.

You can combine these to follow relationships -- you can **annotate** the number of editions of each `Book` in your queryset by **aggregating** the Sum of total editions of each book.

## How many of something does each item in my queryset have?

```python
from django.db.models import Avg, Count, Max, Min, Sum

# Assumes Book has a M2M for `authors`
qs = Book.objects.annotate(Count("authors"))

for book in qs:
    print(book.authors__count)
```
