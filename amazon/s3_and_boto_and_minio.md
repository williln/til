# AWS S3 and Boto3 Cheat Sheet

_Note: This was written almost entirely by ChatGPT and lightly edited by me after a lengthy Q&A session where I was asking it to help me understand interacting with S3._ 

This cheat sheet covers the basics of interacting with AWS S3 using Boto3 and Python. It includes examples of listing, reading, and downloading objects from an S3 bucket.

## Boto3 

### Setup

Install the required packages:
```bash
pip install boto3
```
 
Configure AWS CLI:

```bash
aws configure
```
  
In your Python script, import Boto3:

```python
import boto3
```

### Operations 

#### List Buckets

```python
s3 = boto3.client('s3')
response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print("Bucket List: {}".format(buckets))

```

#### List Objects in a Bucket

```python
bucket_name = 'your_bucket_name'
response = s3.list_objects_v2(Bucket=bucket_name)
objects = [obj['Key'] for obj in response['Contents']]
print("Objects in bucket: {}".format(objects))
```

#### List Objects with a Prefix
```python
prefix = 'your_prefix/'
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
objects = [obj['Key'] for obj in response['Contents']]
print("Objects with prefix '{}': {}".format(prefix, objects))
```

#### Download an Object from S3
```python
import os

key = 'path/to/your/object'
local_folder = 'your_local_folder'
os.makedirs(local_folder, exist_ok=True)
local_path = os.path.join(local_folder, os.path.basename(key))

with open(local_path, 'wb') as f:
    s3.download_fileobj(bucket_name, key, f)
```

#### Download the First Markdown File from an S3 Bucket
```python
def find_and_save_first_md_file(bucket_name):
    continuation_token = None

    while True:
        if continuation_token:
            response = s3.list_objects_v2(Bucket=bucket_name, ContinuationToken=continuation_token)
        else:
            response = s3.list_objects_v2(Bucket=bucket_name)

        markdown_object = None
        for obj in response.get('Contents', []):
            if obj['Key'].endswith('.md'):
                markdown_object = obj
                break

        if markdown_object:
            local_folder = 'markdown_files'
            os.makedirs(local_folder, exist_ok=True)

            key = markdown_object['Key']
            local_path = os.path.join(local_folder, os.path.basename(key))

            with open(local_path, 'wb') as f:
                s3.download_fileobj(bucket_name, key, f)
            print(f"Downloaded {key} to {local_path}")
            break

        if response.get('IsTruncated'):
            continuation_token = response['NextContinuationToken']
        else:
            print("No markdown files found in the bucket.")
            break

bucket_name = 'stage.boost.org'
find_and_save_first_md_file(bucket_name)
```
This script paginates through objects in the specified S3 bucket and stops when it finds and saves the first object with an .md suffix. If no markdown files are found, it prints "No markdown files found in the bucket."
