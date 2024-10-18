# Naming a `git stash` and re-applying it later 

> Disclaimer: Not a git expert. 

Helped out by this [StackOverflow](https://stackoverflow.com/a/49559472) and the [`git stash docs`](https://git-scm.com/docs/git-stash#Documentation/git-stash.txt-push-p--patch-k--no-keep-index-u--include-untracked-a--all-q--quiet-m--messageltmessagegt--ltpathspecgt82308203)

## Name the code in your `git stash`

`git stash push -m "message"`

## See your stashes 

`git stash list` 

This command will output something like: 

```
stash@{0}: On develop: perf-spike
stash@{1}: On develop: node v10
```

## Apply a stash

`git stash apply {n}` 

Where `n` corresponds to the integer in `stash@{n}` from your `git stash list` output. 

## Delete a single stash 

`git stash drop {n}` 

## Delete all stashes 

All means all. 

`git stash clear` 

