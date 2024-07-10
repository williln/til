# Using `iterator()` to loop through large querysets efficiently 

## Links 

- [`iterator()` in the Django docs](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#iterator)

## Use case 

I learned this when I reviewed a PR from my colleague Jeff. We needed to loop through about 40k records to reset some data. 

> 💡 Side note: This is one of the reasons PR review is helpful -- cross-training!

From the docs: 

> A QuerySet typically caches its results internally so that repeated evaluations do not result in additional queries. In contrast, iterator() will read results directly, without doing any caching at the QuerySet level (internally, the default iterator calls iterator() and caches the return value). For a QuerySet which returns a large number of objects that you only need to access once, this can result in better performance and a significant reduction in memory.

## Code example

```py
from my_app.models import MyModel

# Perform whatever query you need 
qs = MyModel.objects.all()

# Loop over it with `iterator`
for obj in qs.iterator():
    # whatever you needed to do in this loop 
```
