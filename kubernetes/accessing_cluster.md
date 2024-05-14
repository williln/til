# Accessing a Kubernetes cluster for the first time 

## 1. Ensure Your Config File is Set

First, make sure you’ve set the `KUBECONFIG` environment variable to point to the correct config file for the project you’re working on: 


```bash
export KUBECONFIG=~/path/to/kubeconfig.yaml
```

## Check your context

Verify that you’re connected to the right cluster by checking the current context:

```bash
kubectl config current-context
```

This command should output the name of the current context specified in your `kubeconfig.yaml`.

## Getting cluster info 

Display information about your Kubernetes cluster:

```bash
$ kubectl cluster-info
Kubernetes control plane is running at https://redacted
CoreDNS is running at https://redacted-proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

## Common commands

### List All Nodes:

```bash
$ kubectl -n [namespace] get nodes
NAME                      STATUS   ROLES    AGE   VERSION
default-node-pool-qwer3   Ready    <none>   24   v1.00.1
default-node-pool-qwer7   Ready    <none>   24   v1.00.1
```

### List All Pods in the Default Namespace:

```bash
$ kubectl -n [namespace] get pods
No resources found in default namespace.
```

### List All Services in the Default Namespace:

```bash
$ kubectl -n [namespace] get services
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   00.000.0.1   <none>        443/TCP   24d
```
### Open a Shell to a Running Container:

```bash
$ kubectl exec -it <pod-name> -- /bin/bash
```

This command is particularly useful for debugging issues directly inside the container or running management commands. 
