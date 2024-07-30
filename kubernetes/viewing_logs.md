# Viewing logs for your pod 

## Links 

- [Using Kubectl Logs | SigNoz](https://signoz.io/blog/kubectl-logs/)

## Instructions 

I went with the simplest incantation because I was looking at logs for the dev environment, and had just deployed, so I knew there wouldn't be many logs about the container I needed. 

First, get the ID of the pod you need logs for: 

```shell
kubectl -n [my-namespace] get pods      
```

Then, get the logs: 

```shell
kubectl -n [my-namespace] logs [my-pod-name] 
```

This printed out a lot of logs to my console, which I then copied and pasted into a file so I could peruse them more easily. 
