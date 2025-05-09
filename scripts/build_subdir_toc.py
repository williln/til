import os

import click


@click.command()
@click.argument("directory", type=click.Path())
def generate_readme_links(directory):
    """
    Generate a README file with clickable links to all files in the specified directory.

    DIRECTORY: The path to the directory containing files.
    """

    readme_file = os.path.join(directory, "README.md")

    with open(readme_file, "w") as f:
        # Use first h1 as the header
        header = os.path.basename(directory)
        f.write(f"# {header}\n\n")

        # Only process files if the directory exists and has files
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                contents = []
                for file in files:
                    # Skip the README file
                    if file == "README.md":
                        continue

                    file_path = os.path.join(root, file)

                    try:
                        # Read the file so I can get the header, which contains the title
                        with open(os.path.join(root, file), "r") as file_obj:
                            title = file_obj.readline().replace("#", "").strip()

                        # Skip files that don't have a title
                        if not title:
                            continue

                        relative_path = os.path.relpath(file_path, directory)
                        contents.append(f"- [{title}]({relative_path})")
                    except Exception as e:
                        click.echo(f"Warning: Could not process file {file}: {e}")

                sorted_contents = sorted(contents)
                f.write("\n".join(sorted_contents))

    click.echo(f"README file generated at {readme_file}")


if __name__ == "__main__":
    generate_readme_links()
