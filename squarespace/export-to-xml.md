# Export Your Squarespace Site to XML

## Links

- [Squarespace: Exporting your site](https://support.squarespace.com/hc/en-us/articles/206566687-Exporting-your-site)
- Your Squarespace import-export panel: `https://<your-site>.squarespace.com/config/settings/website/import-export`

## How to export your Squarespace site to XML

Note:

- You can only export one "blog" type at a time
- It doesn't allow you to export in a format other than Wordpress, but Squarespace's docs say you don't have to import it into Wordpress. Whatever that means. I guess we'll see.


1. In the **Import & Export Content** page of your website settings, select **Export**
2. Select **Wordpress** (which as of April was your only option)
3. Confirm. You will now see your download processing.
4. When your download is ready, select **Download**
5. Select your save location. What saves will be an XML file.

## Sample output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:wfw="http://wellformedweb.org/CommentAPI/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:wp="http://wordpress.org/export/1.2/">
  <channel>
    <title>Lacey Henschel</title>
    <link>https://www.mywebsite.com</link>
    <pubDate>Mon, 06 Feb 2017 03:46:14 +0000</pubDate>
    <description />
    <language>en-US</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:author>
      <wp:author_id>966804475</wp:author_id>
      <wp:author_login>redacted@redacted.com</wp:author_login>
      <wp:author_email>redacted@redacted.com</wp:author_email>
      <wp:author_display_name><![CDATA[Lacey Henschel]]></wp:author_display_name>
      <wp:author_first_name><![CDATA[Lacey]]></wp:author_first_name>
      <wp:author_last_name><![CDATA[Henschel]]></wp:author_last_name>
    </wp:author>
    <wp:category>
      <wp:cat_name><![CDATA[Personal - null]]></wp:cat_name>
      <wp:category_nicename>Personal-null</wp:category_nicename>
      <wp:category_parent />
    </wp:category>
    <item>
      <link>/about</link>
      <title>About Lacey</title>
      <pubDate>Tue, 13 Nov 2018 16:57:45 +0000</pubDate>
      <content:encoded><![CDATA[<div class="sqs-html-content">
         <h1 style="white-space: pre-wrap;">Hi there! I’m Lacey.</h1><p style="white-space: pre-wrap;">Here is more data about me.</p>
         </div>
      </content:encoded>

        <item>
            <title>A blog post title </title>
            <link>/path/to/post</link>
            <content:encoded><![CDATA[<div class="sqs-html-content">
                <p class="" style="white-space:pre-wrap;">Here is some blog content! </p>
            </div>]]></content:encoded>
            <excerpt:encoded />
            <wp:post_name>path/to/post</wp:post_name>
            <wp:post_type>post</wp:post_type>
            <wp:post_id>3</wp:post_id>
            <wp:status>publish</wp:status>
            <pubDate>Fri, 13 Jan 2023 19:16:18 +0000</pubDate>
            <wp:post_date>2023-01-13 19:16:18</wp:post_date>
            <wp:post_date_gmt>2023-01-13 19:16:18</wp:post_date_gmt>
            <category domain="post_tag" nicename="tag-1"><![CDATA[weeknotes]]></category>
            <category domain="post_tag" nicename="tag-2"><![CDATA[art]]></category>
            <dc:creator>redacted@redacted.com</dc:creator>
            <wp:comment_status>closed</wp:comment_status>
        </item>
    </channell>
</rss>
```

This is a heavily redacted and thinned version of what exported for me, and I don't have that many blog posts for how old my blog is --  I'm a very inconsistent blogger.

## Goals

I think I finally want to move my blog off Squarespace and into mkdocs or Wagtail or something else. Not sure. At the very least, I want to convert what is there to a more useful format and have it stored somewhere I can attach version control to it.

Now I have this XML copy of my site and we're going to figure out what to do next with it.
