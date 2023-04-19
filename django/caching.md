# Caching in Django Projects


## Adding Cache Logic

To add cache logic to your Django views or functions:

1. `from django.core.cache import caches`
2. Choose the appropriate cache (e.g., `cache = caches['my_cache']`; you might have multiple caches)
3. Get data from the cache using the `cache.get(key)` method.
4. If data is not found in the cache, fetch it.
5. Store the fetched data in the cache using the `cache.set(key, value, timeout)` method.

### Acccessing a cache

```python
from django.core.cache import caches

my_cache = caches["my_cache"]
# Perform cache operations using my_cache
```


## Testing Cache Logic

1. Set up your data.
2. Clear the cache before running your tests.
3. Test cache miss scenario: there is nothing in the cache. 
4. Test cache hit scenario: the object is found in the cache.
5. Test cache expiration scenario: the object was in the cache, but the cache is expired.

### Using `override_settings` in Tests for Caching

1. Import the `override_settings` decorator: `from django.test.utils import override_settings`
2. Use the `@override_settings` decorator before your test function to temporarily change the settings during the test.
3. Provide the cache settings you want to use during the test, such as `CACHES` with the appropriate cache backend and configuration.

Example:

```python
@override_settings(
    CACHES={
        "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    }
)
def test_cache_behavior():
    # Your test logic here
```

## Handling Multiple Caches in One Project

1. Define multiple caches in your `settings.py` file with appropriate cache backends and configurations.
2. Use the caches object from `django.core.cache` to access the specific cache you need.
3. Perform cache operations (e.g., get, set, delete) using the chosen cache.

### Example of defining multiple caches in the settings file

```python
CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    "special_cache": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "TIMEOUT": 86400,
    },
    # Add more caches if needed
}
```
