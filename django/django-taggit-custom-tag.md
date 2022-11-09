# Adding a custom tag with `django-taggit` 

For a side project to manage my fanfiction TBRs, I'm using `django-taggit` to import the tags from AO3. But I do plan to use this to create more TILs and potentially some tutorials, and... not all tags would potentially be professional. 

So I wanted to add a field that would let me indicate which tags I could hide when showing these tags to an API or a web UI. 

It turns out the [`django-taggit` docs](https://django-taggit.readthedocs.io/en/latest/custom_tagging.html#custom-tag) are quite clear about how to do this, and my implementation worked in no time at all. 

## Create a custom tag model and add your extra fields 

```python
# models.py 
from django.db import models
from django.utils.translation import gettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class MyCustomTag(TagBase):
    hide = models.BooleanField(default=False

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
```

## Create a through model 

If you need a refresher on what a "through" model is, the ["You might need a custom through model"](https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/) section of my article, "Tips for Using Django's ManyToManyField" from 2018 is still accurate.

```python
# models.py

class TaggedFic(GenericTaggedItemBase):
    # TaggedFic can also extend TaggedItemBase or a combination of
    # both TaggedItemBase and GenericTaggedItemBase. GenericTaggedItemBase
    # allows using the same tag for different kinds of objects, in this
    # example Fic.

    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(
        MyCustomTag,
        on_delete=models.CASCADE,
        related_name="tags",
    )
```

## Add your through model to the manager 

```python
# models.py

class Fic(models.Model):
    # ... fields here

    tags = TaggableManager(through=TaggedFic)
````

## Prove it to yourself 

Now you can do things like: 

```python
$ from model_bakery import baker
$ from .models import Fic

$ fic = baker.make("fics.Fic")
$ tag = baker.make("fics.MyCustomTag", hide=True)
$ fic.tags.add(tag)
$ Fic.objects.filter(tags__hide=True).exists()
True 
$ fic.tags.filter(hide=True).exists()
True
```
