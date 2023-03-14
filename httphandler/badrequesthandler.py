from httphandler.basichandler import BasicHandler


class BadRequestHandler(BasicHandler):
    def __init__(self):
        super().__init__()
        self.status = 404

    def handle(self, request):
        self.data = f'Oops! {request.path} is not served.'
        return self

