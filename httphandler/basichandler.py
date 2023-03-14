import json
from urllib.parse import parse_qs


class BasicHandler:
    __statuses = (200, 400, 404, 405, 406, 409, 500)

    def __init__(self):
        self.__status = 200
        self.__data = None
        self.__content_type = 'text/plain'
        self.__methods = {}
        self.__request = None
        self.__query = None
        self.__got_json = False
        self.__db_address = None

    def handle(self, request, db_address):
        self.request = request
        self.query = parse_qs(request.query)
        self.db_address = db_address
        method = self.methods.get(request.path, None)
        getattr(self, method)(self.query)
        self.__format_output()
        return self

    def __format_output(self):
        if self.__got_json:
            self.data = json.dumps(self.data, indent=4)

    @property
    def got_json(self):
        return self.__got_json

    @property
    def methods(self):
        return self.__methods

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, request):
        self.__request = request

    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query):
        self.__query = query

    @classmethod
    def check_status(cls, status):
        if status in cls.__statuses:
            return True
        return False

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if self.check_status(status):
            self.__status = status
        else:
            self.__status = 404

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, content):
        self.__data = content

    @property
    def content_type(self):
        return self.__content_type

    @content_type.setter
    def content_type(self, content_type):
        self.__content_type = content_type

    @property
    def db_address(self):
        return self.__db_address

    @db_address.setter
    def db_address(self, db_address):
        self.__db_address = db_address

