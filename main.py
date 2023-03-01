
from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import csv


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes('<html><body><h1>Hello, Mr.Peterson!</h1></body></html>', 'utf-8'))


server = HTTPServer(('127.0.0.1', 8080), Handler)

db_connection = sqlite3.connect('local.db')
db_cursor = db_connection.cursor()
db_cursor.execute('''DROP TABLE Currencies''')
db_cursor.execute('''CREATE TABLE Currencies (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
Code VARCHAR(5) NOT NULL, FullName VARCHAR(50) NOT NULL, Sign VARCHAR(5) NOT NULL)''')
db_cursor.execute('''CREATE UNIQUE INDEX CurrencyCode ON Currencies(Code)''')
with open('currencies.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, delimiter=';')
    content = []
    for row in reader:
        content.append(row)


    for row in content[1:]:
        rowtuple = (row[1], row[0], row[2])
        db_cursor.execute('INSERT INTO Currencies (Code, FullName, Sign)'
                          'VALUES (?,?,?)', rowtuple)
        db_connection.commit()
db_connection.close()






# if __name__ == '__main__':
    # server.serve_forever()
