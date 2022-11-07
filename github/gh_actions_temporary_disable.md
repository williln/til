# Temporarily disabling a GitHub action without touching the workflow file 

I have an action that I am working on refining the behavior of, but I don't want it to run when I'm not working on it. (At least... not until it's fixed and ready.) 

According to [the docs](https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow), doing this is simple: 

- Go to the Actions tab and select your workflow on the left 
- Next to the search bar in the upper right, click the three dots 
- Select **Disable workflow**
- The workflow won't run until you re-enable it, which you can do by clicking the button that says **Enable workflow**

## Disabling the workflow 
<img width="1636" alt="Screen Shot 2022-11-07 at 12 38 24 PM" src="https://user-images.githubusercontent.com/2286304/200411251-bd298ff8-0d34-4ce3-8b56-951d811dbf0e.png">

## Re-enabling the workflow 
<img width="1644" alt="Screen Shot 2022-11-07 at 12 38 31 PM" src="https://user-images.githubusercontent.com/2286304/200411312-8d18ff79-1c10-40bd-bfa9-4199c4a8e4f2.png">
