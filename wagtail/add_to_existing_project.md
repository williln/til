# Add Wagtail to an existing Django project 

[Integrating Wagtail into a Django project](https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html)

Install Wagtail however you do dependency management. 

Add these to your `INSTALLED_APPS`: 

```python
  'wagtail.contrib.forms',
  'wagtail.contrib.redirects',
  'wagtail.embeds',
  'wagtail.sites',
  'wagtail.users',
  'wagtail.snippets',
  'wagtail.documents',
  'wagtail.images',
  'wagtail.search',
  'wagtail.admin',
  'wagtail',
  
  'modelcluster',
  'taggit',
```

Add this to `MIDDLEWARE`: 

```python
  'wagtail.contrib.redirects.middleware.RedirectMiddleware',
```


Add these other settings: 

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
WAGTAIL_SITE_NAME = 'My Example Site'
WAGTAILADMIN_BASE_URL = 'http://example.com'
```

Add the Wagtail urls to your `urls.py`: 

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    ...
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Then, run: 

```bash
./manage.py migrate 
```

And restart your server. 

