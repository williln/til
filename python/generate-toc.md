# Generate a markdown file with a table of contents in Python

Cribbed from Simon Willison: https://github.com/simonw/til/blob/0abdc32464f1bc726abebdbc147b945d22bae7a8/update_readme.py

- Python 3.10 
- Depends on having a database available that `sqlite_utils` can use 
- `til.db` should be replaced with the name of your db 
- Generates an actual table, not a list 
- For repos with a long readme (like someone who uses this workflow for blogging), this makes an easier-to-scan table of contents, but provides less data 

## Create a project-level README file 

 The body of it should be: 
 
 ```
 <!-- index starts -->
 <!-- index ends -->
 ```
 
 ## Create a `update_readme.py` file 

```python
# update_readme.py
import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

# Set up a regex to find your "index" comments in the README.md 
index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)

if __name__ == "__main__":
    Open your SQLite db and go through the rows 
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)
        
    index = ["<!-- index starts -->"]

    # Alphabetize the topics so your README is in alphabetical order 
    topics = list(by_topic.keys())
    topics.sort()

    for topic in topics:
        # Set up the heading
        index.append("### {}\n".format(topic))

        # Set up the table
        index.append("| Title | Status | Last Updated |")
        index.append("| ----- | ------ | ------------ |")

        # Go through the items
        rows = by_topic[topic]
        # Depends on these fields being in your db: 
        # - title, url, status, created
        for row in rows:
            index.append(
                "| [{title}]({url}) | {status} | {date} |".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")
       
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")

    # Opens the README and replaces the "index" with what was generated above
    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        readme.open("w").write(index_re.sub(index_txt, readme_contents))
    # Prints the output to the console for local testing 
    else:
        print("\n".join(index))

```

## Combine with a GitHub Action to auto-generate a new README 

This action will generate a new README every time `main` changes. 

```yml
# build.yml

name: Build README

on:
  push:
    branches:
    - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repo
      uses: actions/checkout@v2
      # We need full history to introspect created/updated:
      with:
        fetch-depth: 0
    - name: Set up Python
      uses: actions/setup-python@v1
      with:
        python-version: 3.8
    - name: Configure pip caching
      uses: actions/cache@v1
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Build database
      run: python build_database.py
    - name: Update README
      run: |-
        python update_readme.py --rewrite
        cat README.md
    - name: Commit and push if README changed
      run: |-
        git diff
        git config --global user.email "readme-bot@example.com"
        git config --global user.name "README-bot"
        git diff --quiet || (git add README.md && git commit -m "📝 Updated Table of Contents")
        git push

```
