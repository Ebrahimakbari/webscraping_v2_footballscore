import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
r = requests.get('https://www.skysports.com/womens-championship-table', headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find('table')
rows = table.select('tr')
main_data = []
for row in rows:
    data = []
    for head in row.select('th'):
        data.append(head.text.replace('\n', ''))
        temp = data
    for body in row.select('td'):
        data.append(body.text.replace('\n', ''))
        temp = data
    main_data.append(temp[0:-1])
# print(main_data)
with open('data.txt', 'w') as reader:
    for item in main_data:
        reader.write(f"{item}\n")