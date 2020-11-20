'''
Program to download fiction books from Library Genesis.
'''

from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from sys import exit, stdout
from urllib import request
from tabulate import tabulate

DOWNLOAD_PATH = '.'
RESET = '\x1b[0m'
MAX_CHARS = 25 # max char length to show in the table before cutting it off

def getSearchResults(page_number):
    ''' Check if the url exists and retrieves the content table from the page '''
    name_f = name.replace(' ', '+')
    url = f'http://libgen.rs/fiction/?q={name}&criteria=&language=English&format=epub&page={page_number}'
    
    try:
        page = requests.get(url).text
    except ConnectionError:
        displayError('No internet connection.')
        exit()

    soup = BeautifulSoup(page, 'lxml')  
    table = soup.find('table', attrs={'class': 'catalog'})
    
    try:
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
    except AttributeError:
        return False
        displayError('No books found.')

    return rows

def getBooks(table):
    ''' Show the search results and save the mirrors in arrays '''
    titles, mirrors, records = [], [], []
    headers = ['#', 'Author', 'Title', 'Series', 'Size']

    fit = lambda txt: txt[:MAX_CHARS-2]+'..' if len(txt) > MAX_CHARS else txt

    for i in range(len(table)):
        cols = table[i].find_all('td')
        author = cols[0].text.strip().split(';')[0].split(',')
        author.reverse()
        author = ' '.join(author).strip()
        series, title = [cols[i].text.strip() for i in range(1, 3)]
        links = [a['href'] for a in cols[5].find_all('a')]
        size = cols[4].text.split('/')[1].strip()

        mirrors.append(links)
        titles.append(title)

        series = fit(series)
        title = fit(title)
        author = fit(author)

        records.append([i+1, author, title, series, size])

    print(tabulate(records, headers))

    return (titles, mirrors)
    
def displayError(err_msg):
    ''' Display formatted error message '''
    print(f'\n\x1b[38;5;9m{err_msg}{RESET}')
    
def downloadBook(download_links, title):    
    ''' Downloads the book from any one mirror '''
    file_name = f'{DOWNLOAD_PATH}/{title}.epub'
    print(f'\n{Colors.download}Downloading {title}...{RESET}')
    for i in range(2):
        try:
            download_link = getURLfromMirror(i, download_links[i])

            with open(file_name, "wb") as f:
                response = requests.get(download_link, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None: # no content length header
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(25 * dl / total_length)
                        stdout.write("\r %s [%s%s]" % (str(done*4) + '%', '#' * done, ' ' * (25-done)))    
                        stdout.flush()

            print(f'\n{Colors.success}Successfully Downloaded{RESET}')
            return True
        except:
            displayError('There was a problem. Trying again...')
            if i == 1:
                displayError('Sorry, can\'t download the book.')
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
    print('\x1b[48;5;4m', ' '*33 ,RESET, sep='')
    print(f'\x1b[38;5;15m\x1b[48;5;4m   Library Genesis Book Search   {RESET}')
    print('\x1b[48;5;4m', ' '*33 ,RESET, sep='', end='\n\n')
    
    name = input('Enter book to search: ').strip()
    if name == '':
        displayError('No search parameter given.')
        exit()
        
    page_number = 1
    get_next_page = True

    while get_next_page:
        table = getSearchResults(page_number)
        
        if table: # if table exists
            print(f'\n\nPage #{page_number}\n')
            book_titles, book_mirrors = getBooks(table)

        else:
            if page_number == 1:
                print('No results available')
                break
            else:
                print('No more results available')
            selection = input('\nType # of page or press any other key to quit.')
            if selection.isnumeric():
                page_number = int(selection)
            else:
                get_next_page = False
            continue
        
        selection = input('\nType # of book to download, q to quit or just press Enter to see more matches: ')

        if selection.isnumeric():
            i = int(selection) - 1
            if -1 < i < 24:
                downloadBook(book_mirrors[i], book_titles[i])
            else:
                displayError('Invalid Selection')
            break

        elif selection.lower() == 'q':
            exit()
        
        else:
            page_number += 1