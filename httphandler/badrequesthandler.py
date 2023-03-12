from httphandler.basichandler import BasicHandler


class BadRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 404
        self.content_type = 'text/html'

    def handle(self, request, *args, **kwargs):
        self.data = f'{request.path} not found or not callable.'
        return self

