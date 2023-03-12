from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from routes.routes import routes
from httphandler.badrequesthandler import BadRequestHandler
from httphandler.dbrequesthandler import DBRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        request = urlparse(self.path, allow_fragments=False)
        if request.path in routes:
            handler = DBRequestHandler()
        else:
            handler = BadRequestHandler()

        response = handler.handle(request, requesttype='get')
        self.respond(response)

    def do_POST(self):
        request = urlparse(self.path, allow_fragments=False)
        if request.path in routes:
            handler = DBRequestHandler()
        else:
            handler = BadRequestHandler()

        response = handler.handle(request)
        self.respond(response)
    def do_PATCH(self):
        self.do_GET()


    def respond(self, handler):
        self.send_response(handler.status)
        self.send_header('Content-type', handler.content_type)
        self.end_headers()
        self.wfile.write(bytes(handler.data, encoding='utf-8'))
