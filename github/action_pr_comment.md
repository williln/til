# Github Action that leaves a comment on new PRs or issues 

```yml
name: Comment on PRs

on:
  pull_request:
    branches:
      - main
      # any other branches, like dev/develop

jobs:
  comment:
    runs-on: ubuntu-latest
    steps:
      - name: Comment on PR
        uses: actions/github-script@v5
        with:
          github-token: ${{secrets.GITHUB_TOKEN}}
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '👋 Hi there!'
            })
```
