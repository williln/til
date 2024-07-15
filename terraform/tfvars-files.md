# About Terraform and .tfvars files

## Links 

- [Terraform](https://www.terraform.io/)
- [.tfvars file](https://registry.terraform.io/providers/terraform-redhat/rhcs/latest/docs/guides/terraform-vars)

## About Terraform 

It's an infrastructure-as-code tool. As far as I can tell, it lets you do a lot of infrastructure via config files, among other things. 

<img width="1309" alt="Screenshot 2024-07-15 at 9 14 08 AM" src="https://github.com/user-attachments/assets/b289e622-bdaf-4a6b-adfe-37d628777c41">

## .tfvars file 

From the docs: 

> Terraform allows you to define variable files called *.tfvars to create a reusable file for all the variables for a project.

AKA, this is one of the examples of the infrastructure-via-config-file that Terraform enables. 

Example: 

```
account_role_prefix = ""
availability_zones   = [""]
cloud_region = ""
cluster_name = ""
operator_role_prefix = "
token = ""
url = "
```

> You can create multiple versions of this file, and then, apply and destroy using this file with the -var-file= flag.

You can also add your own variables to it. 

```
teams = [
  "sharks",
  "jets",
]
years = [
  1961,
  2021,
]
```

## Syntax 

There are some specific rules about syntax that are unfamiliar to me: [Variable values and format](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/variables/managing-variables#variable-values-and-format). At baseline, it seems to be strings and [its own Terraform syntax](https://developer.hashicorp.com/terraform/language/syntax/configuration). You can also use JSON, apparently, but the docs don't sound keen on that:

> The constructs in the Terraform language can also be expressed in JSON syntax, which is harder for humans to read and edit but easier to generate and parse programmatically.
