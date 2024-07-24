# Running your tests with `pytest` in your PR via a GitHub Action 

tags: ci, pytest, github-actions

## Links 

- [Building and testing Python - GitHub Docs](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) 

## Process 

I decided to follow the [Using a Python starter workflow](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#using-a-python-starter-workflow) process, at least initially. I've done this before, but I can't remember how and it's been a while. It seems best to return to the docs and see how we do things _now_. 

Their automated builder spit out a workflow that I made a few changes to: 

- I deleted their linting step because I have a pre-commit hook for that 
- I updated their `setup-python` version from 3 to 5. 

```yaml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.12
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        pytest
```

On every PR and push to `main`, this workflow: 

- Installs Python 3.12 
- Installs `pytest`
- Installs the `requirements.txt`
- Runs `pytest` 

It worked right there in the PR that I made it in! 
