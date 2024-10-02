## [`plata`](https://github.com/matthiask/plata/) order processors 

[`plata`](https://github.com/matthiask/plata/)  is a shopping cart experience built in Django, and I've been using it for the last 6 months but somehow not written a single TIL about it. It's [really well documented](https://plata-django-shop.readthedocs.io/en/latest/)! 

## Order processors 

[Order Processors in the docs](https://plata-django-shop.readthedocs.io/en/latest/api/shop.html?highlight=processors#order-processors) 

Plata has a setting [`PLATA_ORDER_PROCESSORS`](https://plata-django-shop.readthedocs.io/en/latest/settings.html): 

> The list of order processors which are used to calculate line totals, taxes, shipping cost and order totals.

> The classes can be added directly or as a dotted python path. All classes should extend `ProcessorBase`.

In [`Order.recalculate_total()`](https://github.com/matthiask/plata/blob/86ad0da0d94086588a48c9b881d6c3922c3b34c0/plata/shop/models.py#L237-L255), we cycle through all of the processes in this setting and run the `process()` method on the order. But what's a process? 

We can take a look at [Plata's default settings](https://github.com/matthiask/plata/blob/4a67e47035ec674503e72dbfda66b8191108f8ee/plata/default_settings.py#L18-L27): 

```py
PLATA_ORDER_PROCESSORS = getattr(
    settings,
    "PLATA_ORDER_PROCESSORS",
    [
        "plata.shop.processors.InitializeOrderProcessor",
        "plata.shop.processors.DiscountProcessor",
        "plata.shop.processors.TaxProcessor",
        "plata.shop.processors.MeansOfPaymentDiscountProcessor",
        "plata.shop.processors.ItemSummationProcessor",
        "plata.shop.processors.ZeroShippingProcessor",
        "plata.shop.processors.OrderSummationProcessor",
    ],
)
```

They contain all of the code that decides what the final total is. You can include or exclude the ones based on your needs. In my case, one of those was indeed the source of my bug... which I learned today was actually a feature: `ZeroShippingProcessor`. It's well-named, and it was the reason I couldn't save the shipping to the order. I was removing the shipping, literally setting it to zero.

Everything became clearer after that. As much as I love free shipping, I removed that class, and implemented a variation of the [`FixedAmountShippingProcessor`](https://github.com/matthiask/plata/blob/master/plata/shop/processors.py#L194).
