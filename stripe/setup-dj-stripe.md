---
tags: stripe, webhooks, django, dj-stripe
---
# `dj-stripe` contains models for all the Stripe objects and can sync them for you

- [dj-stripe](https://dj-stripe.dev/2.8/)
- [Installation](https://dj-stripe.dev/2.8/installation/)

## Use case 

I realized that Stripe's webhooks don't fire in order, and therefore I was at risk of overwriting valid data with outdated data if I processed them in the order that I received them. I asked Frank for advice and he suggested dj-stripe. 

We do have a requirement to use [plata](https://plata-django-shop.readthedocs.io/en/latest/) if possible, so part of this TIL is seeing if dj-stripe plays well with plata, but a quick glance didn't reveal any obvious red flags. 

## Initial setup 

- Add `dj-stripe` to `requirements.in` and use `pip-compile` to regenerate my requirements file. Rebuild container.
- Add `djstripe` to `INSTALLED_APPS`
- Add `path("stripe/", include("djstripe.urls", namespace="djstripe")),` to `urls.py`
- Add these to `settings.py`:

```py
STRIPE_LIVE_MODE = False  # Change to True in production
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
```

- Start my server. 
- Go into the Django Admin and add my **test** Stripe private API key:

<img width="642" alt="Screenshot 2024-07-18 at 10 13 21 AM" src="https://github.com/user-attachments/assets/b3490d47-4be8-4bc2-a329-db9ed8d4b87c">

Add my API key and save. 

<img width="612" alt="Screenshot 2024-07-18 at 10 14 00 AM" src="https://github.com/user-attachments/assets/5f6e8e16-1b43-46ec-aa70-98c03c53348d">

- In local dev, in my Docker `web` container, run `./manage.py djstripe_sync_models`. See my models populate!
