# Testing Django signals, and disabling signals in tests (Django 2.2)

Say I have a post-save signal that does some processing once a model has been saved.

```python
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MyModel


@receiver(post_save, sender=MyModel)
def post_save_my_model(sender, instance, created, *args, **kwargs):
    if created:
        # Do some processing
        pass
    else:
        # Do some other processing
        pass

```

I want to test that my signal has been called. I couldn't find a ton of information in StackOverflow about this, at least not that made sense to me. So I went to Django's source code to see how Django tests its own signals. I then adapted that for my own use.

```python
# test_signals.py
from django.db.models import signals
from django.test import TestCase

from my_app import factories, models


class TestMySignal(TestCase):

    def test_post_save_signal(self):
        """
        Cribbed from how Django tests their signals
        https://github.com/django/django/blob/stable/2.2.x/tests/signals/tests.py#L50
        """
        data = []

        def post_save_handler(signal, sender, instance, **kwargs):
            data.append(
                (instance, sender, kwargs.get("created"), kwargs.get("raw", False))
            )

        signals.post_save.connect(post_save_handler, weak=False)

        try:
            instance = factories.MyModelFactory()
            self.assertEqual(
                data, [(instance, models.MyModel, True, False)]
            )
        finally:
            signals.post_save.disconnect(post_save_handler)

```

I set up a `data` list, which I use to record some data when my signal is called.

Then, I create a function `post_save_handler` that appends a tuple of information to that `data` list. The tuple adds some information to the list that I can check once my signal has run.

I then connect the `post_save` signal to the `post_save_handler` I wrote, so all `post_save` signals (not just the one I am testing) will execute the code in the `post_save_handler`.

Now I can test my signal for real. In a `try` block, I create a new instance of my model, and then check that `data` contains what I expect it to.

At this point, I can refresh my instance from the database and check any side effects from the signal. If the signal changes the value in a database field, for example, I can check that that happened.

## Disabling signals in tests with Factory Boy

If you're using Factory Boy, the [`mute_signals`](https://factoryboy.readthedocs.io/en/latest/orms.html#factory.django.mute_signals) decorator will come in handy.

## Further Reading

- [Django 2.2 Source Code](https://github.com/django/django/blob/stable/2.2.x/tests/signals/tests.py#L50)
