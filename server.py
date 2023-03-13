from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from routes.routes import routes
from httphandler.badrequesthandler import BadRequestHandler
from httphandler.dbrequesthandler import DBRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        handler, request = self.__choose_handler()
        response = handler.handle(request, requesttype='get')
        self.respond(response)

    def do_POST(self):
        handler, request = self.__choose_handler()
        response = handler.handle(request, requesttype='post')
        self.respond(response)
    def do_PATCH(self):
        handler, request = self.__choose_handler()
        response = handler.handle(request, requesttype='patch')
        self.respond(response)

    def __choose_handler(self):
        request = urlparse(self.path, allow_fragments=False)
        if request.path in routes:
            handler = DBRequestHandler()
        else:
            handler = BadRequestHandler()
        return handler, request

    def respond(self, handler):
        self.send_response(handler.status)
        self.send_header('Content-type', handler.content_type)
        self.end_headers()
        self.wfile.write(bytes(handler.data, encoding='utf-8'))
