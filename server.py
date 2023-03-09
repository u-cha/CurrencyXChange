from http.server import BaseHTTPRequestHandler
from routes.routes import routes

from httphandler.badrequesthandler import BadRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in routes:
            handler = BadRequestHandler()
            handler.get_content(routes)
            self.respond(handler)



    def do_POST(self):
        self.respond()

    def do_PATCH(self):
        self.respond()

    def handle_query(self):
        pass

    def respond(self, handler):
        self.send_response(handler.status)
        self.send_header('Content-type', handler.content_type)
        self.end_headers()
        self.wfile.write(bytes(handler.data, 'utf-8'))
