import sqlite3

class ArticleDatabase:
    def __init__(self, name) -> None:
        if name.endswith('.adb') == 0:
            self.fName = name + '.adb'

        self.dbConnection = sqlite3.connect(name)
        db = self.dbConnection.cursor()
        db.execute('CREATE TABLE IF NOT EXISTS magazine (title TEXT, date TEXT)')
    
    def __del__(self) -> None:
        self.close_database()

    def article_not_found(self, articleTitle, articleDate) -> bool:
        """Check if a given pair of article title and date
        Args:
            self (articleDatabase): database
            articleTitle (str): The title of an article
            articleDate (str): The publication date of an article
        Returns:
            bool: True if not found. False if found.
        """

        db = self.dbConnection.cursor()
        db.execute('SELECT * from magazine WHERE title=? AND date=?', (articleTitle, articleDate))
        if not db.fetchall():
            return True
        else:
            return False

    def add_article_to_db(self, articleTitle, articleDate):
        """
        Args:
            articleTitle (str)             : The title of an article
            articleDate  (str)             : The publication date of an article
        Return:
            Nothing
        """

        self.dbConnection.cursor().execute('INSERT INTO magazine VALUES(?, ?)', (articleTitle, articleDate))
        self.dbConnection.commit()

    def close_database(self):
        self.dbConnection.close()