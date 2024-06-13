# Stop search engines from indexing your site and showing it in search results 

## Links 

- [Block Search Indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) from Google Search Central docs

## Use case 

I have a site that I don't want to appear in search results. Maybe it's a dev site, maybe I want to share it with friends and family but I'm a private person, there are lots of reasons this might be useful. 

## `noindex` 

From the [docs](https://developers.google.com/search/docs/crawling-indexing/block-indexing): 

> noindex is a rule set with either a <meta> tag or HTTP response header and is used to prevent indexing content by search engines that support the noindex rule, such as Google. When Googlebot crawls that page and extracts the tag or header, Google will drop that page entirely from Google Search results, regardless of whether other sites link to it.

Add this to your HTML template:

`<meta name="robots" content="noindex">` 

If you are using Django (or any other templating system), you can add in your `base.html` template, and it will appear on every page that inherits from that template, allowing you to keep the web from indexing all of your pages. 

You can also choose to add this tag only to certain pages, allowing the rest of your site to appear in search results, but hiding those pages you want to keep from search results. 

## How to fix pages that are already indexed 

If you own the site and you need to remove pages from search results, first add the `noindex` as indicated above. Then, follow the instructions in [Refresh Outdated Content tool](https://support.google.com/webmasters/answer/7041154?hl=en). 
