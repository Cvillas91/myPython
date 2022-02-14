from urllib.request import urlopen
from bs4 import BeautifulSoup 

url = "https://webscraper.io/test-sites/tables"

html_code = urlopen(url).read().decode("UTF-8")

soup = BeautifulSoup(html_code, 'lxml')

'''
headings_2 = soup.findAll('h2')
#print(headings_2)

images = soup.findAll('img')
print(images[1]['src'])
print(images[1]['alt'])
'''

first_table = soup.find('table')
rows = first_table.findAll('tr')[1:]
last_names = []

for row in rows :
    last_names.append(row.findAll('td')[2].get_text())

print(last_names)
