# Commenting on an issue from a GitHub Action 

Uses [`actions/github_script`](https://github.com/marketplace/actions/github-script)

Gets `issue_number` from the [GitHub context](https://docs.github.com/en/actions/learn-github-actions/contexts#github-context), same with the `owner` and `repo`. 

```yaml
name: Comment on a new issue 

on:
  issues:
    types: opened

jobs:
  create-issue-comment:
    runs-on: ubuntu-latest
    steps:
      - name: Comment on issue
        id: create_comment
        uses: actions/github-script@v6
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: "👋 Hi there!"
            })
```

Result when a new issue is created: 

![Screen Shot 2022-11-04 at 12 43 33 PM](https://user-images.githubusercontent.com/2286304/200061735-4c7c7184-d13f-4ae8-a657-6ac8b6da0c17.png)
