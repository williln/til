# Finding out how many objects have N connections to the other model in a M2M relationship 

Assume we have a model `Item` with a ManyToMany field to `Category` through `ItemCategory`. 

```python
class Category(models.Model):
...

class Item(models.Model):
    categories = models.ManyToManyField("Category", through="ItemCategory"...)

class ItemCategory(models.Model):
    item = models.ForeignKey("Item"...)
    category = models.Category("Category"...)
```

We want to know how many Items do not have any Categories. 

```python
from django.db.models import Count
from items.models import Item

# Annotate each item with the count of related categories
items_with_category_count = Item.objects.annotate(categories_count=Count('categories'))

# Filter items that have zero categories
items_with_zero_categories = items_with_category_count.filter(categories_count=0)

# Get the count of items with zero categories
count_of_items_with_zero_categories = items_with_zero_categories.count()

print(count_of_items_with_zero_categories)
```
