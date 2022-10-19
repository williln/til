# Using `defer()` to limit the data you get from your models 

> In some complex data-modeling situations, your models might contain a lot of fields, some of which could contain a lot of data (for example, text fields), or require expensive processing to convert them to Python objects. If you are using the results of a queryset in some situation where you don’t know if you need those particular fields when you initially fetch the data, you can tell Django not to retrieve them from the database. 

So if you have some fields that have complex or expensive data, and you won't be using those fields, you can essentially skip (or rather, "defer") retriving that data. 

```python
# Will not preload the title field 
book = Book.objects.defer("title").get(pk=1)
```

However, be mindful of N+1 queries. While you can still access that field in your object or queryset, when you do so, an extra query will be executed. 

- [`defer()`](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.query.QuerySet.defer) in the docs 
- Learned from Simon Charette in his [DjangoCon US 2022 keynote](https://2022.djangocon.us/talks/keynote-state-of-orm/)
