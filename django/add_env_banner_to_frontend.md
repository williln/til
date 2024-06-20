# Using `django-admin-env-notice` to add an envioronment notice to the frontend 

## Links 

- [django-admin-env-notice](https://github.com/dizballanze/django-admin-env-notice/)

## Use case 

I have a dev site and I want a notice about the fact that it's a dev site to appear on every page, not just in the admin, but I don't want to write extra code for it. 

## What I did 

- I installed `django-admin-env-notice` as directed, and confirmed I could see it in my local admin
- Then, I headed to the repo and found the [base template](https://github.com/dizballanze/django-admin-env-notice/blob/master/django_admin_env_notice/templates/admin/base_site.html):

```python
{% extends "admin/base_site.html" %}
{% block extrastyle %}{{ block.super }}
{% if ENVIRONMENT_NAME and ENVIRONMENT_COLOR and show_notice %}
<!-- Environment notice -->
<style type="text/css"{% if request.csp_nonce %} nonce="{{ request.csp_nonce }}"{% endif %}>
    {{ ENVIRONMENT_ADMIN_SELECTOR }}:before {
        display: block;
        line-height: 35px;
        text-align: center;
        font-weight: bold;
        text-transform: uppercase;
        color: {{ ENVIRONMENT_TEXT_COLOR }};
        content: "{{ ENVIRONMENT_NAME }}";
        background-color: {{ ENVIRONMENT_COLOR }};
        {% if ENVIRONMENT_FLOAT %}
            position: sticky;
            top: 0;
            z-index: 1000;
        {% endif %}
    }
</style>
{% endif %}
{% endblock %}
```

- Right out of the gate, I reproduced the entire `{% if %}` condition directly in my base template, above my header. It worked great!

I tested it logged in and logged out and it works equally well. I figured out from looking at the context processor that this is because there is a setting for showing the banner to unauthenticated users, and it defaults to True: 

```python
def show_notice(request):
    return request.user.is_authenticated or getattr(settings, 'ENVIRONMENT_SHOW_TO_UNAUTHENTICATED', True)


def from_settings(request):
    return {
        'ENVIRONMENT_NAME': getattr(settings, 'ENVIRONMENT_NAME', None),
        'ENVIRONMENT_COLOR': getattr(settings, 'ENVIRONMENT_COLOR', None),
        'ENVIRONMENT_TEXT_COLOR': getattr(settings, 'ENVIRONMENT_TEXT_COLOR', "white"),
        'ENVIRONMENT_ADMIN_SELECTOR': getattr(
            settings, 'ENVIRONMENT_ADMIN_SELECTOR', 'body'),
        'ENVIRONMENT_FLOAT': getattr(settings, 'ENVIRONMENT_FLOAT', False),
        'show_notice': show_notice(request),

    }
```
## What about Prod? 

I don't want this banner to appear on the frontend in Prod, so I have some options: 

1. Add an item to my production checklist to remove the banner.
2. Add a new setting and a context processor (similar to the one that `django-admin-env-notice` uses: https://github.com/dizballanze/django-admin-env-notice/blob/master/django_admin_env_notice/context_processors.py) so I can use that setting to control whether I see the banner in the base template
3. Set the `django-admin-env-notice` values to null in production
4. Override their context processor to change the `show_notice()` logic 

I love how easy it was to use this library in a way it wasn't intended! 
