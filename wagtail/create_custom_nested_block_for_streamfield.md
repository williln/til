# Create a Custom Nested Block for Wagtail StreamField 

- allows for more complex data structures within a `StreamField`
- common use case for a custom nested block is a "Card" layout, where each card contains an image, a title, a short text, and an optional link
- Featured products, team members, etc. 

## Define blocks 

```python
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# Individual blocks to be nested
class TitleBlock(blocks.CharBlock):
    class Meta:
        template = "blocks/title_block.html"

class TextBlock(blocks.TextBlock):
    class Meta:
        template = "blocks/text_block.html"

# Main nested block
class CardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = TitleBlock(required=True, max_length=100)
    text = TextBlock(required=True, max_length=400)
    link = blocks.URLBlock(required=False)

    class Meta:
        template = "blocks/card_block.html"
        icon = "placeholder"
```

## Create Templates for Your Blocks

For each custom block, especially the `CardBlock`, you need to create a corresponding template that defines how the block should be rendered. Place these templates in your templates directory, under a `blocks` folder for organization.

**Title Block Template (`title_block.html`):**

```html
<h2>{{ value }}</h2>
```

**Text Block Template (`text_block.html`):**

```html
<p>{{ value }}</p>
```

**Card Block Template (`card_block.html`):**

```html
<div class="card">
    <img src="{{ value.image.url }}" alt="{{ value.title }}">
    {% include "blocks/title_block.html" with value=value.title %}
    {% include "blocks/text_block.html" with value=value.text %}
    {% if value.link %}
        <a href="{{ value.link }}">Learn More</a>
    {% endif %}
</div>
```

## Integrate the Nested Block into a Page

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from .blocks import CardBlock

class HomePage(Page):
    content = StreamField([
        ('cards', CardBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]
```

Run migrations: 

```shell
python manage.py makemigrations
python manage.py migrate
```
