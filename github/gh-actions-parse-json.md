# Parsing JSON output from a GitHub Issue template in a GitHub Action 

## Steps: 

- Set up an issue template 
- Set up an action to look at new issues that get created for that template (I do this by looking for a specific label) 
- Parse the issue body into JSON 
- Use the built-in `fromJSON` method to get specific fields from the JSON 

### Set up an issue template 

This method uses [`peter-murray/issue-forms-body-parser@v2.0.0`](https://github.com/peter-murray/issue-forms-body-parser), which requires thetemplate for the issue to be set up in a specific way. 

The action supports more complex key/value pairs than just `{"key": "val"}` (like lists, etc) but I have only tried it with URLs. 

This is the issue template I use: 

```md
# .github/ISSUE_TEMPLATE/new-issue.md
---
name: Add to TBR
about: 'Add a new link to TBR '
title: 'Add [TITLE] to TBR '
labels: tbr
assignees: ''

---

### >>link<<

[LINK]
```

When someone creates an issue with this template, the issue will: 

- auto-fill the title as `Add [TITLE] to TBR`
- auto-fill the body with a header `### >>link<<` and a body `[LINK]`. 

The user replaces `[LINK]` with a URL, and `[TITLE]` in the title of the issue with whatever they want. The user **should not change the heading**. The `>>link<<` part is important -- that's how the action we're using will know how to parse the issue into JSON. 

### Set up an action to look at new issues that get created for that template

This action looks for issues that have been newly opened, or have been newly-labeled.  

```yaml
# .github/workflows/new_issue.yml
name: Process issues

on:
  issues:
    types: [labeled, opened]

jobs:
  create-issue-comment:
    runs-on: ubuntu-latest
    outputs:
      issue_json: ${{ steps.set-json.outputs.issue_json }}
```

### Parse the issue body into JSON 

Create a step called `parse` to parse the issue body using [`peter-murray/issue-forms-body-parser@v2.0.0`](https://github.com/peter-murray/issue-forms-body-parser). 

This example shows why the formatting of the issue template was so important. `label_marker_start` contains the characters that mark out a new **value**, and `label_marker_end` marks the end of that key. Whatever comes after that is the value.

So this issue template: 

```markdown
## >>link<<
https://example.com
```

Will create this JSON: 

```javascript
{
  "link": "https://example.com"
}
```

And this yaml add the `parse` step, then echo the result to the console when the action runs. 

```yaml
jobs:
  create-issue-comment:
    ... 
    steps:
      # Parse the JSON from the issue body
      - name: Parse issue
        id: parse
        uses: peter-murray/issue-forms-body-parser@v2.0.0
        with:
          issue_id: ${{ github.event.issue.number }}
          # These arguments correspond to the formatting in the issue template
          separator: '###'
          label_marker_start: '>>'
          label_marker_end: '<<'

      # Show the parsed JSON
      - name: Show parsed data JSON
        run: |
          echo "${{ steps.parse.outputs.payload }}"
```

### Use the built-in `fromJSON` method to get specific fields from the JSON 

You can introspect the JSON output and access specific fields using the [built-in `fromJSON` method](https://docs.github.com/en/actions/learn-github-actions/expressions#fromjson). 

The `set-json` step sets the JSON payload from the `parse` step as an output using `$GITHUB_OUTPUT`. 

Then the `see-link` step uses `env` to run `fromJSON` on the JSON output from the issue, then runs `echo "${link}"` to print the link to the console. 

I'm going to be totally honest that I don't 100% understand how this works but I know that it does. 

```yaml
jobs:
  create-issue-comment:
    ... 
    steps:
      ... 
      # Save the parsed JSON as output
      - name: Set JSON output 
        id: set-json
        run: echo "issue_json=${{ steps.parse.outputs.payload }}" >> $GITHUB_OUTPUT

      # See the link
      - name: From JSON
        id: see-link
        env: ${{ fromJSON(steps.parse.outputs.payload) }}
        run: echo "${link}"
```
