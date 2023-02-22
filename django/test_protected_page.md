# How to log in a test user in a `pytest` unit test 

- Django 3.2 
- Python 3.10 
- `pytest`, `django-test-plus`, and `pytest-django` 
- [Example from the pytest-django docs](https://pytest-django.readthedocs.io/en/latest/helpers.html#client-django-test-client)

```python
def test_profile_photo_update_success(tp, user, client):
    """
    POST /users/me/photo

    Confirm that user can update their profile photo 
    """
    client.force_login(user)
    res = tp.get("protected-page")
    tp.response_200(res)
```

- `client` argument is the test client 
- use the `force_login` method on `client` with the `user` fixture 
- follow up with testing that your user can now access whatever protected page you're testing 

## Example from the `pytest-django` docs 

```python
def test_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    client.force_login(user)
    # Or this:
    client.login(username=username, password=password)
    response = client.get('/private')
    assert response.content == 'Protected Area'
```
