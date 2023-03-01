import requests
import bs4
import csv

url = 'https://www.no1currency.com/currencies/world-currency-symbols/'
response = requests.get(url)
try:
    response.status_code == 200
except Exception:
    print(f'Failed to reach {url}')

soup = bs4.BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
rows = table.find_all('tr')
clean_table = []
for row in rows:
    row.find_all('td')
    clean_table.append([tag.text for tag in row])

with open('currencies.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(clean_table)