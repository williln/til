# Creating Custom StreamField Blocks 

## Define Your Custom Block

```python
from wagtail.core import blocks

# Extend StructBlock 
class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "blocks/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"
```

## Create a Template for Your Block

This template should be located in your templates directory under a `blocks/` subdirectory.

```html
# blocks/title_and_text_block.html
<div class="title-and-text-block">
    <h2>{{ self.title }}</h2>
    <p>{{ self.text }}</p>
</div>
```

## Add Custom Block to a `StreamField`

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

class MyCustomPage(Page):
    body = StreamField([
        ('title_and_text', TitleAndTextBlock()),
        #  add more block types here as needed
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Register Your Block (If Necessary)

Some blocks, like those intended for use with `Snippets` or specific functionalities, may need to be registered with Wagtail's admin to appear in the interface. This is not typically required for blocks used directly in `StreamFields`.

### Tips for Advanced Custom Block Development

- **JavaScript Integration**: For blocks that require dynamic user interaction in the Wagtail admin, consider adding JavaScript enhancements using the `media` class property.
- **Block Methods**: Override methods like `clean`, `value_from_datadict`, and `get_context` to customize the behavior and context data of your blocks.
- **Nested Blocks**: Custom blocks can contain other blocks, including more instances of custom blocks, allowing for highly complex data structures.
