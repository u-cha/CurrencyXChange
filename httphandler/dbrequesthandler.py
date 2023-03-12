import sqlite3
import json
from urllib.parse import parse_qs

from httphandler.basichandler import BasicHandler
from routes.routes import routes


class DBRequestHandler(BasicHandler):

    def __init__(self):
        super().__init__()
        self.status = 200

    def handle(self, request, requesttype):
        method = routes[request.path]['method'][requesttype]
        query = parse_qs(request.query)
        getattr(self, method)(query)
        self.__format_output(query)
        return self

    def __format_output(self, query):
        if ('format' in query and query['format'][0].lower() == 'html'
                or self.status != 200):
            self.content_type = 'text/html'
        else:
            self.content_type = 'application/json'
            self.data = json.dumps(self.data, indent=4)

    def query_database(self, db_query, params=None):
        try:
            with sqlite3.connect('database/local.db') as db_connection:
                db_cursor = db_connection.cursor()
                if params:
                    content = db_cursor.execute(db_query, params)
                else:
                    content = db_cursor.execute(db_query)
        except Exception:
            return None
        return content

    def get_currencies(self, *args):
        db_query = 'SELECT * FROM Currencies'
        response = self.query_database(db_query)
        if not self.__check_db_response(response): return self

        currencies = response.fetchall()
        colnames = [col[0] for col in response.description]
        result = []
        for currency in currencies:
            element = dict(zip(colnames, currency))
            result.append(element)
        self.data = result
        return self

    def __check_db_response(self, response):
        if not response:
            self.status = 500
            self.content_type = 'text/html'
            self.data = 'Some problem occurred when trying to reach database.'
            return None
        return True

    def get_currency(self, query):
        if not self.__check_get_currency_query(query): return self
        if not self.__check_currency_code(query['currency'][0]): return self

        currency = query['currency'][0].upper()
        db_query = 'SELECT * FROM Currencies WHERE Code=?'
        params = (currency,)
        response = self.query_database(db_query, params)
        if not self.__check_db_response(response): return self

        value = response.fetchone()
        if not value:
            self.status = 404
            self.data = f'Валюта {currency} не найдена в базе данных.'
            return self

        colnames = [col[0] for col in response.description]
        output = dict(zip(colnames, value))
        self.data = output
        return self

    def __check_currency_code(self, curcode):
        if (
                type(curcode) != str or
                len(curcode) != 3 or
                not curcode.isalpha()
        ):
            print(curcode)
            self.status = 400
            self.data = '''Incorrect currency. Expected 3 latin letters, like "ABC" or "abc".'''
            return None

        return True

    def __check_get_currency_query(self, query):
        if 'currency' not in query:
            self.status = 400
            self.data = 'Missing currency parameter. Syntax is /currency?currency=ABC'
            return None
        if len(query['currency']) > 1:
            self.status = 400
            self.data = 'Incorrect currency input. Syntax is ?currency=ABC. Method takes only one currency.'
            return None

        return True

    def get_currency_by_id(self, cur_id):
        db_query = 'SELECT * FROM Currencies WHERE ID=?'
        params = (cur_id,)
        response = self.query_database(db_query, params)
        if not self.__check_db_response(response): return self

        value = response.fetchone()
        if not value:
            self.status = 404
            self.data = f'Валюта с ID {cur_id} не найдена в базе данных.'
            return self

        colnames = [col[0] for col in response.description]
        output = dict(zip(colnames, value))
        self.data = output

        return self

    def post_currency(self, query):
        if (
                'name' not in query
                or 'code' not in query
                or 'sign' not in query
        ):
            self.status = 400
            self.content_type = 'text/html'
            self.data = 'Missing parameter(s). Syntax is ?name=<name>&code=ABC&sign=<sign>'
            return self
        elif not query['name'][0].isalpha():
            self.status = 400
            self.content_type = 'text/html'
            self.data = '"name" parameter can contain only letters'
            return self
        elif not query['code'][0].isalpha() or len(query['code'][0]) != 3:
            self.status = 400
            self.content_type = 'text/html'
            self.data = '"code" parameter can contain only letters and have 3-letters length.'
            return self
        else:
            response = self.get_currency({'currency': (query['code'][0].upper(),)})
            if response.data == f'Валюта {query["code"][0].upper()} не найдена в базе данных.':
                db_query = '''INSERT INTO Currencies ("Code", "FullName", "Sign") 
    VALUES (?, ?, ?)'''
                params = (query['code'][0].upper(), query['name'][0].capitalize(), query['sign'][0])
                self.query_database(db_query, params)
                response = self.get_currency({'currency': (query['code'][0].upper(),)})
                return response
            else:
                self.status = 409
                self.content_type = 'text/html'
                self.data = 'This currency code already exists in database.'
                return self

    def get_exchange_rates(self, *args):
        db_query = 'SELECT * FROM ExchangeRates'
        response = self.query_database(db_query)
        if not self.__check_db_response(response): return self

        exchangerates = response.fetchall()
        result = []
        for exchangerate in exchangerates:
            element = {
                'ID': exchangerate[0],
                'BaseCurrency': self.get_currency_by_id(exchangerate[1]).data,
                'TargetCurrency': self.get_currency_by_id(exchangerate[2]).data,
                'Rate': exchangerate[3]
            }
            result.append(element)
        self.data = result
        return self
