# Adding extra fields to the list view in the Django Admin 

I didn't actually learn this today, but I remembered it this week and am writing it down. To add extra fields to the List display in the Django admin, add the `list_display` attribute to your `ModelAdmin` class. 

```python
from django.contrib import admin
 from fics.models import Author, Character


 class CharacterAdmin(admin.ModelAdmin):
     list_display = ("name", "fandom")


 admin.site.register(Character, CharacterAdmin)


```

Result: You can now see the `fandom` element in the list display for the `Character` model in the admin! 

<img width="1647" alt="Screen Shot 2022-11-16 at 8 55 15 AM" src="https://user-images.githubusercontent.com/2286304/202245659-2c6eeef1-c53b-4348-b160-124802f66da3.png">
