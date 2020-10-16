'''
Program to download epub files for english books from Library Genesis.
'''

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from sys import exit
from urllib import request
from colored import fg, bg, attr

DOWNLOAD_PATH = '.'
RESET = attr(0)

class Colors:
    title_fg = fg(15)
    title_bg = bg(4)
    table_head = fg(12)
    table_grid = fg(10)
    download = fg(14)
    success = fg(10)
    error = fg(9)
    white = fg(15)
    
def displayError(err_msg):
    print(f'\n{Colors.error}{err_msg}{RESET}')
    exit()
    
def showTable(data):
    print('\n%s%-4s %-25s %-25s %-25s %-7s %s' % (Colors.table_head, 'Sno', 'Author', 'Title', 'Series', 'Size', RESET))
    print('%s%-4s %-25s %-25s %-25s %-7s%s' % (Colors.table_grid, '-'*4, '-'*25, '-'*25,'-'*25, '-'*7, RESET))
    
    print(Colors.white)
    for book in data:
        for key, value in list(book.items())[1:4]:    
            if type(value) != int and len(value) > 25:
                book[key] = value[:23] + '..'
        print('%(n)-4i %(author)-25s %(title)-25s %(series)-25s %(size)-7s' % book)
    print(RESET)

def downloadBook(download_links, title):    
    ''' Downloads the book from any one mirror '''
    file_name = f'{DOWNLOAD_PATH}/{title}.epub'
    print(f'\n{Colors.download}Downloading {title}... {RESET}')
    for i in range(2):
        try:
            download_link = getURLfromMirror(i, download_links[i])
            request.urlretrieve(download_link, file_name)
            print(f'\n{Colors.success}Successfully Downloaded{RESET}')
            return
        except:
            displayError('There was a problem. Trying again...')
            if i == 1:
                displayError('Sorry, can\'t download the storm of book.')
            continue
    
def getURLfromMirror(mirror_index, download_link):
    ''' Gets the book download link from the mirror '''
    page = requests.get(download_link).text
    soup = BeautifulSoup(page, 'lxml')
    if mirror_index == 0 or mirror_index == 1:
        a = soup.find('a')
        download_link = a['href']
    return download_link
        
if __name__ == '__main__':
    print(Colors.title_bg, ' '*33 ,RESET, sep='')
    print(f'{Colors.title_fg}{Colors.title_bg}   Library Genesis Book Search   {RESET}')
    print(Colors.title_bg, ' '*33 ,RESET, sep='', end='\n\n')
    
    name = input('Enter book to search: ').strip()
    if name == '':
        displayError('No search parameter given.')
    
    name_f = name.replace(' ', '+')
    url = f'http://libgen.rs/fiction/?q={name}&criteria=&language=English&format=epub'
    
    try:
        page = requests.get(url).text
    except ConnectionError:
        displayError('No internet connection.')
    
    soup = BeautifulSoup(page, 'lxml')  
    table = soup.find('table', attrs={'class': 'catalog'})
    
    try:
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
    except AttributeError:
        displayError('No books found.')
    
    data = []
    
    for i in range(len(rows)):
        cols = rows[i].find_all('td')
        author, series, title = [cols[i].text.strip() for i in range(3)]
        links = [a['href'] for a in cols[5].find_all('a')]
        size = cols[4].text.split('/')[1].strip()
        
        book = {
                'n': i,
                'author': author,
                'series': series,
                'title': title,
                'title_full': title,
                'links': links,
                'size': size
            }
        data.append(book)
    
    showTable(data)
    
    try:
        selection = int(input('\nEnter selection: '))
    except ValueError:
        displayError('Invalid Selection')
        
    for book in data:
        if book['n'] == selection:
            download_links = book['links']
            title = book['title_full']
            downloadBook(download_links, title)
            break
    else:
        displayError('Invalid Selection')