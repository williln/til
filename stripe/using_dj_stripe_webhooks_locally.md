# Receiving Stripe webhooks via `dj-stripe` in local dev 

## Use case 

I am implementing `dj-stripe` in my project so that my data stays in sync without me having to think too much about it. I need the webhooks to run locally. 

## Links 

- [Local Webhook Testing](https://dj-stripe.dev/2.8/usage/local_webhook_testing/)
- [Using Stripe Webhooks](https://dj-stripe.dev/2.8/usage/webhooks/)
- [dj-stripe contains models for all the Stripe objects and can sync them for you](https://github.com/williln/til/blob/main/stripe/setup-dj-stripe.md)
- [Setting up a webhook in local development (Django project)](https://github.com/williln/til/blob/main/stripe/webhook_local_dev.md)

## What I did 

> 🗒️ This finally worked after some trial and error so the directions might not be 100% exactly correct, but I think it's mostly right

Note: This assumes you have a Stripe account, have set up Stripe in your project, and have installed `dj-stripe` and imported your Stripe data. See [dj-stripe contains models for all the Stripe objects and can sync them for you](https://github.com/williln/til/blob/main/stripe/setup-dj-stripe.md). 

You also **already need to have deployed your site**. The dj-stripe admin won't accept localhost as a webhook base URL. But you will use the Stripe CLI to forward the webhooks to your local server. 

> ⚠️ This **creates a real webhook** so **use your test API key**

1. Go to Webhook Endpoints in the Django admin: `http://localhost:8000/admin/djstripe/webhookendpoint/`
2. Create a new endpoint
3. Fill out the form: 

<img width="724" alt="Screenshot 2024-07-19 at 11 23 20 AM" src="https://github.com/user-attachments/assets/4ec9459f-5a4d-4f45-b545-c8e5774874b2">

- **Stripe account**: Tied to the API key your provided when you set up dj-stripe. dj-stripe does support multiple Stripe accounts, but I haven't used that feature so I only had one to choose from.
- **Live mode**: I left unchecked because I am testing
- **Base url:** They only need the base, like `https://example.com`, but although it prepopulates with `localhost`, it will error if you don't change it.
- **API version**: See the [dj-stripe docs on versions](https://dj-stripe.dev/2.8/api_versions/). This one is referring to your Stripe API version. I found this on a Developers page: https://dashboard.stripe.com/test/developers. I filled the API version with the default version as `2023-10-16` and that worked fine
- **Enabled events**: Highlight the events you want to listen to
- **Tolerance**: I didn't change this from the default, 300

<img width="936" alt="Screenshot 2024-07-19 at 11 26 43 AM" src="https://github.com/user-attachments/assets/5d584554-28c3-48aa-b8fa-f821c6264f70">

4. After you save your webhook, go to your Stripe test webhooks dashboard and confirm that you can see it. It will have a UUID as part of the URL and look something like: `http://example.com/stripe/webhook/68f60f4c-4e97-4029-8457-99de29fc58fc/`
5. Back in your terminal, start your Django server. In a new terminal window, run the command to forward the Stripe webhooks to the local endpoint you just added: `stripe listen --forward-to http://localhost:8000/stripe/webhook/68f60f4c-4e97-4029-8457-99de29fc58fc/`
6. This part is a little hacky: You will see a webhook secret output, and you need to pass that secret. So you will wind up running `stripe listen` twice: Once to obtain the secret, and then once to pass the secret along with the request.

```
stripe listen --forward-to http://localhost:8000/stripe/webhook/68f60f4c-4e97-4029-8457-99de29fc58fc/
> Ready! You are using Stripe API Version [2023-10-16]. Your webhook signing secret is whsec_redacted (^C to quit)
stripe listen --forward-to http://localhost:8000/stripe/webhook/68f60f4c-4e97-4029-8457-99de29fc58fc/ -H "x-djstripe-webhook-secret:whsec_redacted"
> Ready! You are using Stripe API Version [2023-10-16]. Your webhook signing secret is whsec_redacted (^C to quit)
```

The secret is `whsec_redacted`, so you obtain it the first time, then pass it the second time. There is probably a better way to do this, but this worked for me. 

7. Now that you are listening to webhooks locally, trigger one. In a new window, I ran `stripe trigger customer.created`, and I could see output the terminal running the Stripe listener.

I hope all of this makes sense! 
