from http.server import HTTPServer
from server import Server

Server.db_address = 'database/local.db'
server = HTTPServer(('127.0.0.1', 8080), Server)

if __name__ == '__main__':
    server.serve_forever()
