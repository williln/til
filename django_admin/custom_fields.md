# Adding a custom field to the Django admin list display

You can add whatever fields you want to the Django admin's list display, create a special method with the same name as your field.  

To show the `Fandom` objects associated with a specific `Fic`: 

1. Create a method in the `FicAdmin` class called `show_fandoms.` (I can't just use `fandoms` -- that will technically work but shows me None) 
2. Have it take `self` and the instance as `obj` as arguments 
3. Use the `obj` instance to get the data (or whatever processing you need to do) 
4. Return the data 
5. Add the field to the `list_display` attribute, and use the same name as the method. 

```python
from django.contrib import admin
from fics.models import Author, Character, CustomTag, Fandom, Fic, Ship


class FicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "show_fandoms",
        "show_ships",
        "show_authors",
        "word_count",
        "complete",
    )

    def show_fandoms(self, obj):
        if obj.fandoms.exists():
            return ", ".join([fandom.name for fandom in obj.fandoms.all()])
        return ""

    def show_ships(self, obj):
        if obj.ships.exists():
            return ", ".join([ship.name for ship in obj.ships.all()])
        return ""

    def show_authors(self, obj):
        if obj.authors.exists():
            return ", ".join([author.username for author in obj.authors.all()])
        return ""

```

Result: 

<img width="1527" alt="Screen Shot 2022-11-17 at 10 04 58 AM" src="https://user-images.githubusercontent.com/2286304/202523839-eb75b8df-b705-4f0b-b933-e81c11eeef22.png">
