# Securing the Meilisearch search itself 

## Links 

- [Securing Your Project](https://www.meilisearch.com/docs/learn/security/basic_security)

## Goal 

I got Meilisearch set up locally in my Django project and was able to successful search, but because I [secured my Meilisearch instance](https://github.com/williln/til/blob/main/meilisearch/securing_meilisearch_in_docker.md), I had to pass an API key _in my Django template_ in the Javascript code. That's not something I'm even going to commit in this state, even with dummy data, so my next step was to figure out what I was supposed to do instead. 

## Example code 

From [Front-end integration](https://www.meilisearch.com/docs/learn/front_end/front_end_integration#lets-try-it): 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/templates/basic_search.css" />
  </head>
  <body>
    <div class="wrapper">
      <div id="searchbox" focus></div>
      <div id="hits"></div>
    </div>
  </body>
  <script src="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/dist/instant-meilisearch.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>
  <script>
    const search = instantsearch({
      indexName: "movies",
      searchClient: instantMeiliSearch(
        "http://localhost:7700",
        "my-meilisearch-key" // This is the key I had to add 
      ).searchClient
      });
      search.addWidgets([
        instantsearch.widgets.searchBox({
          container: "#searchbox"
        }),
        instantsearch.widgets.configure({ hitsPerPage: 8 }),
        instantsearch.widgets.hits({
          container: "#hits",
          templates: {
          item: `
            <div>
            <div class="hit-name">
                  {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
            </div>
            </div>
          `
          }
        })
      ]);
      search.start();
  </script>
</html>
```

Until I added my Meilisearch key, I got an error in the JS console:

```bash
User
MeiliSearchApiError: The Authorization header is missing. It must use the bearer authorization method.
```

That was my clue to add my key, and when I did, it worked. 

## Step 1: Read the docs 

Back to [Securing your project](https://www.meilisearch.com/docs/learn/security/basic_security). I found what I needed under [Obtaining API keys](https://www.meilisearch.com/docs/learn/security/basic_security#obtaining-api-keys): 

> When your project is protected, Meilisearch automatically generates two API keys: Default Search API Key and Default Admin API Key. API keys are authorization tokens designed to safely communicate with the Meilisearch API.

Based on the instructions further down the page, I used `curl` to retrieve my API keys: 

```bash
$ curl -X GET 'http://localhost:7700/keys' -H 'Authorization: Bearer my-meilisearch-key'
$ {
  "results": [
    {
      "name": "Default Search API Key",
      "description": "Use it to search from the frontend",
      "key": "my-search-key",
      "uid": "redacted",
      "actions": ["search"],
      "indexes": ["*"],
      "expiresAt": null,
      "createdAt": "2024-04-05T19:02:29.222201737Z",
      "updatedAt": "2024-04-05T19:02:29.222201737Z"
    },
    {
      "name": "Default Admin API Key",
      "description": "Use it for anything that is not a search operation. Caution! Do not expose it on a public frontend",
      "key": "my-admin-key",
      "uid": "redacted",
      "actions": ["*"],
      "indexes": ["*"],
      "expiresAt": null,
      "createdAt": "2024-04-05T19:02:29.220337412Z",
      "updatedAt": "2024-04-05T19:02:29.220337412Z"
    }
  ],
  "offset": 0,
  "limit": 20,
  "total": 2
}
```

I added those to my `.env` file and as settings: 

```python
# settings.py
MEILISEARCH_SEARCH_API_KEY = env("MEILISEARCH_SEARCH_API_KEY", default="")
MEILISEARCH_ADMIN_API_KEY = env("MEILISEARCH_ADMIN_API_KEY", default="")
```

Then, I added the search API key setting (as well as another setting I added, to set the search URL) to the context of the view that loaded my template, and folded them into the template: 

```html
  <script>
    const searchUrl = "{{ search_url }}";
    const searchApiKey = "{{ search_api_key }}";
  </script>
  <script>
    {% verbatim %}
        const search = instantsearch({
        indexName: "movies",
        searchClient: instantMeiliSearch(
            searchUrl,
            searchApiKey
        ).searchClient
        });
```

--- 

This does work, but there still feels like there is something missing, so I am sure more Meilisearch TILs will come. 

I wound up having this other problem where each time I restarted my Docker container, the API keys would change, so I added some code to the view to retrieve the API key from the `localhost:7700/keys` endpoint, but that doesn't seem like it should generally be necessary? (And I wound up in a weird situation where I needed to use `meilisearch:7700` for the API keys, but `localhost:7700` for the search, which also doesn't seem right.) 

On reflection, I think what's happening is that in my Compose file, I'm restarting Meilisearch each time I restart Docker, and re-adding the same master key. But since it's technically spinning up a new Meilisearch instance, even though it's the same key, it generates new search and admin API keys. So I bet what I need to do is add a little script that runs when the Docker container starts that will retrieve the API keys and set them in settings, because retrieving them in the view is _not_ a long-term solution! 
