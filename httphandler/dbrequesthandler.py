import sqlite3
from httphandler.basichandler import BasicHandler


class DBRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 200
        self.content_type = 'text/html'

    def get_content(self, route):
        self.data = open(f"html/{route['htmlpage']}").read()

    def get_currencies(self):
        db_connection = sqlite3.connect('database/local.db')
        db_cursor = db_connection.cursor()
        currencies = db_cursor.execute('SELECT * FROM Currencies').fetchall()
        db_connection.close()
        self.data = currencies


    def get_currency(self, currency):
        db_connection = sqlite3.connect('database/local.db')
        db_cursor = db_connection.cursor()
        currency = db_cursor.execute('SELECT * FROM Currencies WHERE Code=?', currency).fetchone()
        db_connection.close()
        self.data = currency


