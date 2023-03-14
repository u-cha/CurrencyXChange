from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from routes import routes
import httphandler


class Server(BaseHTTPRequestHandler):
    __db_address = None

    def __parse_request(self):
        parsed_request = urlparse(self.path, allow_fragments=False)
        return parsed_request

    def __check_request(self):
        request = self.__parse_request()
        if request.path not in routes:
            return None
        return request

    def do_GET(self):
        request = self.__check_request()
        if request:
            handler = httphandler.GetRequestHandler()
        else:
            handler = httphandler.BadRequestHandler()
        response = handler.handle(request, Server.db_address)
        self.respond(response)

    def do_POST(self):
        request = self.__check_request()
        if request:
            handler = httphandler.PostRequestHandler()
        else:
            handler = httphandler.BadRequestHandler()
        response = handler.handle(request, Server.db_address)
        self.respond(response)

    def do_PATCH(self):
        request = self.__check_request()
        if request:
            handler = httphandler.PatchRequestHandler()
        else:
            handler = httphandler.BadRequestHandler()
        response = handler.handle(request, Server.db_address)
        self.respond(response)

    def respond(self, handler):
        self.send_response(handler.status)
        self.send_header('Content-type', handler.content_type)
        self.end_headers()
        self.wfile.write(bytes(handler.data, encoding='utf-8'))

    @property
    def db_address(self):
        return self.__db_address

    @db_address.setter
    def db_address(self, db_address: str):
        self.__db_address = db_address
