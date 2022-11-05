# Making a collapsible markdown section

From this [gist by pierrejoubert73](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab): 

- Have an empty line after the `</summary>` tag or markdown/code blocks will not render.
- Have an empty line after each `</details>` tag if you have multiple collapsible sections.

```markdown
<details>
  <summary>Click me</summary>
  
  ### Favorite Disney Movies
  1. Wall-E
  2. Moana 
</details>
```

## Live example: 

<details>
  <summary>Click me</summary>
  
  ### Favorite Disney Movies
  1. Wall-E
  2. Moana 
</details>
