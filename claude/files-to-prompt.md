# Using `files-to-prompt` to generate an XML file for your Claude context

## Links

- [simonw/files-to-prompt](https://github.com/simonw/files-to-prompt)
- [Building files-to-prompt entirely using Claude 3 Opus](https://simonwillison.net/2024/Apr/8/files-to-prompt/)
- [Use XML tags to structure your prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
- [Claude Desktop](https://claude.ai/download)
- [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
- [aider](https://aider.chat)

## Notes

I've really seen the benefit of using [files-to-prompt](https://github.com/simonw/files-to-prompt) to zip up code files so [Claude can better consume them](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags) in my prompts.

My workflow is usually this:

1. Set up a `prompt.md` in my repo.
2. `pip install files-to-prompt`
3. Add an XML `<background>` tag with notes on the project, whatever background I want the AI to focus on, whatever expertise I want to reflect
4. Add an XML `<instructions>` tag with very specific instructions on what I want to accomplish (Something like "Use a custom template for this view `MyView`" or "Write a test that the `MyView` endpoint returns a 200")
5. Run `files-to-prompt -e py --cxml path/to/file1.py path/to/file2.py` and capture the output
6. Copy the output and paste it at the bottom of the `prompt.md`
7. Upload the `prompt.md` to [Claude Desktop](https://claude.ai/download), or pass it to whatever CLI tool (like [aider](https://aider.chat)) I am using to interact with Claude.
8. My prompt is usually something like "Read `prompt.md` and follow the instructions."

```md
# prompt.md
<background>
- You are a [whatever background I specify]
</background>

<instructions>
- Look at [whatever class or file I need]
- Do [very specific small task]
</instructions>

<documents>
This is the part where I paste in the output from `files-to-prompt`
</documents>
```

I use Claude Desktop a lot, and I like being able to reduce the number of files I need to upload because the Desktop app limits the number of files you can upload at once.

Some options to consider:

- `--ignore <pattern>`: Specify a pattern to ignore. This could be useful in getting whole apps but excluding everything in `migrations/`.
- `--ignore-ditignore`: Ignore the `gitignore`, and include all files.
- `-c/--cxml`: Output in Claude XML
- `-m/--markdown`: Output as Markdown
- `-o/--output <file>`: Output to a file

The [README](https://github.com/simonw/files-to-prompt?tab=readme-ov-file) has several examples of how to use different options to get the files you want in the format you want.
