# Setting up Kubernetes access on MacOS with a config file 

Disclaimer: I don't know if I am getting some of this wrong. These are very much rough, personal notes. 

Goal: Connect to a client's remote cluster from my work Macbook Pro. 

## 1. Download the config file

I had the link from a colleague. It saved in my Downloads folder.

## 2. Set the `KUBECONFIG` Environment Variable

Next, I needed to tell my terminal to use this config file when running Kubernetes commands:

```bash
export KUBECONFIG=~/Downloads/kubeconfig.yaml
```

This tells the system, "Use this file for Kubernetes configurations."

## 3. Check the Configuration

To make sure everything's working, I ran:

```bash
kubectl config view
```

This should spit out the contents of my `kubeconfig.yaml` file. 

## 4. Alias this config file 

This will let me quickly switch to this client's config file when I need to. 

```bash
alias k-client="export KUBECONFIG=~/Downloads/kubeconfig.yaml"
```
