# How to use a Github Action

Refer to `til/build.yml` for examples.

GitHub Actions use YAML, so create a `build.yml` file in your project root.

```yaml
name: Build README
```

The name of your action.

```yaml
on:
  push:
    branches:
    - main
```

When you want this action to run. In this case, we want to run it when we push to the `main` branch.

```yaml
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
    - uses: actions/cache@v1
      name: Configure pip caching
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
        git diff --quiet || (git add README.md && git commit -m "Updated README")
        git push

```

What we want the action to execute. This action will run the `build` job, which has several steps:

- `Check out repo`: Check out the repository to inspect when files were created/updated. This uses an existing GitHub Action [`checkout@v2`](https://github.com/actions/checkout)
- `Set up Python`: Prepare a Python environment using 3.8, with the [`actions/setup-python@v1`](https://github.com/actions/setup-python) action. This also installs pip.
- Configures pip
- Installs dependencies from `requirements.txt`
- Runs `build_database.py`
- Runs `update_readme.py`
- Creates a commit and pushes if the README changed

## Further Reading

- [Using a self-rewriting README powered by GitHub Actions to track TILs](https://simonwillison.net/2020/Apr/20/self-rewriting-readme/)
