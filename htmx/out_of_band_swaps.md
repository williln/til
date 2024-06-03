# Updating other elements on the page with `hx-swap-oob` 

## Links 

- [Out of Band Swaps (`hx-swap-oob`) in htmx docs](https://htmx.org/docs/#oob_swaps)

## Use case 

I used htmx to make an API call and remove an item from a form and have that row of the form be removed smoothly. Then, I needed other elements on the page to update (such as the total number of items). 

## Example 

 Say I am removing a book from my "Holds" list at the library. I want the total number of books I have on hold to update on that screen. 

 In my view:

 ```python
# views.py
from django.http import HttpResponse
from django.template.loader import render_to_string


def remove_hold(request, hold_id):
    # rest of the code to remove the hold 
    
    template = "hold_summary.html"
    html = render_to_string(template, {
        "div_id": "total-holds", # What div HTMX will look for 
        "total_holds": total, # Updated value inside that div
        "extra": "hx-swap-oob='true'" #The 'out of band swap' action 
    })
    return HttpResponse(html, content_type="text/html"

 ```

 The template I used is "included" in the main `hold.html` template: 

```html
# templates/holds.html 
{% extends "base.html" %}
# load HTMX 

{% for hold in holds %}
    <p>{{ hold.title }}</p>
{% endfor %} 

{% include "hold_summary.html %}
```

Then, in `hold_summary.html`, I specify the div id and other fields: 

```html
<div id="total-holds" {{ extra }}>{{ total_holds }}</div>
```

That `{{ extra }}` holds all the htmx I need to render. 

--- 

## Thoughts 

- This was really cool and easy to implement once I understood it 
- I have no idea if how I have structured things is a good practice  
- The way that htmx works with Django templates is starting to make more sense to me 
- I still feel like something isn't quite clicking but it's almost there.  
- I am still in the "throwing spaghetti at the wall to see what sticks" phase, but I feel closer to being able to make an actual simple pasta dish (if I may extend the pasta metaphor a little...) 
