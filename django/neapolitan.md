# Neapolitan: Everything I've Learned 

(Okay, maybe not everything, but I am going to collect the practical things I have learned about [Neapolitan](https://github.com/carltongibson/neapolitan) in this document. Huge thanks to Carlton Gibson for the library, and [Jeff Triplett](https://webology.dev/) for teaching me everything I know about it. Literally.) 

---

## Basics 

### What is Neapolitan? 

It's a Django library that gives you a set of basic CRUD views that you can use for your Django models. It's a good way to get started building all of the basic views you need when standing up a new Django model. 

### What is a Role? 

A Role is an action, the thing the user is doing in the view right now. Choices as of 08-2024 are: LIST, DETAIL, CREATE, UPDATE, and DELETE. In my brain, they correspond mostly to the actions you would think of in ViewSets. 

### Selecting which fields appear 

You can distinguish between detail views if you want to. 

```py
from neapolitan.views import CRUDView

class MyModelCRUDView(CRUDView):
    # Choose which fields to display for all views 
    fields = ["author_name", "title", "publication_year", "summary"]
```

### Setting custom fields for the list view 

```py
from neapolitan.views import CRUDView

class MyModelCRUDView(CRUDView):
    # Choose which fields to display in the list view
    list_fields = ["author_name", "title", "publication_year"] 

    def list(self, request, *args, **kwargs):
        self.fields = self.list_fields
        return super().list(request, *args, **kwargs)
```

### Setting things like the form, the filter, etc. 

These work the way you would expect -- you set the attribute on the class, like you would a regular class-based view. 

- `filterset_class`
- `form_class`
- `model`
- `paginate_by` (int)


---

## Other fun things 

### Change the queryset based on the Role 

```py
from neapolitan.views import CRUDView
from neapolitan.views import Role

class MyModelCRUDView(CRUDView):
    def get_queryset(self):
        qs = super().get_queryset()
        # Show a special subset on the list page 
        if self.role == Role.LIST:
            return qs.filter(status="in progress")
        return qs
```

### Use a custom template based on the Role 

```py
from neapolitan.views import CRUDView
from neapolitan.views import Role

class MyModelCRUDView(CRUDView):
    def get_template_names(self):
        template_names = super().get_template_names()

        if self.Role == Role.UPDATE:
            template_names = ["/path/to/custom_update_template.html"]

        return template_names
```
