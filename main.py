from argparse import ArgumentParser
import logging
import feedparser

from articledatabase import articleDatabase as articleDB

def create_argparse() -> ArgumentParser:
    """Generates argument parser

    Returns:
        ArgumentParser: Object to parse command line arguments
    """

    arguementParser = ArgumentParser(description='Reads RSS feeds and stores articles to sql format database with file extension ".adb"')
    arguementParser.add_argument('input_type', choices=['FILE', 'URL'],
        help=''
    )
    arguementParser.add_argument("input", help='')
    arguementParser.add_argument('-o', '--output',
        metavar='PATH', default='./articles.adb',
        help='Location and name of output file. Default: ./articles.adb'
    )
    arguementParser.add_argument('-v', '--verbose', action='store_true',
        help='Verbose logging mode'
    )
    return arguementParser

def verbose_mode(verbose):
    logger = logging.getLogger('Feed status')

    if verbose:
        logger.setLevel(level='DEBUG')
    else:
        logger.setLevel(level='INFO')
    lHandler = logging.StreamHandler()

    formatter = logging.Formatter(

    )
    lHandler.setFormatter(formatter)
    logger.addHandler(lHandler)
    return logger

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
    argParser = create_argparse()
    args = argParser.parse_args()
    logger = verbose_mode(args.verbose)
    articles = articleDB(args.output)