# How to test a file upload with `pytest` and 'SimpleUploadedFile`

Situation: A user can upload a new profile photo. We want to test that they can actually do that.

This is another thing I know I've done before, but after spending several years almost exclusively with APIs, I wanted to write it down so I can copy and paste it forever! 

- Django 3.2 
- Python 3.10 
- Project uses `pytest` and `django-test-plus` 
- Stackoverflow: [How to Unit Test File Upload in Django](https://stackoverflow.com/questions/11170425/how-to-unit-test-file-upload-in-django)
- [Unit Testing File Objects in Django with SimpleUploadedFile](https://blog.kinsacreative.com/articles/unit-testing-file-objects-django/)
- [Testing Files with Python/Django](https://swapps.com/blog/testing-files-with-pythondjango/)

## Stackoverflow snippet 

```python
from django.core.files.uploadedfile import SimpleUploadedFile

def test_upload_video(self):
    video = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
    self.client.post(reverse('app:some_view'), {'video': video})
```

I tried a pretty close version of this, but got this error: `AttributeError: 'SimpleUploadedFile' object has no attribute 'items'`. Researching that error led me to this post: https://swapps.com/blog/testing-files-with-pythondjango/, which reminded me of `override_settings`: 

This is the code that finally worked: 

```python
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings


@override_settings(MEDIA_ROOT=tempfile.gettempdir())
def test_profile_photo_update_success(tp, user, client):
    old_image = user.image
    client.force_login(user)
    image = SimpleUploadedFile(
        "/image/fpo/user.png", b"file_content", content_type="image/png"
    )
    res = tp.post("profile-photo", data={"image": image})
    tp.response_302(res)
    assert f"/my/expected/redirect/url" in res.url
    user.refresh_from_db()
    assert user.image != old_image
```

- `tp` is the `django-test-plus` fixture
- `user` is the `User` fixture, so we have a user to log in 
- `client` arg is the test client, so we can force the user to log in 
- The path `"user.png"` is a dummy path -- in reality, I have a test file in my filesystem and I use the full path to that. 
- This view redirects on success, so I also added a check that the redirect was to the correct URL 
- Also added a check that the user's profile photo did actually update

