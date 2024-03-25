# What to do if you delete the default Wagtail homepage 

**NOTE**: The project this was for is in its beginning stages and the intent of this TIL was to get me past a bug.

What to do if you delete the default Wagtail homepage and don't have a custom Homepage class? 

Answer: Create a custom home page class and use that to create a new homepage. Wagtail apparently really, really expects you to have a custom Wagtail homepage, even if you are integrating Wagtail into an existing Django project and don't intend to use Wagtail to maintain the homepage.

I wound up in the situation described in [this comment](https://github.com/wagtail/wagtail/issues/6294#issue-673435282). 

In scrolling, I came upon the [explanation](https://github.com/wagtail/wagtail/issues/6294#issuecomment-669128941) in a further comment, and the instruction for what to do: 

> Ah - I see that the original poster on Reddit is following the "Integration with Django" steps, so their codebase won't have the HomePage model defined. As a result, there are no page types available to create. Once they've installed Wagtail into their project, they need to continue following the main tutorial from here: https://docs.wagtail.io/en/v2.9.3/getting_started/tutorial.html#extend-the-homepage-model

In reading the comments, it seems very clear that Wagtail strongly intends this behavior. Although there are workarounds in the thread, I opted to create a simple custom Homepage that inherits from the `Page` class. 

```python
from __future__ import annotations

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    template = "homepage.html"
```

My existing homepage logic that uses `homepage.html` is still intact. 

This way, if I accidentally delete the default page, I can re-add another one easily. 
