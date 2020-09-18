from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from sys import exit

'''
Format:
http://libgen.rs/fiction/?q={string separated by +}&criteria=&language=English&format=epub

Eg: http://libgen.rs/fiction/?q=dune+1&criteria=&language=English&format=epub

'''

def showTable(data):
    print('%-4s %-25s %-25s %-25s %-7s' % ('Sno', 'Author', 'Series', 'Title', 'Size'))
    print('%-4s %-25s %-25s %-25s %-7s' % ('-'*4, '-'*25, '-'*25,'-'*25, '-'*7))
    
    for book in data:
        for key, value in list(book.items())[1:4]:    
            if type(value) != int and len(value) > 25:
                book[key] = value[:23] + '..'
        print('%(n)-4i %(author)-25s %(series)-25s %(title)-25s %(size)-7s' % book)


name = input('Enter book to search: ')
name_f = name.replace(' ', '+')
url = f'http://libgen.rs/fiction/?q={name}&criteria=&language=English&format=epub'

try:
    page = requests.get(url).text
except ConnectionError:
    print('No internet connection')
    exit()

soup = BeautifulSoup(page, 'lxml')  
table = soup.find('table', attrs={'class': 'catalog'})
tbody = table.find('tbody')
rows = tbody.find_all('tr')

data = []

for i in range(len(rows)):
    cols = rows[i].find_all('td')
    author, series, title = [cols[i].text.strip() for i in range(3)]
    link = cols[5].find('a')['href']
    size = cols[4].text.split('/')[1].strip()

    book = {
            'n': i,
            'author': author,
            'series': series,
            'title': title,
            'link': link,
            'size': size
        }
    data.append(book)

showTable(data)

selection = input('Enter selection: ')

for book in data:
    if book['n'] == selection:
        details_page = book['link']
        
try:
    page = requests.get(details_page).text
except NameError:
    print('No selection made.')
    exit()
    
soup = BeautifulSoup(page, 'lxml')
h2 = soup.find('h2')
download_url = h2.find('a')['href']

print('Downloading...',)

file_online = requests.get(download_url).content
file_name =  name.capitalize() + '.epub'
open(file_name, 'wb').write(file_online)

print('\nSuccessfully Downloaded')