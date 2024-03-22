# Fork a copy of your own repo 

I wanted to create a `til-life` repo by forking this one and then just resetting everything so I would have a place to put my life notes like recipe ideas. But the UI makes it hard to fork your own repo. So this is what ChatGPT and I came up with. I used my own cloning of this repo into [til-recipes](https://github.com/williln/til-recipes) as an example. 
## Create a bare clone of your original repo 

In the directory you want your new repo to go, run: 

```bash
git clone --bare git@github.com:williln/til.git
```

## Create the new repo 

Create a new, totally empty repo with the name you want. I chose `williln/til-recipes`. 

## Mirror-push to the new repo 

> With the bare clone, you now mirror-push to the new repository. However, since you want a fresh history, you'll first need to create the new repository on your preferred Git hosting service (e.g., GitHub, GitLab) without initializing it with a README, license, or .gitignore files.

> Once the new repository is created (e.g., til-life), push the content of the original repository

```bash
cd til
git push --mirror git@github.com:williln/til-recipes.git
```

## Remove the bare clone 

```bash
cd .. 
rm -rf til.git
```
## Clone your new repo where you want it to be 

```bash
git clone git@github.com:williln/til-recipes.git
```

Now I can see all my TIL files in my til-recipes repo. 



--- 

All done! 
