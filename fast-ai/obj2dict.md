# Converting a `fastcore.basics.AttrDict` into a regular dictionary. 

Problem: The [`ghapi`](https://ghapi.fast.ai/) package returns the JSON data from GitHub as a Fast AI object called [`fastcore.basics.AttrDict`](https://fastcore.fast.ai/basics.html#attrdict). What this `AttrDict` object buys you is the ability to access the data in a dictionary with dot notation (which was a feature I wasn't taking advantage of. I assumed JSON was being returned and was using regular dictionary syntax to access the fields I needed.) 

But this data format wasn't playing nicely with Django's [JSONField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield). It seemed like sometimes it would work and fine other times I would get an error. 

I tried various things, mostly involving importing the `json` package and running `json.dumps`, then `json.loads` onto the data I wanted to save in the JSONField, but nothing worked consistently enough. 

It finally occurred to me that this special data format I was unfamiliar with probably came with the gift of methods! 

Sadly, `dir(my_data_in_attr_dict_format)` didn't reveal anything. 

But then I found [`obj2dict`](https://fastcore.fast.ai/xtras.html#obj2dict)! Which does exactly what it sounds like -- converts an `AttrDict` object to a `dict` with no muss, no fuss. 

I did have to hunt a little to figure out where to import it from, as I wasn't familiar with the documentation format. The import is: 

```python
from fastcore.xtras import obj2dict
```
