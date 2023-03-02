# Test that an exception is raised 

Docs: https://docs.pytest.org/en/7.1.x/how-to/assert.html

```python
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```
