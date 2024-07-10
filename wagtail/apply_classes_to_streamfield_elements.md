# Applying Tailwind classes to Wagtail StreamField elements 

## Links 

- [How to use StreamField for mixed content — Wagtail Documentation 6.1.1 documentation](https://docs.wagtail.org/en/stable/topics/streamfield.html)

## Use case 

I have a Wagtail StreamField. This is the one from the [docs]((https://docs.wagtail.org/en/stable/topics/streamfield.html)): 

```python
from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

class BlogPage(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]
```

I need the elements of the StreamField, like the `heading` and the `paragraph`, to have different Tailwind classes applied to them. 

## Solution: Apply a CSS class, then implement the Tailwind classes in the CSS file 

> Note: This TIL assumes your Tailwind setup is already configured and working. I wish I had written that TIL when I did that, but I did not. 

In my template, I added the class `custom-page` to where I render the `body`: 

```html
{% load wagtailcore_tags %}

{% for block in page.body %}
    {% if block.type == "heading" %}
        <h2 class="custom-page">{{ block.value }}</h2>
    {% elif block.type == "paragraph" %}
        <p class="custom-page">{{ block.value|richtext }}</h2>
    {% endif %}
{% endfor %}
```
