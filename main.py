import sqlite3
import smtplib
from email.mime.text import MIMEText
import feedparser

db_connection = sqlite3.connect('D:\\Projects\\rssPython\\testBase.sqlite')
db = db_connection.cursor()
db.execute('CREATE TABLE IF NOT EXISTS magazine (title TEXT, date TEXT)')

def article_is_not_db(article_title, article_date):
    """ Check if a given pair of article title and date
    Args:
        article_title (str): The title of an article
        article_date (str): The publication date of an article
    Return:
        True if the article is not in db
        False if the article exists in db
    """
    db.execute('SELECT * from magazine WHERE title=? AND date=?', (article_title, article_date))
    if not db.fetchall():
        return True
    else:
        return False

def add_article_to_db(article_title, article_date):
    """
    Args:
        article_title (str): The title of an article
        article_date (str): The publication date of an article
    """
    db.execute('INSERT INTO magazine VALUES(?, ?)', (article_title, article_date))
    db_connection.commit()

def read_article_feed():
    """ Gets articles from RSS feed """
    feed = feedparser.parse('https://fedoramagazine.org/feed/')
    for article in feed['entries']:
        if article_is_not_db(article['title'], article['published']):
            add_article_to_db(article['title'], article['published'])

if __name__ == '__main__':
    print('running')
    read_article_feed()
    db_connection.close()