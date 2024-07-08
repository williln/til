# Including your project's README on your MkDocs index page 

## Links 

- [mkdocs-include-markdown-plugin](https://pypi.org/project/mkdocs-include-markdown-plugin/)

## Instructions 

1. `pip install mkdocs-include-markdown-plugin`
2. Add to your `mkdocs.yml`:

```yaml
plugins:
  - include-markdown
```

3. Add to your `docs/index.md`:

```md
{% include-markdown "../README.md" %}
```

You can configure a lot about how this works, or only include snippets or sections, etc. Check out the examples in the link. 
