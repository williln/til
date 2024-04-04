# Securing Meilisearch with Docker for local Django development 

This is a follow-up to [Setting up Meilisearch with Python, Docker, and Compose for local development](https://github.com/williln/til/blob/main/meilisearch/setting_up_meilisearch_python_docker.md). 

## Links 

- [Securing your project](https://www.meilisearch.com/docs/learn/security/basic_security)

## Step 1: Add environment variables 

To my `.env` file, I added: 

```
# .env
# Meilisearch key 
MEILISEARCH_KEY="changeme"
```

I also added it to `.env-dist`, the template this project uses for environment variables. 

## Step 2: Load Meilisearch with the variable 

In my Compose file, I enabled the variable. 

```yaml
# compose.yml
services:
  ...

  meilisearch:
    image: getmeili/meilisearch:v1.7
    ports:
      - "7700:7700"
    volumes:
      - ./meili-data:/meili-data
    environment:
      - MEILI_MASTER_KEY=${MEILISEARCH_KEY}
    command:
      - meilisearch
      - --http-addr=0.0.0.0:7700
    depends_on:
      - db
```

I also added `meilisearch` to what the `web` service depends on: 

```yaml
# compose.yml
  web:
    depends_on:
      - db
      - meilisearch
```

## Step 3: Load the setting in `settings.py` 

I added this to `settings.py`: 

```python
# Meilisearch settings
import environs
env = environs.Env()
MEILISEARCH_KEY = env("MEILISEARCH_KEY", default="")
```

Note: This project uses [`environs`](https://pypi.org/project/environs/), which I love because I just never have to think about my environment variables.  

## Step 4: Put it all together 

Now, I want to be able to index the `movies.json` file via a management command run from inside my `web` container, which will enable me to search via the `localhost:7700` Meilisearch UI, or via a Django shell. (The `movies.json` file is from the example in the [Quick start](https://www.meilisearch.com/docs/learn/getting_started/quick_start).)

My management command (assumes that `movies.json` is located at the root level of the project): 

```python
# my_app/management/commands/index.py
from __future__ import annotations

import djclick as click
import meilisearch
import json

from django.conf import settings

@click.command()
@click.option("--verbose", is_flag=True, default=False)
def main(verbose):
    """Index Meilisearch."""
    client = meilisearch.Client('http://meilisearch:7700', settings.MEILISEARCH_KEY)
    json_file = open('movies.json', encoding='utf-8')
    movies = json.load(json_file)
    client.index('movies').add_documents(movies)
```

Note on `Client('http://meilisearch:7700', settings.MEILISEARCH_KEY)`: The url is `meilisearch:7700` and not `localhost:7700` because of Docker. The url should match the service name and port specified in the Compose file. 

I ran `docker compose up` to restart my services, then ran `./manage.py index` to run my management command in another window. I could see successful output in the console, and I could see my movies indexed once again on `http://localhost:7700/`. 

--- 

But my Meilisearch Docker volume doesn't seem to be persisting, so I'm sure that will be the subject of a future TIL. 
