# Why won't my Django file URLs come back signed from S3?

This week, I needed to do several things:

- Add a file field to a Django model
- Make sure files uploaded to that field were stored in a private Amazon S3 bucket
- Return the URLs for those files as [signed URLs](https://cloud.google.com/storage/docs/access-control/signed-urls)

I was using [Storing Django Static and Media Files on Amazon S3](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) by Michael Herman, and it's a really excellent resource. Essentially, his code examples are what I had, but we already had this repo set up to use a public S3 bucket so my settings were slightly different:

```python
# config/storage_backends.py
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_STORAGE_BUCKET_NAME
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False


# config/settings.py
USE_S3 = os.getenv('USE_S3') == 'TRUE'

if USE_S3:
    # aws settings
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_QUERYSTRING_AUTH = False
    # s3 private media settings
    AWS_PRIVATE_STORAGE_BUCKET_NAME = os.getenv('AWS_PRIVATE_STORAGE_BUCKET_NAME')
    PRIVATE_FILE_STORAGE = 'config.storage_backends.PrivateMediaStorage'
    # s3 static settings
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_IS_GZIPPED = True


# my_app/models.py
from django.db import models
from config.storage_backends import PrivateMediaStorage

class Upload(models.Model):
    image = models.FileField(storage=PrivateMediaStorage())
```

This all worked great, except no matter what settings I tried, my URLs for `Upload.image` were not coming back signed, and so I was not able to access the image from S3. I looked through the django-storages documentation and beat my head against this wall, and then I did the smart thing: I asked for help.

A coworker pointed out that we had `AWS_QUERYSTRING_AUTH` set to `False` globally, and the [base `S3Boto3Storage` class](https://github.com/jschneier/django-storages/blob/master/storages/backends/s3boto3.py#L298) I was overriding for my `PrivateMediaStorage` class retrieved the value for its `querystring_auth` from this global value (with a default of `True`). So we weren't getting a signed URL because we were telling Django that we didn't want one.

The solution was to add the attribue `querystring_auth` to the custom private storage class, so the final custom class looked like this:

```python
class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_STORAGE_BUCKET_NAME
    default_acl = "private"
    file_overwrite = False
    custom_domain = False
    querystring_auth = True
```

Then I received valid, signed URLs back from S3 and was able to move on with my life.

## Versions

- Django 2.2
- django-storages 1.11
- boto3 1.11.12
