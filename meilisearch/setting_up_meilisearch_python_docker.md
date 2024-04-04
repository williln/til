# Setting up Meilisearch with Python, Docker, and Compose for local development 

This is a record of what I wound up doing to get the equivalent of a "Hello World" when setting up Meilisearch in my Django project. For me, the "Hello World" is being able to complete the [Quick Start](https://www.meilisearch.com/docs/learn/getting_started/quick_start) example with the `movies.json` file within the Dockerized context of my project.  

- [Meilisearch](https://www.meilisearch.com) 1.7
- [Docker](https://www.docker.com/) and [Compose](https://docs.docker.com/compose/)
- For a Django 5.0 project

## Step 1: Install Meilisearch 

- Add `meilisearch` to `requirements.in` and run the commands to generate the `requirements.txt`

This enables me to run `import meilisearch` from within my project modules. 

---

After I completed Step 1, I ran `./manage.py shell` from within my `web` container and tried execute the sample: 

- Downloaded the `movies.json` file and moved it into my project directory
- Ran this code:

```python
import meilisearch
import json

client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

json_file = open('movies.json', encoding='utf-8')
movies = json.load(json_file)
client.index('movies').add_documents(movies)
```

On the last line, I got an error:

```
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='localhost', port=7700): Max retries exceeded with url: /indexes/movies/documents (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0xffffb4b34d90>: Failed to establish a new connection: [Errno 111] Connection refused'))
```

So I figured I needed to add the service to Compose. Meilisearch needs to be running in its own instance; it doesn't run alongside the web container. 

This made sense once I thought about it -- one of the quickstart instructions is to [run meilisearch](https://www.meilisearch.com/docs/learn/getting_started/quick_start#running-meilisearch), so obviously I needed to do something to make that happen. 

---

## Step 2: Add Meilisearch service to Compose 

This is incomplete -- I only showed the parts relevant to `meilisearch`. 

```yaml
services:

  db:
    ....

  meilisearch:
    image: getmeili/meilisearch:v1.7
    ports:
      - "7700:7700"
    volumes:
      - ./meili-data:/meili-data
    # environment:
    #   - MEILI_MASTER_KEY=your_master_key_here
    command:
      - meilisearch
      - --http-addr=0.0.0.0:7700
    depends_on:
      - db

  web:
    depends_on:
      - db
    ports:
      - "8000:8000"

volumes:
  meili-data:
  postgres-data:

```

---

After I added this, I rebuilt my Docker image and restarted my services with `just up`. I could see the Meilisearch Dashboard at `http://localhost:7700/`, but it was asking me for an API key.

Instead of setting one, I commented out the `MEILI_MASTER_KEY` (in the spirit of getting through the "Hello World" first. But I will add this back in later, I promise). 

## Step 3: Hello, World 

I ran the first part of the "hello world" commands from the command line: 


```bash
>>> import json
>>> client = meilisearch.Client('http://localhost:7700')
>>> json_file = open('movies.json', encoding='utf-8')
>>> movies = json.load(json_file)
>>> client.index('movies').add_documents(movies)
TaskInfo(task_uid=0, index_uid='movies', status='enqueued', type='documentAdditionOrUpdate', enqueued_at=datetime.datetime(2024, 4, 4, 17, 9, 48, 254011))
```


After this, and with the compose file above, I was able to see the movies on the Meilisearch dashboard: 

<img width="1721" alt="Screenshot 2024-04-04 at 10 34 46 AM" src="https://github.com/williln/til/assets/2286304/e85c1af9-066a-40d1-acf8-91c8ad1681a9">

I can also search on the dashboard: 

<img width="958" alt="Screenshot 2024-04-04 at 10 37 37 AM" src="https://github.com/williln/til/assets/2286304/6934b211-3aa4-434a-bacb-6616048271cd">

Here is the output from the rest of the quick start commands: 

```bash
>>> client.get_task(0)
Task(uid=0, index_uid='movies', status='succeeded', type='documentAdditionOrUpdate',
details={'receivedDocuments': 31944, 'indexedDocuments': 31944}, error=None,
canceled_by=None, duration='PT3.438210921S', enqueued_at=datetime.datetime(2024,
4, 4, 17, 9, 48, 254011), started_at=datetime.datetime(2024, 4, 4, 17, 9, 48, 262717),
finished_at=datetime.datetime(2024, 4, 4, 17, 9, 51, 700927))


>>> client.index("movies").search("eras")
{'hits': [{'id': 985, 'title': 'Eraserhead', 'overview': 'Henry Spencer tries to survive
his industrial environment, his angry girlfriend, and the unbearable screams of his
newly born mutant child.', 'genres': ['Fantasy', 'Horror'], 'poster':
'https://image.tmdb.org/t/p/w500/fjq2xZvWWKZJtg8FGNHXdbVoAAf.jpg', 'release_date':
255312000}, {'id': 9268, 'title': 'Eraser', 'overview': "U.S. Marshall John Kruger
erases the identities of people enrolled in the Witness Protection Program. His
current assignment is to protect Lee Cullen, who's uncovered evidence that the weapons
manufacturer she works for has been selling to terrorist groups. When Kruger discovers
that there's a corrupt agent within the program, he must guard his own life while
trying to protect Lee's.", 'genres': ['Action', 'Drama', 'Mystery', 'Thriller'],
'poster': 'https://image.tmdb.org/t/p/w500/rcXxBhE6npESFZhHBMRuaTeQXOs.jpg', 'release_date':
835315200},...], 'query': 'eras', 'processingTimeMs': 1, 'limit': 20, 'offset': 0,
'estimatedTotalHits': 38}
```

## More Links 

- Meilisearch docs: [Installation](https://www.meilisearch.com/docs/learn/getting_started/installation)
- Meilisearch docs: [Securing your project](https://www.meilisearch.com/docs/learn/security/basic_security)
- Meilisearch docs: [Using Meilisearch with Docker](https://www.meilisearch.com/docs/learn/cookbooks/docker)

## What's Next 

- [Security](https://www.meilisearch.com/docs/learn/security/basic_security)
- Index data from my own project 
