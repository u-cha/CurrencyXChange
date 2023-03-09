from http.server import HTTPServer

from server import Server

server = HTTPServer(('127.0.0.1', 8080), Server)

if __name__ == '__main__':
    server.serve_forever()
