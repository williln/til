# Creating a new file and committing it using a GitHub Action 

When a new issue is opened in this repo, this workflow checks out the repo, then created a file called `new_link.txt`. The content of that file is set to a URL, then the new file is added and committed to `main`, then pushed. 

*Note*: Not suggesting that one should create new files when people open issues! Just documenting how to create a file from scratch in an action. 
```yaml
# .github/actions/commit-random-file.yml
name: Process new to-be-read issues

on:
  issues:
    types: opened

jobs:
  create-issue-comment:
    # Only run this job if the issue has the label "tbr"
    if: ${{ github.event.label.name == 'tbr' }}
    runs-on: ubuntu-latest
    steps:
      - name: Check out repo
        uses: actions/checkout@v3
      - name: Commit a random file
        run: |
          echo "https://example.com" > new_link.txt
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add .
          git commit -m "🙃 generated"
          git push
```

## Result 

![Screen Shot 2022-11-04 at 12 22 26 PM](https://user-images.githubusercontent.com/2286304/200058643-4af3a88a-43b5-4c53-89db-a14aa5b96972.png)
