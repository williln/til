# Generating a `PaymentIntent` and saving it to a Django model 

## Use case 

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

### Best practices around Payment Intents from the docs 

> - We recommend creating a PaymentIntent as soon as you know the amount, such as when the customer begins the checkout process, to help track your purchase funnel. If the amount changes, you can update its amount. For example, if your customer backs out of the checkout process and adds new items to their cart, you may need to update the amount when they start the checkout process again.

> - If the checkout process is interrupted and resumes later, attempt to reuse the same PaymentIntent instead of creating a new one. Each PaymentIntent has a unique ID that you can use to retrieve it if you need it again. In the data model of your application, you can store the ID of the PaymentIntent on the customer’s shopping cart or session to facilitate retrieval. The benefit of reusing the PaymentIntent is that the object state helps track any failed payment attempts for a given cart or session.

> - Remember to provide an idempotency key to prevent the creation of duplicate PaymentIntents for the same purchase. This key is typically based on the ID that you associate with the cart or customer session in your application.

### Payment Intents JSON object

<details>
    <summary>Payment Intents JSON response </summary>
    
```javascript
{
  "allowed_source_types": [
    "card"
  ],
  "amount": 600,
  "amount_capturable": 0,
  "amount_details": {
    "tip": {}
  },
  "amount_received": 0,
  "application": null,
  "application_fee_amount": null,
  "automatic_payment_methods": null,
  "canceled_at": null,
  "cancellation_reason": null,
  "capture_method": "manual",
  "charges": {
    "data": [],
    "has_more": false,
    "object": "list",
    "total_count": 0,
    "url": "/v1/charges?payment_intent=[redacted]"
  },
  "client_secret": "[redacted]",
  "confirmation_method": "automatic",
  "created": 1717717579,
  "currency": "usd",
  "customer": null,
  "description": null,
  "id": "[redacted]",
  "invoice": null,
  "last_payment_error": null,
  "latest_charge": null,
  "livemode": false,
  "metadata": {
    "order_id": "1",
    "user_email": "lacey@example.com"
  },
  "next_action": null,
  "next_source_action": null,
  "object": "payment_intent",
  "on_behalf_of": null,
  "payment_method": null,
  "payment_method_configuration_details": null,
  "payment_method_options": {
    "card": {
      "installments": null,
      "mandate_options": null,
      "network": null,
      "request_three_d_secure": "automatic"
    }
  },
  "payment_method_types": [
    "card"
  ],
  "processing": null,
  "receipt_email": null,
  "review": null,
  "setup_future_usage": null,
  "shipping": null,
  "source": null,
  "statement_descriptor": null,
  "statement_descriptor_suffix": null,
  "status": "requires_source",
  "transfer_data": null,
  "transfer_group": null
}
```

</details>

## Save the PaymentIntent information 

Based on the Stripe docs, I need to save the ID I get from the PaymentIntent to my Order model. I added this field to my custom Order model: 

```python
class Order(models.Model):
    payment_intent_id = models.CharField(
        _("Stripe payment intent ID"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("The Stripe payment intent ID for this order."),
    )
```

Now when I receive the response back from Stripe, I can save the ID to my Order object. 

## Idempotency keys 

[Stripe docs on Idempotent Requests](https://docs.stripe.com/api/idempotent_requests)

I need to generate a unique key for each request and pass it to the Stripe API. This way, if a checkout fails, I can retry that checkout and not create a duplicate. Here is a simple example: 

```python
def create_payment_intent_with_retry(amount, currency, retries=3, backoff_factor=2):
    attempt = 0
    idempotency_key = str(uuid.uuid4())  # Generate a unique idempotency key
    
    while attempt < retries:
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency=currency,
                capture_method="manual",
                payment_method_types=["card"],
                idempotency_key=idempotency_key
            )
            return payment_intent 
        except stripe.error.StripeError as e:
            attempt += 1
            if attempt < retries:
                time.sleep(backoff_factor ** attempt)  # Exponential backoff
            else:
                raise e
```

## Practical application

I plugged this into my shopping cart flow so that, at the point the user chooses to pay with Stripe, a PaymentIntent is created. 

```python
def process_order(...):
    # Rest of code 

    # Create a Stripe PaymentIntent and save the id to the Order 
    if not my_order.payment_intent_id:
        payment_intent = create_payment_intent(
            amount=self.amount,
            ... 
        )
        my_order.payment_intent_id = payment_intent["id"]
        my_order.save()
    
    return ...# Rest of Plata code 
```
