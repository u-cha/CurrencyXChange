import sqlite3
from httphandler.basichandler import BasicHandler
import json


class DBRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 200
        self.content_type = 'application/json'

    def get_content(self, query, params=None):
        with sqlite3.connect('database/local.db') as db_connection:
            db_cursor = db_connection.cursor()
            if params:
                content = db_cursor.execute(query, params)
            else:
                content = db_cursor.execute(query)
        return content

    def get_currencies(self):
        query = 'SELECT * FROM Currencies'
        response = self.get_content(query)

        currencies = response.fetchall()
        colnames = [col[0] for col in response.description]


        result = []
        for currency in currencies:
            element = dict(zip(colnames, currency))
            result.append(element)

        self.data = json.dumps(result, indent=4)


    def get_currency(self, currency):
        query = 'SELECT * FROM Currencies WHERE Code=?'
        params = (currency,)
        response = self.get_content(query, params)
        value = response.fetchone()

        if value:
            colnames = [col[0] for col in response.description]
            output = dict(zip(colnames, value))
            self.data = json.dumps(output, indent=4)
        else:
            self.data = f'Валюта {currency} не найдена в базе данных.'



