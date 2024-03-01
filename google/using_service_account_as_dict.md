# Using Google Cloud Service Accounts and authenticating as a dictionary (without the json file) in a Django project 

`gspread` showed a quick example of how to use a dictionary to authenticate against the google API, instead of messing with the JSON file you have to download: [Authentication - For bots using a service account — gspread 5.7.2 documentation](https://docs.gspread.org/en/latest/oauth2.html#for-bots-using-service-account) 

Here's a full example of what I did: 

## Step 1: Create a Google Cloud Platform Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project

## Step 2: Enable the Google Sheets API

1. In your new project, navigate to the "API & Services > Dashboard" panel.
2. Click on “ENABLE APIS AND SERVICES”.
3. Search for "Google Sheets API" and enable it.
4. Search for "Google Drive API" and enable it also. 

## Step 3: Create a Service Account

1. Go to "IAM & Admin > Service accounts" from the side menu.
2. Click on "Create Service Account".
3. Enter a name and description for the service account.
4. Click "Create".
5. I skipped assigning roles because the sheets I need are public. 
6. Click "Done".

## Step 4: Create and Download the JSON Key

1. In the service accounts list, click on the newly created service account.
2. Go to the "Keys" tab.
3. Click "Add Key" and choose "Create new key".
4. Select "JSON" as the key type and click "Create".
5. The JSON key file will be downloaded to your computer. Secure this file as it provides access to your service account.

## Step 5: Share the Sheet with Your Service Account

> Note: If you don't own the sheet and the sheet is public, just skip this step. It will still work. 

1. Open the public Google Sheet in your web browser.
2. Click the "Share" button.
3. Enter the service account's email (found on the service account page in the IAM & Admin section of the Google Cloud Console).
4. Grant "Viewer" access to the service account.

## Step 6: Install the `gspread` Library

Install `gspread` via pip:

```sh
pip install gspread
```

Or however you like to manage your dependencies. 

## Step 7: Add env variables and set up the auth dict 

Get all these values from the `.json` file you downloaded earlier. 

```
# .env

GOOGLE_PROJECT_ID="changeme"
GOOGLE_PRIVATE_KEY_ID="changeme"
GOOGLE_PRIVATE_KEY="changeme"
GOOGLE_CLIENT_EMAIL="changeme"
GOOGLE_CLIENT_ID="changeme"
GOOGLE_CLIENT_X509_CERT_URL="changeme"
```

```python
# settings.py
GOOGLE_CREDENTIALS = {
    "type": "service_account",
    "project_id": os.environ.get("GOOGLE_PROJECT_ID", None),
    "private_key_id": os.environ.get("GOOGLE_PRIVATE_KEY_ID", None),
    "private_key": os.environ.get("GOOGLE_PRIVATE_KEY", None),
    "client_email": os.environ.get("GOOGLE_CLIENT_EMAIL", None),
    "client_id": os.environ.get("GOOGLE_CLIENT_ID", None),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get("GOOGLE_CLIENT_X509_CERT_URL", None),
    "universe_domain": "googleapis.com",
}

```

## Step 8: Authenticate and Access the Sheet Using `gspread`

Here's a simple management command that demonstrates how to use `gspread` with a service account to access a Google Sheet:

```python
import djclick as click
import gspread
from django.conf import settings


@click.command()
def command():
    # Authenticate with Google sheets
    gc = gspread.service_account_from_dict(settings.GOOGLE_CREDENTIALS)

    # Open the main sheet
    sheet = gc.open_by_key(settings.MY_GOOGLE_SHEET_ID)
```
