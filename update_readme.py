import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

# Regular expressions to find headings and the placeholders in the markdown file
heading_re = re.compile(r"^(#{1,6})\s+(.*)", re.MULTILINE)
index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
toc_re = re.compile(r"<!\-\- toc starts \-\->.*<!\-\- toc ends \-\->", re.DOTALL)


def generate_toc(contents):
    """Generate a Table of Contents from the README"""
    toc = ["<!-- toc starts -->"]
    for match in heading_re.finditer(contents):
        level = len(match.group(1))
        title = match.group(2)
        slug = re.sub(r"\W+", "-", title.lower()).strip("-")
        # Only pick up H3 and lower
        if level >= 3:
            toc.append(f'{"  " * (level - 3)}* [{title}](#{slug})')
    toc.append("<!-- toc ends -->")
    return "\n".join(toc)


def generate_index():
    """Generate an index of all TILs by topic"""
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="topic"):
        by_topic.setdefault(row["topic"], []).append(row)

    topics = sorted(by_topic.keys())

    index = ["<!-- index starts -->"]
    for topic in topics:
        index.append("### {}\n".format(topic))
        rows = sorted(by_topic[topic], key=lambda x: x["title"].lower())
        for row in rows:
            index.append(
                "* [{title}]({url}) - {date}".format(
                    date=row["created"].split("T")[0], **row
                )
            )
        index.append("")

    if index[-1] == "":
        index.pop()

    index.append("<!-- index ends -->")
    return "\n".join(index)


if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.read_text()

    # Generate index
    index = generate_index()

    # Update index in README
    if index_re.search(readme_contents):
        readme_contents = index_re.sub(index, readme_contents)
    else:
        readme_contents = f"{index}\n\n{readme_contents}"

    # Generate TOC
    toc = generate_toc(readme_contents)

    # Update TOC in README
    if toc_re.search(readme_contents):
        readme_contents = toc_re.sub(toc, readme_contents)
    else:
        readme_contents = f"{toc}\n\n{readme_contents}"

    # Rewrite README
    if "--rewrite" in sys.argv:
        readme.write_text(readme_contents)
    else:
        print(readme_contents)
