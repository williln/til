# How I added a very simple django-streamfield example to a project

## Info 

- [django-streamfield on PyPI](https://pypi.org/project/django-streamfield/)
- [django-streamfield on GitHub](https://github.com/raagin/django-streamfield)
- Django 5.0
- Python 3.11 
- Docker development environment

## Steps 

This outlines what I did for my own local setup. Your own setup might be different. 

### Installation and setup 

1. Install `django-streamfield` with `pip-compile` 
2. Rebuild my Docker image 
3. Exec into my Docker shell 
4. Run `./manage.py startapp streamblocks` and add the `streamblocks` and `streamfield` apps to `settings.INSTALLED_APPS`

### Create some stream blocks 

I did some research to confirm that I did need to write all my own blocks from scratch, and that does seem to be the case. 

1. Following the [tutorial](https://github.com/raagin/django-streamfield?tab=readme-ov-file#how-to-use), add a `RichText` model in `streamblocks/models.py`
2. Add my own `QuoteBlock` model. 

```python
# streamblocks/models.py
from django.db import models

from django_extensions.db.models import TimeStampedModel

class RichTextBlock(TimeStampedModel):
    text = models.TextField(blank=True
  
  
class QuoteBlock(TimeStampedModel):
    quote = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)

STREAMBLOCKS_MODELS = [
    RichTextBlock,
    QuoteBlock,
]
```

I also added both blocks to a `STREAMBLOCKS_MODELS` setting in the same file. 

3. Run `makemigrations ` and `migrate`
4. Add `streamfield` urls to `urls.py` per the instructions: 

```python
# config/urls.py 
urlpatterns += [
    path('streamfield/', include('streamfield.urls'))
]
```

5. Add some simple templates for the new blocks. The `/templates/streamblocks/`

```html
<!-- templates/streamblocks/blocks/richtext.html -->
<div class="rich-text-block">
    {{ block_content.text|safe }}
</div>
```

```html
<!-- templates/streamblocks/quote.html -->
<div class="quote-block">
    <div>"{{ block_content.quote|safe }}"</div>
    <div>{{ block_content.author|safe }}</div>
</div>
```

6. Add my template names as attributes to the block models, which did not require a migration: 

```python
# streamblocks/models.py 
class RichTextBlock(TimeStampedModel):
    block_template = "streamblocks/richtext.html"
```

### Add the StreamField to my model 

The use case is a proof of concept for using this project for an e-commerce site. 

1. Add my blocks to the model that I wanted to use the StreamField. In this case, I wanted to add an "extra info" field that would use both blocks. 

```python
from streamfield.fields import StreamField
from streamblocks.models import RichTextBlock, QuoteBlock

class Product(TimeStampedModel):
    stream = StreamField(
        model_list=[RichTextBlock, QuoteBlock],
        verbose_name="Extra Info Blocks",
        help_text="A special notice for this product.",
	)
```

I ran `makemigrations` and `migrate` again. 

2. I started my local dev server so I could try and add some data to one of my Product objects via the Django admin. I'm not adding screenshots (lazy), but I can tell you that while the UI isn't totally intuitive out of the box, it did work fine. I saved my changes. 
3. I added the new streamfield block to the product template. 

```html
<!-- templates/products/product_detail.html -->

<!-- rest of my template -->
<div>special notice: {{ object.stream.render }}</div>
```

### Test the block models 

Anytime I create a new model, I like to create a basic canary test for it.

```python
# streamblocks/tests/fixtures.py
from __future__ import annotations

import pytest
from model_bakery import baker

@pytest.fixture
def rich_text_block(db):
    return baker.make("streamblocks.RichTextBlock", text="Hello, world!")
```

```python
# streamblocks/tests/test_models.py
def test_rich_text_block(rich_text_block):
    assert rich_text_block.text == "Hello, world!"
```

### Test the Streamfield on the Product model 

This one was trickier, and I want to thank [@FunkBob](https://chaos.social/@FunkyBob/112119091650686006) on Mastodon for helping me figure out how to set this test up. The object with the Streamfield must be reloaded from the db before you can access the `add` method on the Streamfield field to add the blocks. 

```python
# products/tests/test_models.py

# uses pre-existing item fixture 
def test_item_stream(item, rich_text_block):
    # The object has to be reloaded to access the StreamField
    item.refresh_from_db()
    item.stream.add(rich_text_block)
    assert len(item.special_notice.value) == 1
    ids = set([block["id"] for block in item.special_notice.value])
    assert rich_text_block.id in ids
    assert quote_block.id in ids
```

This isn't the most useful test, but I will probably have some more complex streamfield logic later, so I will probably appreciate having written an example test. 
