# Using `pip-tools` and `pip-compile` for Python dependency management 

## Links 

- [`pip-tools`](https://github.com/jazzband/pip-tools/)
- [`pip-compile`](https://github.com/jazzband/pip-tools/?tab=readme-ov-file#example-usage-for-pip-compile)

## Use case 

I want to keep my requirements up to date and I don't want to worry about it.  

## Instructions 

Note: Even in a Docker setup, I still use pip tools in a virtual env outside of Docker. It's generally always been faster. 

1. Install`pip-tools` with `pip install pip-tools`
2. Put your requirements in a `requirements.in` file:

```
boto3
django
django-extensions
```

3. Run `pip-compile requirements.in --output-file requirements.txt`
4. You will see the "pinned" version of the requirements in a `requirements.txt` file.
5. Rebuild your Docker container or reinstall your requirements however you do that.

The output in `requirements.txt` will be something like: 

```
# This file is autogenerated by pip-compile with Python 3.10
# by the following command:
#
#    pip-compile requirements.in
#
asgiref==3.6.0
    # via django
django==4.1.7
    # via -r requirements.in
sqlparse==0.4.3
    # via django
```

You can see the source of every installed package, not just the ones you defined in your `requirements.in`. 

