# Cheat Sheet for Wagtail StreamField

## Using StreamField 

First, you define the blocks you want to use. For this example, we'll create a simple blog post page that can contain text, images, and embedded videos.

```python
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.blocks import RichTextBlock, StructBlock, URLBlock, ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

# Define a custom StructBlock for embedded videos
class VideoBlock(StructBlock):
    url = URLBlock(help_text="URL of the video")
    caption = RichTextBlock(required=False)

    class Meta:
        icon = "media"
        template = "blocks/video_block.html"
```

Next, incorporate the StreamField into your page model. You can mix and match any blocks defined previously or provided by Wagtail by default.

```python
class BlogPage(Page):
    body = StreamField([
        ('heading', RichTextBlock(icon="title", template="blocks/heading_block.html")),
        ('paragraph', RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        # List the custom video block as one of the StreamField block options
        ('video', VideoBlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```
## Custom Templates for Custom Blocks 

For each block, you can define a template that controls how the block is rendered on the page. 

```html
# blocks/video_block.html
{% if self.url %}
    <div class="video-block">
        <iframe src="{{ self.url }}" frameborder="0" allowfullscreen></iframe>
        {% if self.caption %}
            <div class="caption">{{ self.caption|richtext }}</div>
        {% endif %}
    </div>
{% endif %}

```

## Built-In StreamField Blocks 

### Basic Blocks

- **CharBlock**: A single line of text.
- **TextBlock**: A multi-line text area.
- **RichTextBlock**: A WYSIWYG editor for rich text content.
- **BooleanBlock**: A true/false checkbox.
- **IntegerBlock**: For integers.
- **FloatBlock**: For floating-point numbers.
- **DecimalBlock**: For decimal numbers.
- **RegexBlock**: Validates text against a regular expression.
- **URLBlock**: For URLs.
- **DateBlock**: For dates.
- **DateTimeBlock**: For dates and times.
- **TimeBlock**: For times.
- **EmailBlock**: For email addresses.
- **ChoiceBlock**: Dropdown of specified choices.
- **PageChooserBlock**: Allows choosing a Wagtail page.
- **DocumentChooserBlock**: For choosing a document from the document library.
- **ImageChooserBlock**: For choosing an image from the image library.
- **SnippetChooserBlock**: For choosing an instance of a registered Snippet model.
- **StaticBlock**: Renders a template with no context.

### Structured Blocks

- **StructBlock**: Groups together a fixed set of sub-blocks as a single logical block.
- **ListBlock**: A list of blocks all of the same type.
- **StreamBlock**: A list of blocks that can be of multiple types, chosen from a predefined set.

### Field Blocks

These are blocks that mirror Django's model fields:

- **BlockQuoteBlock**: Specifically for block quotes (not a direct Django model field but common in content).
- **ChoiceBlock**: Mirrors `models.ChoiceField` with a set of choices.

### Specialty Blocks

- **RawHTMLBlock**: For raw HTML input.
- **TableBlock**: For tabular data.
- **SequenceBlock**: Similar to `ListBlock`, but for a sequence of blocks.

### Advanced Blocks

- **EmbedBlock**: Embeds content from URLs (e.g., YouTube, Twitter) via the `embed` framework.
- **StaticLiveBlock**: A variant of `StaticBlock` designed for use with live content.

### Example Usage

```python
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class MyStreamBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    date = blocks.DateBlock()

    class Meta:
        template = "myapp/blocks/my_stream_block.html"
```

And then add the `StreamField` to a Wagtail Page model:

```python
class MyPage(Page):
    body = StreamField(MyStreamBlock(), null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
```
