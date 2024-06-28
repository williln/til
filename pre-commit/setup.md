# Setting up `pre-commit` in a new project 

## Links 

- [pre-commit](https://pre-commit.com/)

## Instructions 

- Install with `pip install pre-commit` in your local dev environment. Even though I work in Docker environments, I still use a virtualenv so I don't need to rebuild a container every time I run pre-commit.
- Add a `.pre-commit-config.yaml` file
- Add the things you want linted to that config file
- The first time you run pre-commit, run `pre-commit run --all-files` if you want to lint your whole codebase at once
- After that, run `pre-commit run` and only the files you changed will be linted

## My config file 

- [adamchainz/blacken-docs: Run \`black\` on python code blocks in documentation files](https://github.com/adamchainz/blacken-docs)
- https://github.com/psf/black
- https://github.com/pycqa/isort
- https://github.com/prettier/prettier

```yaml
default_language_version:
  python: python3.12

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml

  - repo: https://github.com/adamchainz/blacken-docs
    rev: 1.16.0
    hooks:
      - id: blacken-docs

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
    - id: isort

```
