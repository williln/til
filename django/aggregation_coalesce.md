# Using `Coalesce` to provide a default value for `aggregate` queries

My client [Sean](https://github.com/seanpar203) told me about `Coalesce` in a PR of mine he reviewed recently. I was fixing a bug that happened when the result of an `aggregate` `Sum` query came back as `None`, but I was doing it with some conditional logic. He suggested I look at using `Coalesce` instead!

[Django Docs on Coalesce](https://docs.djangoproject.com/en/2.2/ref/models/database-functions/#coalesce)

```python
>>> # Get a screen name from least to most public
>>> from django.db.models import Sum, Value as V
>>> from django.db.models.functions import Coalesce

>>> # Prevent an aggregate Sum() from returning None
>>> aggregated = Author.objects.aggregate(combined_age=Coalesce(Sum('age'), V(0))
>>> print(aggregated['combined_age'])
0
```

If the result of your `aggregate` query would have been a null value, you can wrap your expression (in this case `Sum`) in `Coalesce` and use `Value` (as `V` in their example) to provide a default value instead.

A lot simpler than wrapping your result in an `if/else` before you return the value!
