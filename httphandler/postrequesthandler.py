import sqlite3
import json
from urllib.parse import parse_qs

from httphandler.basichandler import BasicHandler
from routes import routes


class PostRequestHandler(BasicHandler):

    def __init__(self):
        super().__init__()
        self.status = 200
