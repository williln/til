# Using off-session payments and `setup_future_usage`

## Links 

- [Optimizing payment methods for future payments](https://docs.stripe.com/payments/payment-intents#future-usage) - Stripe docs
- [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage)

## Use case 

I need to be able to charge a customer's card with saved information (example: I need to adjust their shipping information, or change the quantity of an item). In Stripe, this is called an **off-session payment** (maybe it's called this everywhere -- I don't do a lot of ecommerce). 

<img width="866" alt="Screenshot 2024-06-06 at 6 11 16 PM" src="https://github.com/williln/til/assets/2286304/8a786f25-98d5-457c-8874-a5c777a316b1">

## Note 

Stripe's docs don't sound fond of these payments: 

> You can still accept off-session payments with a card set up for on-session payments, _but the bank is more likely to reject the off-session payment and require authentication from the cardholder_.

and

> Setups for off-session payments are more likely to incur additional friction. Use on-session setup if you don’t intend to accept off-session payments with the saved card.

## `setup_future_usage`

From the docs: 

> Indicates that you intend to make future payments with this PaymentIntent’s payment method.

> Providing this parameter will attach the payment method to the PaymentIntent’s Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be attached to a Customer after the transaction completes.

> When processing card payments, Stripe also uses setup_future_usage to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.

Example code: 

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = settings.API_KEY

stripe.PaymentIntent.create(
  amount=1099,
  currency="usd",
  setup_future_usage="off_session",
)
```

