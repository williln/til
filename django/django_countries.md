# Using `django-countries` 

My use case is that my client ships to over 200 countries all over the world, so I need a lot of country data, so their customers can go shopping and receive their items wherever they need to. 

I found [`django-countries`](https://github.com/SmileyChris/django-countries/). It's got a lot of stars, it's been updated recently, and it does a lot of useful things, so I'm giving it a try. 

My `Profile` model: 

```python
from django_countries.fields import CountryField

class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile",
    )
    # Other address fields 
    country = CountryField(
        blank_label="(select country)", blank=True, null=True, help_text="Country"
    )
```

## Features 

### [`CountryField`](https://github.com/SmileyChris/django-countries/?tab=readme-ov-file#countryfield)

I like the [`CountryField`](https://github.com/SmileyChris/django-countries/?tab=readme-ov-file#countryfield) field because I can ((apparently) use the standard field attributes, and it will take care of providing the choices for me. 

### In forms 

You can use the same `CountryField` in your [forms](https://github.com/SmileyChris/django-countries/?tab=readme-ov-file#custom-forms) too:

```python
from django_countries.fields import CountryField

class CustomForm(forms.Form):
    country = CountryField().formfield()
```

### Customizing the list 

You can [customize the list of countries](https://github.com/SmileyChris/django-countries/?tab=readme-ov-file#customize-the-country-list) in various ways -- changing display names, including or excluding specific countries, etc. I anticipate using the features that will let me eliminate countries that my client does not ship to. 

```python
from django.utils.translation import gettext_lazy as _

# Change countries display 
COUNTRIES_OVERRIDE = {
    "NZ": _("Middle Earth"),
    "AU": None,
    "US": {
        "names": [
            _("United States of America"),
            _("America"),
        ],
    },
}

# Limit to specific countries only 
COUNTRIES_ONLY = ["NZ", "AU"]

# Limit to specific countries, and specify their display
COUNTRIES_ONLY = [
    "US",
    "GB",
    ("NZ", _("Middle Earth")),
    ("AU", _("Desert")),
]
```

There is also a setting to `SHOW_COUNTRIES_FIRST` where my client can specifiy the countries they ship to most frequently. 
