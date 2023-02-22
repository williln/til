# How to confirm that login is required in your Django view 

It's been a few years since I wrote a permissions test that wasn't for DRF, so I wanted to write this down! 

- Django 3.2 
- Python 3.10 
- Project uses `django-allauth`, `pytest`, and `django-test-plus`

```python
def test_view_auth(tp, db):
    """
    POST /users/me/photo/

    Canary test that this page is protected. 
    """
    res = tp.post("profile-photo")
    tp.response_302(res)
    assert "/accounts/login" in res.url
```

- `tp` is the `django_test_plus` fixture 
- The argument to `tp.post` "profile-photo" is the `name` of the URL I want to test

This project uses `django-allauth`, which redirects protected pages to the login screen. If you're using something else, you might not have a 302 code. The most important thing is that you get a code that indicates that the user can't access the page without logging in! 
