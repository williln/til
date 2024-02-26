# Cheat Sheet: Wagtail Page Model Fields 

## CharField 

A text field for short-to-medium length strings.

```python

from wagtail.admin.panels import FieldPanel

class MyPage(Page):
    title = models.CharField(max_length=255)
    
    content_panels = Page.content_panels + [
        FieldPanel('title'),
    ]
```

## TextField

A large text field for longer blocks of text.

```python
class MyPage(Page):
    body = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

## RichTextField

Allows for rich text formatting (e.g., bold, italic, links).

```python

from wagtail.fields import RichTextField

class MyPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
```

## DateField

For dates.

```python

class MyPage(Page):
  publish_date = models.DateField()
  
  content_panels = Page.content_panels + [
      FieldPanel('publish_date'),
  ]
```

## DateTimeField

For dates and times.

```python
class MyPage(Page):
    event_datetime = models.DateTimeField()

    content_panels = Page.content_panels + [
        FieldPanel('event_datetime'),
    ]
```

## BooleanField

A true/false field.

```python
class MyPage(Page):
    is_published = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('is_published'),
    ]
```
## ImageField

For images. Requires configuring an image chooser panel.

```python

from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel

class MyPage(Page):
  cover_image = models.ForeignKey(
      Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
  )

  content_panels = Page.content_panels + [
      ImageChooserPanel('cover_image'),
  ]
```

## ForeignKey

To link to another model (e.g., a category or author).

```python

from django.db import models
from wagtail.admin.panels import FieldPanel

category = models.ForeignKey('app.Category', null=True, blank=True, on_delete=models.SET_NULL)

class MyPage(Page):
  content_panels = Page.content_panels + [
      FieldPanel('category'),
  ]
```

## ManyToManyField

For relationships where an instance can belong to multiple categories.

```python
class MyPage(Page):
    tags = models.ManyToManyField('app.Tag', related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
    ]
```

## StreamField

A flexible field for managing a sequence of content blocks.

```python

from wagtail.blocks import TextBlock, StructBlock, StreamBlock, CharBlock, RichTextBlock
from wagtail.fields import StreamField

class MyStreamBlock(StreamBlock):
    heading = CharBlock(form_classname="full title")
    paragraph = RichTextBlock()
    # Add more blocks as needed

class MyPage(Page):
  body = StreamField(MyStreamBlock(), null=True, blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('body'),
  ]
```
