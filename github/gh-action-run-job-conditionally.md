# Running an action conditionally 

Basically, adding an `if` statement before the job is executed. 

```yaml
name: Process new issues

on:
  issues:
    types: [labeled, opened]

jobs:
  create-issue-comment:
    # Only run this job if the issue has the label "todo"
    if: ${{ github.event.label.name == 'todo' }}
    runs-on: ubuntu-latest
```

Add `if: ${{ github.event.label.name == 'todo' }}` (and replace the logic in the `{{}}`) right below the name of your job. If the condition isn't met, none of the steps in the job will execute. 

If you have multiple jobs in one workflow, the other jobs *will* execute unless you add this condition. 

It will be interesting to look into best practices for GitHub Action organization. If you have several different things you want to have happen when an issue is opened, depending on the tags, is one long workflow file `new-issues.yml` a decent idea, with conditional logic for each job depending on what needs to happen? Something to experiment with. 
