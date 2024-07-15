# Running Sphinx docs locally 

Note: This is without Docker, without anything fancy, just cobbling something together. 

## Links 

- [Sphinx Quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html)

## Assumptions 

- You have a `requirements.txt` in your `docs/` directory (separating your docs requirements from your app or project requirements)
- You are using Sphinx and sphinx-autobuild

## Steps 

```
# requirements.in
sphinx
sphinx-autobuild
```

1. Install your requirements 
2. Run `sphinx-build -b html docs docs/_build/html` to build your docs into html. The `docs` points to the directory I want Sphinx to build from, in this case the `docs/` directory. `_build/html` is the name of the directory that I want the HTML files that are generated to be put into.
3. Run the server at `sphinx-autobuild docs docs/_build/html --host "localhost"`
4. Go to `localhost:8000` to see your project docs. 
