# Adding a custom context processor to your Django app so you can include bits of data in your template headers more easily 

## 1. Add `my_app/context_processors.py` 

```python
from __future__ import annotations


def my_context(request):
    """
    Adds a special notice for a sale 
    """
    return {"notice": "All cat toys 50% off!"} 

```


## 2. Add to settings 

In `settings.py`:

```python
TEMPLATES = [
    {
        ...
        "OPTIONS": {
            "context_processors": [
                ...
                "my_app.context_processors.my_context",
            ],
        },
    }
]
```

## 3. Use your context value in your template: 

```html
<h2>{{ notice }}</h2>
```
