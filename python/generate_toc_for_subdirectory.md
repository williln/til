# Generating a clickable table-of-contents for each directory in my TILs 

## Use case 

I have a GitHub Action that rewrites my main README every time I commit to `main` to regenerate the table of contents, sorted by directory. 

I wanted a README in each directory with its own table of contents. 

## Code 

```python
# scripts/build_subdir_toc.py
import os

import click

# Takes a directory as an argument 
@click.command()
@click.argument("directory", type=click.Path(exists=True))
def generate_readme_links(directory):
    """
    Generate a README file with clickable links to all files in the specified directory.

    DIRECTORY: The path to the directory containing files.
    """
    readme_file = os.path.join(directory, "README.md")

    with open(readme_file, "w") as f:
        # Use first h1 as the header for the readme 
        header = os.path.basename(directory)
        f.write(f"# {header}\n\n")

        for root, dirs, files in os.walk(directory):
            contents = []
            for file in files:
                title = None
                # Read the file so I can get the file's header, which is the TIL title.
                with open(os.path.join(root, file), "r") as file_obj:
                    title = file_obj.readline().replace("#", "").strip()

                # Skip files that don't have a title.
                if not title:
                    continue

                # Generate the URL for the file, so the TIL titles are clickable 
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)

                # Write the next list item with a link to this file 
                contents.append(f"- [{title}]({relative_path})")

            # Alphabetize by title 
            sorted_contents = sorted(contents)
            f.write("\n".join(sorted_contents))

    click.echo(f"README file generated at {readme_file}")


if __name__ == "__main__":
    generate_readme_links()
```

Example call: 

```bash
python3 scripts/build_subdir_toc.py django-rest-framework
```

This generates something like: 

```markdown
# django-rest-framework

- [Adding a custom pagination class to an action](custom_action_pagination.md)
- [Passing extra info in `context` to your DRF serializer](pass_to_context.md)
```

## GitHub Action 

> Note: This is currently broken. The Action "succeeds" but the README didn't change. 

Then, I added calls to this script for each TIL directory I wanted to include to the existing GitHub action. 

```yaml
name: Build README

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      ...
      - name: Update subdir README's 
        run: |-
          python3 scripts/build_subdir_toc.py aws
          python3 scripts/build_subdir_toc.py celery
          python3 scripts/build_subdir_toc.py django
       ...
```

### Why aren't you just traversing all your directories? 

I tried that, but I was getting some internal directories. As I was coding an EXCLUDED list, I decided I preferred an ALLOW list. 

This does mean that I will need to manually add a new line to the GitHub action whenever I create a new TIL directory, but I am comfortable with that. Even if I don't get around to it, the main TIL README will still update, so it's an inconvenience I can live with. Also, I'm tired. 

--- 

## Notes 

- As soon as I finished, it occured to me that I could have done this in a DRY-er way by re-using more of the code in `update_readme.py`. But I was re-using code from a side project that worked a little differently, so I tried a different pattern. 
- I tried to move the scripts for the project-level README into `scripts/` but there was a git-related `InvalidGitRepositoryError` error that I didn't feel like debugging, so I just moved them back out.
