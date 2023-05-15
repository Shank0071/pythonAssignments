import feedparser

rss_urls = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    "https://techcrunch.com/feed/",
    "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "https://www.espn.com/espn/rss/news"
]

for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)

    if feed.bozo:
        print("Error parsing RSS feed:", feed.bozo_exception)
    else:
        print("Feed Title:", feed.feed.title)

        for post in feed.entries[:6]:
            print("Title:", post.title)

        print() 
