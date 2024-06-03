# Using inline formsets with `inlineformset_factory`

## Links 

- [Creating forms from models | Django documentation | Django 5.0](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#inline-formsets)

I'm going to let the Django docs do a lot of the heavy lifting in this TIL and quote them liberally: 

## Simplest example 

Assume these models: 

```python
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```

> If you want to create a formset that allows you to edit books belonging to a particular author, you could do this:


```bash
>>> from django.forms import inlineformset_factory
>>> BookFormSet = inlineformset_factory(Author, Book, fields=["title"])
>>> author = Author.objects.get(name="Mike Royko")
>>> formset = BookFormSet(instance=author)
```


## Scenario: I need to change the behavior of the `InlineFormSet` 

Subclass `BaseInlineFormSet` and override the method: 

```python
from django.forms import BaseInlineFormSet


class CustomInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        # example custom validation across forms in the formset
        for form in self.forms:
            # your custom formset validation
            ...
```

Then, when creating the formset, pass your custom formset as an argument to `inlineformset_factory`: 

```bash
>>> from django.forms import inlineformset_factory
>>> BookFormSet = inlineformset_factory(
...     Author, Book, fields=["title"], formset=CustomInlineFormSet
... )
>>> author = Author.objects.get(name="Mike Royko")
>>> formset = BookFormSet(instance=author)
```

## Scenario: Your model contains for than one foreign key field to the same model 

Example: a `Friendship` model: 

```python
class Friendship(models.Model):
    from_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="from_friends",
    )
    to_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="friends",
    )
    length_in_months = models.IntegerField()
```

To solve, pass the `fk_name` argument to `inlineformset_factory`: 

```bash
>>> FriendshipFormSet = inlineformset_factory(
...     Friend, Friendship, fk_name="from_friend", fields=["to_friend", "length_in_months"]
... )
```

## Scenario: Use the inline formset in a view 


```python
def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=["title"])
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(author.get_absolute_url())
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request, "manage_books.html", {"formset": formset})
```
