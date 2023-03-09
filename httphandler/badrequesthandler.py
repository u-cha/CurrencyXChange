from httphandler.basichandler import BasicHandler
from routes.routes import routes


class BadRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 404
        self.content_type = 'text/html'

    def get_content(self, route):
        self.data = open(f"html/{route[self.status]['htmlpage']}").read()
