from http.server import BaseHTTPRequestHandler
from routes.routes import routes

from httphandler.badrequesthandler import BadRequestHandler
from httphandler.dbrequesthandler import DBRequestHandler


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in routes:
            route = self.path
            handler = DBRequestHandler()
            getattr(handler, routes[route]['method'])()
            handler.cook_html(route)
            self.respond(handler)

        elif self.path.count('/') > 1 and self.path[:self.path[1:].find('/') + 2] in routes:
            route = self.path[:self.path[1:].find('/') + 2]
            extension = self.path[self.path[1:].find('/') + 2:]
            handler = DBRequestHandler()
            getattr(handler, routes[route]['method'])(extension)

            handler.cook_html(self.path)
            self.respond(handler)

        else:
            handler = BadRequestHandler()
            handler.cook_html('404')
            self.respond(handler)

    def do_POST(self):
        self.do_GET()

    def do_PATCH(self):
        self.do_GET()


    def respond(self, handler):
        self.send_response(handler.status)
        self.send_header('Content-type', handler.content_type)
        self.end_headers()
        self.wfile.write(bytes(handler.data, encoding='utf-8'))
