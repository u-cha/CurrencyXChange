from httphandler.basichandler import BasicHandler


class DBRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 200
        self.content_type = 'text/html'

    def get_content(self, route):
        self.data = open(f"html/{route['htmlpage']}").read()