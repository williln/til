# Seeding my Wagtail site 

One of the things I'm working on right now is integrating Wagtail into a Django project. For this project, Wagtail will only be used to manage a few pages; most of the site is using regular Django models.  

I wanted to quickly create my basic set of Wagtail pages for local development, so I wouldn't need to go into the admin to recreate things. 

## Create the `Site` 

Wagtail requires you to have an active `Site`, so I added a function to retrieve one. 

```python
from wagtail.models import Site

SITE_DATA = {
    "hostname": "localhost",
    "root_page_id": 1,
    "is_default_site": True,
    "site_name": "Test Site",
}

def create_site(data: dict = None) -> Site:
    """Create a new site."""
    if Site.objects.exists():
        site = Site.objects.first()
    else:
        site = Site.objects.create(**data)
        site.save()

    return site
```

## Create a a root `Page` 

Wagtail will ship with a default root `Page`, but you can subclass `Page` to create your own homepage class (a practice Wagtail [highly recommends](https://github.com/wagtail/wagtail/issues/6294)). 

I need to see if I have a root page, and if I don't, create one and set it as the root page. 

```python
from wagtail.models import Page
from myapp.models import HomePage

def get_root_page(data: dict = None, site: Site = None) -> Page:
    """Retrieve the root page of the site."""
    slug = data.get("slug")
    try:
        root = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        # `data` contains my custom homepage fields 
        root = HomePage(**data)
        root.save()

    # Set this page as the site's root page 
    if not site.root_page:
        site.root_page = root
        site.save()

    return root
```

## Create the rest of my pages 

My use case is very simple and all pages are children of the root homepage. This code also blatantly overrides any existing root page if it finds that the page already exists. I'll probably want to make things behave a little better. 

```python
from wagtail.models import Page

def create_page(model, data, root) -> Page:
    """Create the page, and add it to the root page.
    Args:
    - model: the Wagtail page model class you're creating.
    - data: Dictionary of your page data (title, slug, etc.)
    - root: root page to set as parent to this page  
    """
    slug = data.get("slug")
    try:
        page = model.objects.get(slug=slug)
    except model.DoesNotExist:
        page = model(**data)

    parent = page.specific.get_parent()
    if parent != root:
        root.add_child(instance=page)
```

## Example in practice: 

```python
site = create_site(data=SITE_DATA)
root = get_root_page(data=ROOT_DATA, site=site)
create_page(model=MyCustomPagePage, data=PAGE_DATA, root=root)
```
