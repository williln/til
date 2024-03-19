# Adding ability to search in the Django Admin 

Add the `search_fields` attribute to your `ModelAdmin` class and list the fields you want to search by. 

This will let you search by `Character.name`: 

```python
from django.contrib import admin
 from fics.models import Author, Character


 class CharacterAdmin(admin.ModelAdmin):
     ...
     search_fields = ("name",)


 admin.site.register(Character, CharacterAdmin)
```

Result: 

<img width="1597" alt="Screen Shot 2022-11-16 at 8 55 23 AM" src="https://user-images.githubusercontent.com/2286304/202245699-cbdf3af9-d294-4f44-91b4-ca6344d529bd.png">

## Searching across a ManyToMany relationship 

The `Fandom` model has `ManyToManyField` connections to other models, `Fandom` and `Ship`. To enable a user to search for `Fic` objects in the admin by the name of the connected `Ship` or `Fandom`, use the field name you want to search on after the double underscore. 

Given these models: 

```python

class Fandom(TimeStampedModel):
    """
    A 'fandom' is the community around a specific thing.
    With respect to fics, 'Hary Potter' and 'Star Wars' are both fandoms.
    """

    name = models.CharField(max_length=255)


class Ship(TimeStampedModel):
    """
    A 'ship' is a relationship. 
    'Harry Potter/Ginny Weasley' is a ship. 
    """

    name = models.CharField(max_length=255)
    characters = models.ManyToManyField("fics.Character", related_name="ships")


class Fic(TimeStampedModel):
    ...
    fandoms = models.ManyToManyField("fics.Fandom", related_name="fics")
    ships = models.ManyToManyField("fics.Ship", related_name="fics")
    
```

If you want to search `Fic`s in the Admin based on the `Fandom` name or the `Ship` name, you add `fandoms__name` and `ships__name` to `search_fields`. 

```python
class FicAdmin(admin.ModelAdmin):
     ...
     search_fields = ("title", "summary", "fandoms__name", "ships__name")

         
  admin.site.register(Fic, FicAdmin)
```
