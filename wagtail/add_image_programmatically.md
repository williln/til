# Adding a Wagtail image programmatically 

See [Seeding a Wagtail site](./seeding_wagtail_site.md) for a related TIL.

## Use case 

I have a seed script for my client to pre-load their main Wagtail content pages (things like the Team page, etc.). This will cut down on the amount of manual work they have to do when they go live. 

I want to be able to add images via that script. Here's how I did it. 

## Process

1. Add your image file however you do that. Mine live in `static/imgs/`. 
2. Add an image field to your Wagtail model 
3. Get or create your image based on the image path 
4. Save the image to the Wagtail page 

## Add an image field to your Wagtail model 

```py
from wagtail.models import Page
from django.db import models 

class MyPage(Page):
    image = models.ForeignKey(
         "wagtailimages.Image",
         null=True,
         blank=True,
         on_delete=models.SET_NULL,
         related_name="+",
     )
     # Other fields 

     panels = [
        FieldPanel("image"),
    ]
```

## Get or create your image based on the image path 

The place where this might be different for you is in the logic for how the code finds the image. My actual code was a little more complex than this due to how that project handles static files, so this is a simpler example. 

```py
import os 
from django.conf import settings
from wagtail.images.models import Image


def create_image_from_file(file_path):
    """Create a Wagtail image from a file path."""
    with open(file_path, "rb") as file:
        image_name = os.path.basename(file_path)
        image = Image(title=image_name)
        image.file.save(image_name, file)
        return image


def get_or_create_image(image_path):
    """Retrieves and returns a Wagtail image from a file path."""

    # Try and find your image path in your static files 
    for static_dir in settings.STATICFILES_DIRS:
        full_path = os.path.join(static_dir, image_path)
        # When you find it, stop
        if os.path.exists(full_path):
            break
    else:
        raise FileNotFoundError(f"File not found: {full_path}")

    # Define a filename for the image 
    image_name = os.path.basename(full_path)

    # Save the image as a Wagtail image 
    try:
        image = Image.objects.get(title=image_name)
    except Image.DoesNotExist:
        image = create_image_from_file(full_path)

    return image
```

## Save the image to the Wagtail page  

```py
from my_app.utils import get_or_create_image
from my_app.models import MyPage 

page = MyPage.objects.get(slug="my-slug")
image = get_or_create_image("path/to/my/image.jpg")
page.image = image 
page.save()
```

There you go! 