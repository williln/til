# Google SEO Notes for eCommerce

These are loose notes about what I am learning about boosting SEO for an e-commerce site. 

- [Google Search Central](https://developers.google.com/search) is where you can go to find info about how to help your site do better in Google rankings.
- You can add [structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) to your html templates to help Google learn more about your site.
- You can find the schemas for the structured data at [Schema.org](https://schema.org).
- JSON-LD is [JSON for Linking Data](https://json-ld.org) and is one form of structured data. It is also the one I will be using.
- You add "snippets" in specific formats that are specifed in the schemas, and this helps Google render your information in more helpful ways, and helps people find your site 

## `offers` 

- [The `Product` Snippet](https://developers.google.com/search/docs/appearance/structured-data/product-snippet)
- [`Offer` on Schema.org](https://schema.org/Offer)

Adding data from the [`Product` snippet](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) to your [structured data](https://schema.org) (in my case, [JSON for Linking Data](https://json-ld.org)) helps Google show that you have products for sale.  

In practice, this feels similar to setting up a `meta` tag

### Adding `ld+json` with pricing information to a Django template 

```html
<!-- /templates/product_list.html

{% block extra_head %}
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "ItemList",
      "name": "Products for Sale",
      "itemListElement": [
        {% for product in products %}
        {
          "@type": "ListItem",
          "position": {{ forloop.counter }},
          "item": {
            "@type": "Product",
            "name": "{{ product.name }},
            "url": "{{ request.scheme }}://{{ request.get_host }}{{ product.get_absolute_url }}",
            "offers": {
                "@type": "Offer",
                "price": "{{ product.default_price }}",
                "priceCurrency": "USD"
              }
          }
        }{% if not forloop.last %},{% endif %}
        {% endfor %}
      ]
    }
    </script>
{% endblock extra_head %}

```

This snippet does the following: 

- Add a `<script>` tag for the `ld+json` structured data about our products for sale to our product-list template
- Declares our schema in `@type`
- Loops through our products to set up each `item` attribute
- Creates an `offers` attribute for each product, where we can add pricing information

<hr> 

There are a lot of other options for adding product information to templates to improve their search performance. I'm going to look through the specification and do a little reading on how important the different attributes are.
