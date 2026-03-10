# Using Claude Rules (`.claude/rules/`)

## Links

- [Official docs](https://code.claude.com/docs/en/memory#organize-rules-with-claude-rules)

## Intro

Claude rules let you organize persistent instructions into focused, topic-specific files rather than cramming everything into one `CLAUDE.md`. They live in `.claude/rules/` and can be optionally scoped to specific file paths so they only load into context when relevant.

## How they work

- Each `.md` file in `.claude/rules/` covers one topic (e.g. `testing.md`, `api-design.md`)
- Rules without path scoping load at every session start, just like `CLAUDE.md`
- Rules **with** path scoping only load when Claude works with matching files (saving tokens and context space)

### Path-scoped rule syntax

```markdown
---
paths:
  - "src/api/**/*.py"
  - "tests/**/*.py"
---

Your rules here...
```

## What to put in rules files

Good candidates for `.claude/rules/` files:

- **Testing conventions**: test structure, fixtures, naming, what to mock vs. not mock
- **API design patterns**: endpoint conventions, request/response shapes, error formats
- **Model/schema conventions**: field naming, validation patterns, relationship design
- **Frontend patterns**: component structure, styling approach, mobile-first considerations
- **External API rules**: rate limiting, caching, retry behavior
- **Code style**: formatting, import order, docstring conventions
- **Security rules**: never log PII, always validate at boundaries, authentication patterns
- **Deployment notes**: environment variable conventions, secrets handling

Keep each file focused and brief; I am for under ~50 lines. The more specific the instruction, the more reliably Claude follows it.

## Example: `testing.md`

```markdown
---
paths:
  - "tests/**/*.py"
  - "**/test_*.py"
---

# Testing Conventions

- Use pytest and model-bakery for all tests
- Use `baker.make()` for fixture creation; avoid manual model instantiation
- Test files mirror the module they test: `myapp/models.py` → `tests/test_models.py`
- Name tests `test_<what it does>_<expected outcome>`, e.g. `test_add_work_returns_201`
- Don't test Django internals. Test behavior at the service/API boundary
- Mock external HTTP calls; never make real network calls in tests
- One assertion per test where practical; use `pytest.mark.parametrize` for multiple cases
- Run tests with `pytest -x` (fail fast) during development
```

## Tips

- Keep `CLAUDE.md` to high-level project overview and architecture, and push specifics into rules files
- Use path scoping. Rules that only apply to test files shouldn't load when editing templates
- Review rules periodically to remove anything stale or contradictory
- If two rules conflict, Claude may pick one arbitrarily, so review rules to reduce overlap and consolidate files when necessary.
- You don't need to refer to your rules from within your `CLAUDE.md` file. As long as they are in `.claude/rules/`, Claude will discover them.
- Make rules directive ("Do this and not that") and specific
- Add short code examples inline to provide Claude with an example to follow
