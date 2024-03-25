# How I set up `django-activity-stream`, including a simple test 

## Links 

- [`django-activity-stream` Documentation](https://django-activity-stream.readthedocs.io/en/latest/index.html)
- [`django-activity-stream` on GitHub]([https://django-activity-stream.readthedocs.io/en/latest/index.html](https://github.com/justquick/django-activity-stream))

## Notes 

My use case is an ecommerce site. I'll be using `django-activity-stream` to help me: 

- Help staff access their most-recently-accessed objects
- Help customers see their recently-viewed items

## Installation and Setup 

1. Install `django-activity-stream[jsonfield]` (I went ahead and included the `jsonfield` option as I'll be using it later)
2. Add `actstream` to `INSTALLED_APPS`
3. I already had a `SITE_ID`
4. I did not add the URLs because I don't currently want a publicly-available stream
5. Add the activity stream settings (note: these were a little different than the docs. I'm not sure if that is because I used `[jsonfield]`, or another reason. These settings are what worked for me with no errors.)

```python
# settings.py 
ACTSTREAM_SETTINGS = {
    "MANAGER": "actstream.managers.ActionManager",
    "FETCH_RELATIONS": True,
}
```

## Register models with `django-activity-stream` 

You have to register the models that you will want to track. 

In the app that contained the model(s) I wanted to track, I opened `apps.py`: 

```python
# my_app/apps.py
from __future__ import annotations
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_objects"

    def ready(self):
        # django-activity-stream stuff
        from actstream import registry
        # Add this line to register the model with django-activity-stream
        registry.register(self.get_model("MyModel"))
```

Now the model is registered with `django-activity-stream` 

## Use `django-activity-stream` to track model changes 

See [Generating Actions](https://django-activity-stream.readthedocs.io/en/latest/actions.html) in the docs for more info. 

I chose to set up a simple signal as a proof-of-concept. 

1. Create `my_app/signals.py`:

```python
# my_app/signals.py
from __future__ import annotations

from actstream import action
from django.db.models.signals import post_save

from my_app.models import MyModel


def mymodel_handler(sender, instance, created, **kwargs):
    if created:
        verb = "was added"
    else:
        verb = "was edited"
    action.send(instance, verb=verb)


post_save.connect(mymodel_handler, sender=MyModel)
```

2. Import the signals in the app config: 

```python
# my_app/apps.py
class MyAppConfig(AppConfig):
    def ready(self):
        # Add this line
        import my_app.signals # noqa

        from actstream import registry
        registry.register(self.get_model("MyModel"))
```


Now, any time a `MyModel` object is created or edited, a signal will fire. That signal will call `action.send()` to create a record of that action using `django-activity-stream`. 

## Test the signal 

Example `pytest`-style test: 

```python
from __future__ import annotations

from unittest.mock import patch

from actstream import action

from my_app.models import MyModel


def test_mymodel_handler(db):
    with patch.object(action, "send") as mock_send: 
        MyModel.objects.create(name="Test")
        mock_send.assert_called_once()
        _, kwargs = mock_send.call_args
        assert kwargs["verb"] == "was added"
```

There are probably other ways to test this as well. 
