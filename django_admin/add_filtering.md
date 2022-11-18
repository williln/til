## Adding filtering functionality to the Django Admin 

To add the ability to filter to the Django admin, enable the `list_filter` attribute and use the field name as it is: 

```python
from django.contrib import admin
from fics.models import Author, Character, CustomTag, Fandom, Fic, Ship


class CharacterAdmin(admin.ModelAdmin):
    ...
    list_filter = ("fandom",)
```

Result: 

<img width="1328" alt="Screen Shot 2022-11-16 at 9 04 16 AM" src="https://user-images.githubusercontent.com/2286304/202245882-471596fd-04ca-46b7-a350-fb4a9d11036e.png">

