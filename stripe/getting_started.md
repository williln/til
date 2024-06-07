# Getting started with Stripe 

## Use case 

- Using with [plata](https://github.com/matthiask/plata) in a Django project
- Need to use a flexible process as I need to be able to submit an order and run the card later, for business reasons

## Credentials 

1. Log into Stripe and make sure you're in test mode
2. Find the test credentials:

<img width="334" alt="Screenshot 2024-06-06 at 5 02 35 PM" src="https://github.com/williln/til/assets/2286304/dd58965e-2ef7-47f3-b081-e83ce06d141d">

4. Add to `settings.py` and wherever you securely store env variables or secrets

```python
# settings.py
STRIPE = {
    "PUBLIC_KEY": env.str("STRIPE_PUBLIC_KEY", ""),
    "SECRET_KEY": env.str("STRIPE_SECRET_KEY", ""),
}
```

## Create a PaymentIntent 

> Building an integration with the Payment Intents API involves two actions: creating and confirming a PaymentIntent. Each PaymentIntent typically correlates with a single shopping cart or customer session in your application. The PaymentIntent encapsulates details about the transaction, such as the supported payment methods, the amount to collect, and the desired currency.
> - [The Payment Intents API](https://docs.stripe.com/payments/payment-intents)

```python
import stripe
from django.conf import settings

amount = 600 # in cents
currency = "USD"

stripe.api_key = settings.STRIPE["SECRET_KEY"]
payment_intent = stripe.PaymentIntent.create(
    amount=int(amount * 100),
    currency=currency.lower(),
    capture_method="manual",
    metadata={"order_id": 1, "user_email": "lacey@example.com"},
    payment_method_types=["card"],
)
```

You can't pass `confirm=True` unless you also pass a `payment_method`. 

Once I submitted that API request, I could see my payment intent in my Stripe dashboard: 

<img width="685" alt="Screenshot 2024-06-06 at 5 06 19 PM" src="https://github.com/williln/til/assets/2286304/a1608761-8b2b-4dde-b8bb-7290fd6d6956">

