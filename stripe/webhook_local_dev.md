# Setting up a webhook in local development (Django project)

## Links 

- [Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks)
- [Events API](https://docs.stripe.com/api/events)
- [Types of events](https://docs.stripe.com/api/events/types)
- [Webhook builder](https://docs.stripe.com/webhooks/quickstart)

## Background notes 

> :pencil: These are my highlights from the [Stripe webhooks docs](https://docs.stripe.com/webhooks). 

- To enable webhook events, you need to register webhook endpoints. 
- After you register them, Stripe can push real-time event data to your application’s webhook endpoint when events happen in your Stripe account.
- Receiving webhook events is particularly useful for listening to asynchronous events such as when ... a recurring payment succeeds.
- When an event occurs, Stripe generates a new [Event](https://docs.stripe.com/api/events) object
- A single API request might result in the creation of multiple events. For example, if you create a new subscription for a customer, you receive customer.subscription.created and payment_intent.succeeded events.
- You receive events for all of the event types your webhook endpoint is listening for in your configuration.
- Use the received event type to determine what processing your application needs to perform. The data.object corresponding to each event type varies.
- The api_version indicates the API version of the event and dictates the structure of the included data.object. Your endpoint receives events using the configured API version, which can differ from your account’s default API version or the API version of any requests related to the event. 
- When retrieving Event objects from the API, you can’t control the API version of the data.object structure. Instead, retrieve that object from the appropriate API endpoint and use the Stripe-Version header to [specify an API version](https://docs.stripe.com/api/versioning).
- When an event is generated as a result of an API request, that request shows up as the `request.id`. If you use an [`idempotency_key`](https://docs.stripe.com/api/idempotent_requests) when making the request, it’s included as the `request.idempotency_key`. Check this `request` hash when you investigate what causes an event.
- For `*.updated` events, the event payload includes `data.previous_attributes` that allow you to inspect what’s changed about the Stripe object. 

## When events get generated

| Source |	Trigger |
| --- | --- |
| Dashboard	| When you call an API by modifying your Stripe resources in the Stripe Dashboard.| 
| API	| When a user action in your app or website results in an API call.| 
| API	| When you manually trigger an event with the Stripe CLI.| 
| API	| When you call an API directly with the Stripe CLI.| 

## Getting Started 

1. Create a webhook endpoint handler to receive event data POST requests.
2. Test your webhook endpoint handler locally using the Stripe CLI.
3. Register your endpoint within Stripe using the Dashboard or the API.
4. Secure your webhook endpoint.

You can register and create one endpoint to handle several different event types at the same time, or set up individual endpoints for specific events.

## Event object 

```javascript
{
  "id": "evt_redacted123",
  "object": "event",
  "api_version": "2024-06-20",
  "created": 1680064028,
  "type": "customer.subscription.updated", // Here is the event type 
  "data": {
    "object": {
      "id": "sub_1Mqqb6Lt4dXK03v50OA219Ya",
      "object": "subscription",
    }
  }
  ...
}
```

--- 

Let's actually start developing. 

1. Create a file `my_app/webhooks.py`. This is the Stripe [example](https://docs.stripe.com/webhooks#example-endpoint), lightly edited: 

```py
import json
from django.http import HttpResponse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Using Django
@csrf_exempt
def stripe_webhook(request):
  payload = request.body
  event = None
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
  stripe.api_key = settings.STRIPE_API_KEY

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    print('Error parsing payload: {}'.format(str(e)))
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    print('Error verifying webhook signature: {}'.format(str(e)))
    return HttpResponse(status=400)

  # Handle the event
  if event.type == 'payment_intent.succeeded':
    payment_intent = event.data.object # contains a stripe.PaymentIntent
    print('PaymentIntent was successful!')
  elif event.type == 'payment_method.attached':
    payment_method = event.data.object # contains a stripe.PaymentMethod
    print('PaymentMethod was attached to a Customer!')
  # ... handle other event types
  else:
    print('Unhandled event type {}'.format(event.type))

  return HttpResponse(status=200)


```

2. Register the endpoint in your `urls.py`:

```py
from __future__ import annotations

from django.urls import include
from django.urls import path

from my_app.webhooks import stripe_webhook

urlpatterns = [
    # Webhook urls 
    path("webhook/stripe/", stripe_webhook, name="stripe-webhook"),  
]

```

3. To test the webhook, download the [Stripe CLI](https://docs.stripe.com/stripe-cli), run `stripe login`, and complete the prompts. 

4. Start your Django server however you do that. I use `docker compose up` and run my server within Docker. 

5. Forward events to your webhook: run `stripe listen --forward-to localhost:8000/webhook/stripe/` (I do this in a new console window.)

```shell
$ stripe listen --forward-to localhost:8000/webhook/stripe/
> Ready! You are using Stripe API Version [2023-10-16]. Your webhook signing secret is whsec_redacted1234455677 (^C to quit)
```

On the second line is this statement: 

> `Your webhook signing secret is whsec_redacted1234455677`

This is your `STRIPE_WEBHOOK_SECRET`. Add this to your settings file or your env vars. When you are in local development, you always get this value from your `stripe listen` output. Otherwise, you get it from your Webhooks console in the Stripe UI when you register your webhook. 

6. In another new console window, run `stripe trigger {event}` and pass the event type you want to trigger, to test your webhook endpoint. 

## Result 

- I did all of the above 
- I ran `stripe trigger payment_intent.succeeded` 

```shell
$ stripe listen --forward-to localhost:8000/webhook/stripe/
> Ready! You are using Stripe API Version [2023-10-16]. Your webhook signing secret is whsec_redacted1234455677 (^C to quit)
2024-07-11 10:33:53   --> charge.succeeded [evt_redacted]
2024-07-11 10:33:53  <--  [200] POST http://localhost:8000/webhook/stripe/ [evt_redacted]
2024-07-11 10:33:53   --> payment_intent.succeeded [evt_redacted_2]
2024-07-11 10:33:53  <--  [200] POST http://localhost:8000/webhook/stripe/ [evt_redacted_2]
2024-07-11 10:33:53   --> payment_intent.created [evt_redacted_3]
2024-07-11 10:33:53  <--  [200] POST http://localhost:8000/webhook/stripe/ [evt_redacted_3]

```

Note that I received three events from initiating one call: 

- `charge.succeeded` 
- `payment_intent.succeeded` (The one I asked for)
- `payment_intent.created` (A side effect of `succeeded`, presumably)

You can also listen for only specific events: 

```
stripe listen --events payment_intent.created,customer.created,payment_intent.succeeded,checkout.session.completed,payment_intent.payment_failed
  --forward-to localhost:8000/webhook/stripe/
```

**Output from my Django server**:

```shell
web-1          | {"request": "POST /webhook/stripe/", "user_agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)", "event": "request_started", "level": "info"}
web-1          | Unhandled event type charge.succeeded
web-1          | {"code": 200, "request": "POST /webhook/stripe/", "event": "request_finished", "level": "info"}
web-1          | [11/Jul/2024 17:33:53] "POST /webhook/stripe/ HTTP/1.1" 200 0
web-1          | {"request": "POST /webhook/stripe/", "user_agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)", "event": "request_started", "level": "info"}
web-1          | Payment Intent succeeded: pi_redacted
web-1          | {"code": 200, "request": "POST /webhook/stripe/", "event": "request_finished", "level": "info"}
web-1          | [11/Jul/2024 17:33:53] "POST /webhook/stripe/ HTTP/1.1" 200 0
web-1          | {"request": "POST /webhook/stripe/", "user_agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)", "event": "request_started", "level": "info"}
web-1          | Unhandled event type payment_intent.created
web-1          | {"code": 200, "request": "POST /webhook/stripe/", "event": "request_finished", "level": "info"}
web-1          | [11/Jul/2024 17:33:53] "POST /webhook/stripe/ HTTP/1.1" 200 0
```

I can see the `Unhandled` message for the two events I didn't ask for, and the print message I expect from the one I did. 

## Bonus: Programmatically register your webhook 

```py
from django.conf import settings 
import stripe 

stripe.api_key = settings.STRIPE_API_KEY

endpoint = stripe.WebhookEndpoint.create(
  url='https://example.com/my/webhook/endpoint',
  enabled_events=[
    'payment_intent.payment_failed',
    'payment_intent.succeeded',
    # rest of the events you want to listen to 
  ],
)

```

