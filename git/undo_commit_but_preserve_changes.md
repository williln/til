# `git reset`, with `soft`: Undo your last commit but keep your changes 

## Use case 

I needed to make some changes in `branch-a` to satisfy some PR comments, but I had some messy, in-progress work on `branch-b`. `branch-b` wasn't working, I've changed a lot of files, I'm kind of midstream. But I'm about to go into a meeting so I'm losing focus anyway. I want to preserve my changes, so I just commit them all with the comment "🚧". 

I attend my meeting, checkout `branch-a` and make my changes. 

Back from the meeting, the PR changes, and lunch, I can't remember exactly what I was doing. I rebuild and my memory is jogged... oh yeah, weird error and I don't know why. I am no closer to discovering why it's happening. Worse, because I committed my changes, I can't even see a diff of my changes unless I push them, which I don't want to do because I hate rebasing and I know that, once I untangle myself from the mess I made, I will want to make a few neat, explanatory commits and not one big spaghetti one.

So I want to undo my last commit, the "🚧" one, but keep all the changes. I also want to ONLY undo my last commit, because I know I had a few others before that on this branch. 

## Links 

- Stack Overflow: [How to un-commit last un-pushed git commit without losing the changes](https://stackoverflow.com/questions/19859486/how-to-un-commit-last-un-pushed-git-commit-without-losing-the-changes)

## What to do 

```shell
git reset HEAD~1 --soft
```

This reverts the  commit, but retains the changes. They are also still staged for commit. This is what I see when I run `git status`: 

```shell
        modified:   docs/index.md
        modified:   mkdocs.yml
        modified:   path/to/other/file/I/modified.md
```

Now I can see where I was and start figuring my way out of the bug I was chasing. 
