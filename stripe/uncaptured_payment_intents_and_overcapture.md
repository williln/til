# Creating a PaymentIntent, but not capturing it, and allowing more to be charged later  

Example use case: You need to calculate shipping manually and adjust it higher than the customer's original amount. 

## Links 

- [Create and confirm an uncaptured PaymentIntent](https://docs.stripe.com/payments/overcapture#confirm-payment-intent)

NOTE: The text below is lifted from the stripe docs basically verbatim! 

You can only perform overcapture on uncaptured payments after PaymentIntent confirmation. To indicate you want to separate the authorization and capture, specify the capture_method as manual when creating the PaymentIntent. To learn more about separate authorization and capture, see how to place a hold on a payment method.

You must specify the PaymentIntents you plan to overcapture by using if_available with the request_overcapture parameter.

```python
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_51P18loRwAvfn4Tp9SA2ClBzSQgt7pxd6r9gaLg3L1kpBZIpNWGVElDuqDCUB7MEkcApA1U4Wk2DZYHVXamlCDyHh00DlRYG5wO"

stripe.PaymentIntent.create(
  amount=1000,
  currency="usd",
  payment_method_types=["card"],
  payment_method="pm_card_visa",
  confirm=True,
  capture_method="manual",
  expand=["latest_charge"],
  payment_method_options={"card": {"request_overcapture": "if_available"}},
)
```

Look at the overcapture.status field on the latest_charge in the PaymentIntent confirmation response to determine if overcapture is available for the payment based on availability. If available, the maximum_amount_capturable field indicates the maximum amount capturable for the PaymentIntent. If unavailable, the maximum_amount_capturable is the amount authorized.

```javascript
// PaymentIntent response
{
  "id": "pi_xxx",
  "object": "payment_intent",
  "amount": 1000,
  "amount_capturable": 1000,
  "amount_received": 0,
  "status": "requires_capture",
  ...
  // if latest_charge is expanded
  "latest_charge": {
      "id": "ch_xxx",
      "object": "charge",
      "payment_method_details": {
        "card": {
          "amount_authorized": 1000
          "overcapture": {
              "status": "available", // or "unavailable"
              "maximum_amount_capturable": 1200
          }
        }
      }
      ...
    }
  ...
}
```

## See also 

- [How to increment a prior authorization([Increment an authorization | Stripe Documentation](https://docs.stripe.com/payments/incremental-authorization)) to increase the authorized amount over the maximum you already authorized
