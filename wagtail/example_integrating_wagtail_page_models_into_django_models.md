# Example of linking Django models to Wagtail Page models 

Using Wagtail 6. 

```python
from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images.panels import ImageChooserPanel

# Assuming Category and Product models are defined in your Django app
from app.models import Category

class CategoryPage(Page):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, related_name="+")

    # Controls extra fields added to the Wagtail Admin 
    content_panels = Page.content_panels + [
        FieldPanel('category'),
    ]

```
