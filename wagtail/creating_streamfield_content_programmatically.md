# Creating Wagtail pages with Streamfield content programmatically 

As part of [Seeding my Wagtail site](https://github.com/williln/til/blob/main/wagtail/seeding_wagtail_site.md), I need to create some initial StreamField content. 

One of the pages I need to create is a Privacy Policy, which is an instance of my `SimplePage` page model: 

```python
# my_app/models.py
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from django.db import models

class SimplePage(Page):
    body = StreamField(
        [
            ("heading", blocks.CharBlock(),
            ("paragraph", blocks.RichTextBlock()),
        ]
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    template = "core/simple_page.html"
```

For reference, here is the [Python.org Privacy Policy](https://www.python.org/privacy/). Let's create this page: 

```python
from my_app.models import SimplePage
from my_app.utils import create_page, get_root_page


PRIVACY_PAGE_DATA = {
    "slug": "privacy",
    "title": "Privacy Policy",
    "body": [
        {"type": "heading", "value": "Python Software Foundation Privacy Policy", "id": "1"},
        {"type": "paragraph", "value": "The Python Software Foundation (the “PSF”) is is dedicated to...", "id": "2"},
        {"type": "paragraph", "value": "By visiting PSF websites or are otherwise providing...", "id": "3"},
        {"type": "paragraph", "value": "This privacy policy will govern our use of your information, regardless of...", "id": "4"},
        {"type": "heading", "value": "1. What information do we collect?", "id": "5"},
    ],
}

# retrive the root page 
root = get_root_page()

# Create the privacy page with the StreamField data
create_page(model=SimplePage, data=PRIVACY_PAGE_DATA, root=root)
```

You can see `create_page()` in [Seeding my Wagtail site](https://github.com/williln/til/blob/main/wagtail/seeding_wagtail_site.md#create-the-rest-of-my-pages). 
