import pathlib
import sqlite_utils
import sys
import re

root = pathlib.Path(__file__).parent.resolve()

index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)

if __name__ == "__main__":
    db = sqlite_utils.Database(root / "til.db")
    by_topic = {}
    for row in db["til"].rows_where(order_by="topic"):
        by_topic.setdefault(row["topic"], []).append(row)

    # Alphabetize the topics
    topics = sorted(by_topic.keys())

    index = ["<!-- index starts -->"]
    for topic in topics:
        index.append("## {}\n".format(topic))

        # Sort rows within the topic by title alphabetically
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

    if "--rewrite" in sys.argv:
        readme = root / "README.md"
        index_txt = "\n".join(index).strip()
        readme_contents = readme.open().read()
        readme.open("w").write(index_re.sub(index_txt, readme_contents))
    else:
        print("\n".join(index))
