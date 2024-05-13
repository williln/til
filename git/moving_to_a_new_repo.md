# Moving from an old repo to a new repo in another organization 

## Situation 

- Have been working in Repo A under Organization A for several months. We have PRs and issues in flight in this repo.
- It's now time to move to Repo B under Organization B, and archive Repo A. (Organization A will remain unaffected.)

## 1. Reveal current state 

```bash
$ git remote -v
origin  git@github.com:org-a/repo.git (fetch)
origin  git@github.com:org-a/repo.git (push)
upstream        git@github.com:org-b/repo.git (fetch)
upstream        git@github.com:org-b/repo.git (push)
```

I have different `origin` and `upstream` remotes because last week, I ran `git remote add upstream git@github.com:org-b/repo.git`. 

## 2. Add the new origin, if needed. 

```bash
$ git remote add upstream git@github.com:org-b/repo.git
```

## 3. Rename the old `origin` 

```bash
$ git remote rename origin old-origin 
```

## 4. Rename the new `upstream` to be the `origin` 

```bash
$ git remote rename upstream origin
```

## 5. Double check your remotes 

```bash
$ git remote -v
old-origin      git@github.com:org-a/repo.git (fetch)
old-origin      git@github.com:org-a/repo.git (push)
origin  git@github.com:org-b/repo.git (fetch)
origin  git@github.com:org-b/repo.git (push)
```

## 6. Fetch from your new origin 

```bash
$ git fetch origin
remote: Enumerating objects: 483, done.
remote: Counting objects: 100% (483/483), done.
remote: Compressing objects: 100% (81/81), done.
remote: Total 355 (delta 290), reused 338 (delta 273), pack-reused 0
Receiving objects: 100% (355/355), 93.96 KiB | 1.88 MiB/s, done.
Resolving deltas: 100% (290/290), completed with 106 local objects.
From github.com:org-b/repo
   f33bdcb..392008f  main       -> origin/main
```

On the second to last line, you will see the path to your new repo. 

## 7. Deal with issues 

In my case, we will be moving the open issues by and (as in, manually recreating them in the new repo) for a few reasons: 

- We have some dead issues that need to be closed
- We have some "internal" issues that we used for planning purposes and will be split into other issues, or closed
- The issues are not always well-organized, and this is an opportunity to start fresh with issues and not move the whole backlog
- The repos are owned by different organizations, making things a little harder: [Transferring an issue to another repository - GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/transferring-an-issue-to-another-repository) 

 ## 8. Archive the old repo 

 [Archiving repositories - GitHub Docs](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)
