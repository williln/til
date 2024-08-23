# Checking out someone else's branch 

## Use case 

A colleague has opened a PR. I want to check out their branch on my own machine so I can run it and test their changes 

## Instructions 

**Assumptions**: You have the repo checked out and set up locally on your machine. You work on it regularly. 

- Get the branch name that you want
- Back in your terminal, get thee to wherever you have this repo
- I always check out `main` and update it at this point, just to be fresh 
- Now run `git fetch` to load all the remote branches
- Then run `git checkout <branch-name>`

You are now in a new branch on your local machine that is a copy of the branch at the remote. 

Another "thing I have known for a while but sometimes forget." 
