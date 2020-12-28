import feedparser

from article_database import articleDatabase as articleDB

def read_article_feed(url, articles):
    """Reads article feed from single url

    Args:
        url (str): website url
        articles (str)
    """

    feed = feedparser.parse(url)
    for article in feed['entries']:
        if articles.article_not_found(article['title'], article['published']):
            articles.add_article_to_db(article['title'], article['published'])

if __name__ == '__main__':
    print('running')

    articles = articleDB('output')

    read_article_feed("", articles)
    articles.close_database()