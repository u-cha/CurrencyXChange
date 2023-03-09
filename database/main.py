import sqlite3
import csv

db_connection = sqlite3.connect('database/local.db')
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

db_cursor.execute('''DROP TABLE ExchangeRates''')
db_cursor.execute('''CREATE TABLE ExchangeRates (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
BaseCurrencyId INTEGER NOT NULL, TargetCurrencyId INTEGER NOT NULL,  Rate DECIMAL(6), 
FOREIGN KEY (BaseCurrencyId) REFERENCES Currencies(ID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (TargetCurrencyId) REFERENCES Currencies(ID) ON DELETE CASCADE ON UPDATE CASCADE)''')
db_cursor.execute('''CREATE UNIQUE INDEX CurrencyPair ON ExchangeRates(BaseCurrencyId, TargetCurrencyId)''')

db_connection.close()
