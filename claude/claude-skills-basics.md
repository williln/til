# Creating a Basic Claude Code Skill

## Links

- [Official Claude skills docs](https://code.claude.com/docs/en/skills)

## What are skills?

Skills are reusable instructions that extend what Claude Code can do. You create a `SKILL.md` file, and Claude adds it to its toolkit. Claude can load skills automatically when they're relevant, or you can invoke one directly with `/skill-name` as a slash command.

Skills augment the older `.claude/commands/` approach (though those files still work). Skills add optional features: a directory for supporting files, frontmatter to control invocation, and automatic loading when relevant.

## Where skills live

| Location | Path | Applies to |
|----------|------|------------|
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |

Personal skills follow you everywhere; project skills are specific to the repo they are in. You can choose to commit them to your codebase so your team shares them.

## Anatomy of a skill

Every skill needs a `SKILL.md` file inside a named directory. The file has two parts: YAML frontmatter and markdown content.

Here's my `/emoji-commit` skill as a real example. This skill looks at staged changes and comes up with a commit message, prefixed with an emoji, for those changes. I can then copy that commit message and use it.

```markdown
---
name: emoji-commit
description: Use when ready to commit staged changes and want an emoji commit message to copy/paste
---

# Emoji Commit Message

## Workflow

1. Run `git diff --staged` to review changes
2. Select emoji based on change type (see table)
3. Output commit message in format: `:emoji: Brief description`

Do not commit yourself.

## Emoji Reference

| Emoji | Code | Use For |
|-------|------|---------|
| 📚 | `:books:` | Documentation |
| 🚑 | `:ambulance:` | Bug fix |
| ✨ | `:sparkles:` | New feature |
| 🔨 | `:hammer:` | Refactoring |
| ... | ... | ... |

## Output Format

Output ONLY the commit message line for easy copy/paste.
```

The file lives at `.claude/skills/emoji-commit/SKILL.md`.

## Frontmatter

The frontmatter between `---` markers configures how the skill behaves. All fields are optional, but `description` is recommended so Claude knows when to use the skill.

Key fields:

- **`name`**: The slash command name. If omitted, uses the directory name. Lowercase, numbers, and hyphens only.
- **`description`**: What the skill does and when to use it. Claude uses this to decide when to load it automatically.
- **`disable-model-invocation`**: Set to `true` to prevent Claude from loading it on its own. The skill only runs when you type `/skill-name`.
- **`user-invocable`**: Set to `false` to hide from the `/` menu. Use for background knowledge Claude should apply automatically but that isn't useful as a direct command.
- **`allowed-tools`**: Restrict which tools Claude can use when the skill is active (e.g., `Read, Grep, Glob` for a read-only skill).
- **`context`**: Set to `fork` to run in an isolated subagent context.

## Arguments

Skills can accept arguments via the `$ARGUMENTS` placeholder:

```markdown
---
name: fix-issue
description: Fix a GitHub issue
---

Fix GitHub issue $ARGUMENTS following our coding standards.
```

Running `/fix-issue 123` replaces `$ARGUMENTS` with `123`. You can also access individual arguments with `$ARGUMENTS[0]`, `$ARGUMENTS[1]`, etc. (or shorthand `$0`, `$1`).

## Tips

- Keep `SKILL.md` as short as you reasonably can; move detailed reference material to separate files in the skill directory
- Write a clear `description` with keywords that match how you'd naturally ask for help, so Claude triggers the skill at the right time
- Start simple: a name, description, and a few markdown instructions is all you need to start playing with skills
- There's a lot more information in [Official Claude skills docs](https://code.claude.com/docs/en/skills) so I recommend giving this a skim before you get started.
