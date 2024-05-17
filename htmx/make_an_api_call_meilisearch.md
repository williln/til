# Making a simple API call to an endpoint with HTMX 

Disclaimer: I am a real beginner at HTMX but I am trying to learn. Might be some errors in here.  

## Use case 

As the user types in a search box, the contents of the search box are sent to an API that returns results. The results are rendered appropriately. 

```html
<!-- includes/sample.html -->
<script src="https://unpkg.com/htmx.org"></script>

<input
    id="searchInput"
    type="text"
    placeholder="Search"
    name="q"
    hx-get="/my/search/endpoint/"
    hx-target="#searchResults"
    hx-trigger="keyup changed delay:50ms"
    hx-params="q"
>

<div id="searchResults"></div>
```

### HTMX params 

- [hx-get Attribute](https://htmx.org/attributes/hx-get/): `hx-get` makes a GET request to the endpoint you pass in. In this case, the value is `/my/search/endpoint/`. "The hx-get attribute will cause an element to issue a GET to the specified URL and swap the HTML into the DOM using a swap strategy." 
- [hx-target Attribute](https://htmx.org/attributes/hx-target/): `hx-target` loads the results of the `hx-get` request into the element with the ID you provide. In this case, the results will be loaded into `#searchResults`, which is further down in the template. "The hx-target attribute allows you to target a different element for swapping than the one issuing the AJAX request." 
- [hx-trigger Attribute](https://htmx.org/attributes/hx-trigger/): `hx-trigger` specifies what behaviors trigger the `hx-get` request to be fired. In this case, it's `keyup` (when the user types), `changes` (when that typing changes), and `delay:50ms` fires the request on a 50ms delay to allow the user time to type a few characters before seeing results. "The hx-trigger attribute allows you to specify what triggers an AJAX request."
- [hx-params Attribute](https://htmx.org/attributes/hx-params/): "The hx-params attribute allows you to filter the parameters that will be submitted with an AJAX request." Lets you specify which parameters you will send with the request.

So the request above will: 

1. Wait 50ms once the user starts typing in the `<input>` box, then
2. Call the `/my/search/endpoint/` endpoint,
3. With the `q` param (containing the search term the user typed in),
4. And put the results into the `<div id="searchResults"></div>` at the bottom of the template.


## View 

Your endpoint needs to return HTML, not JSON: 

> Note that when you are using htmx, on the server side you typically respond with HTML, not JSON.
> *[</> htmx \~ Documentation](https://htmx.org/docs/#introduction)*

I am burning out on writing sample code, so I'll just say: 

- Return an HTML response
- Create a `search_results.html` template that your view renders your results to
- The contents of this template is what will get rendered in `<div id="searchResults"></div>`

This is an incomplete example but is is a thing I learned. 
