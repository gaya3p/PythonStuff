from bs4 import BeautifulSoup
import requests

'''
Format:
http://libgen.rs/fiction/?q={string separated by +}&criteria=&language=English&format=epub

Eg: http://libgen.rs/fiction/?q=dune+1&criteria=&language=English&format=epub


'''
name = input('Enter book to search: ')
name_f = name.replace(' ', '+')
url = f'http://libgen.rs/fiction/?q={name}&criteria=&language=English&format=epub'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')  

data = []
#data = [{'author': 'Dune, Kyra', 'series': 'Dual Realm 1-2', 'title': 'Bonded', 'link': 'http://library.lol/fiction/06C48B85A10BE047BC473D9CF4E85953'}, {'author': 'Herbert, Brian', 'series': 'Dune Legends 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/4D4977ADE79D2A7FA28303FE04A22646'}, {'author': 'Herbert, Brian', 'series': 'Legends of Dune 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/19F40FE8C45B0E63C606AF91603A9264'}, {'author': 'Herbert, Frank', 'series': 'Orignal 3; Dune 1', 'title': 'Children of Dune', 'link': 'http://library.lol/fiction/14389E62EF009743980B5B57C114ED1C'}, {'author': 'Bell, Cindy', 'series': 'Dune House 1,5', 'title': 'Dodgy Dealings', 'link': 'http://library.lol/fiction/57B8048714F9A431E84EA827F7A0894A'}, {'author': 'Dune, Kyra', 'series': 'Dragon Within 1', 'title': 'Dragon Within', 'link': 'http://library.lol/fiction/D15FC6A0486EB85FE15E2A1F4B913555'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune [ed.: 40th anniversary edition]', 'link': 'http://library.lol/fiction/C9EF93A39D2B4BCF99D855574BE2B5D7'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/1CE75A3198E73E38AF5BEDF386010E01'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/338629C11EFF27BDA614130F3D066563'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8D1B31E9502A3DBD992EDA5167CEE272'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/A78E6E165DAF668CF91C6D008E631373'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/916C0C3AE6C39BBFA693F37E720B31AD'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/545F009A483C5DEDE12410EE8017298D'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/9E9CC981477E1DCE9935F9B0549DE4C7'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/71A95433505BB22591AF13F47679A19A'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8BD9390F140A2DEA0FA522E72F2F0D71'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/07C3B66FF181FC78D11E06BB629A79BF'}, {'author': 'Herbert, Frank Patrick', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C01C35708C29B3AF51FAA072E20A8519'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/D644669BD0F55C5F1E8CD32F978957E2'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/3FEC255E9922F6CC259A76AE57E15290'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/FD4AEAA172214BC87E97EE1763560A82'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/76C9353813DDEFEB9F42BBBD9EE1440C'}, {'author': 'Herbert, Frank', 'series': 'Dune Book 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/DA6742DA77EF6BBDD772FB7EAF5FE259'}, {'author': 'Herbert, Frank', 'series': 'Dune Chronicles 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C4D2F8619D70403D0DC3FF8851C0E9FD'}, {'author': 'Herbert, Frank Patrick', 'series': 'Dune Saga 7; Classic Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/81E8B6E153C824892BED50F7ADF97DC5'}]

table = soup.find('table', attrs={'class': 'catalog'})
tbody = table.find('tbody')

rows = tbody.find_all('tr')

for i in range(len(rows)):
    cols = rows[i].find_all('td')
    author, series, title = [cols[i].text.strip() for i in range(3)]
    link = cols[5].find('a')['href']
    
    book = {
            'n': i,
            'author': author,
            'series': series,
            'title': title,
            'link': link
        }
    data.append(book)


#data = [{'author': 'Dune, Kyra', 'series': 'Dual Realm 1-2', 'title': 'Bonded', 'link': 'http://library.lol/fiction/06C48B85A10BE047BC473D9CF4E85953'}, {'author': 'Herbert, Brian', 'series': 'Dune Legends 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/4D4977ADE79D2A7FA28303FE04A22646'}, {'author': 'Herbert, Brian', 'series': 'Legends of Dune 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/19F40FE8C45B0E63C606AF91603A9264'}, {'author': 'Herbert, Frank', 'series': 'Orignal 3; Dune 1', 'title': 'Children of Dune', 'link': 'http://library.lol/fiction/14389E62EF009743980B5B57C114ED1C'}, {'author': 'Bell, Cindy', 'series': 'Dune House 1,5', 'title': 'Dodgy Dealings', 'link': 'http://library.lol/fiction/57B8048714F9A431E84EA827F7A0894A'}, {'author': 'Dune, Kyra', 'series': 'Dragon Within 1', 'title': 'Dragon Within', 'link': 'http://library.lol/fiction/D15FC6A0486EB85FE15E2A1F4B913555'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune [ed.: 40th anniversary edition]', 'link': 'http://library.lol/fiction/C9EF93A39D2B4BCF99D855574BE2B5D7'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/1CE75A3198E73E38AF5BEDF386010E01'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/338629C11EFF27BDA614130F3D066563'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8D1B31E9502A3DBD992EDA5167CEE272'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/A78E6E165DAF668CF91C6D008E631373'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/916C0C3AE6C39BBFA693F37E720B31AD'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/545F009A483C5DEDE12410EE8017298D'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/9E9CC981477E1DCE9935F9B0549DE4C7'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/71A95433505BB22591AF13F47679A19A'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8BD9390F140A2DEA0FA522E72F2F0D71'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/07C3B66FF181FC78D11E06BB629A79BF'}, {'author': 'Herbert, Frank Patrick', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C01C35708C29B3AF51FAA072E20A8519'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/D644669BD0F55C5F1E8CD32F978957E2'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/3FEC255E9922F6CC259A76AE57E15290'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/FD4AEAA172214BC87E97EE1763560A82'}, {'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/76C9353813DDEFEB9F42BBBD9EE1440C'}, {'author': 'Herbert, Frank', 'series': 'Dune Book 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/DA6742DA77EF6BBDD772FB7EAF5FE259'}, {'author': 'Herbert, Frank', 'series': 'Dune Chronicles 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C4D2F8619D70403D0DC3FF8851C0E9FD'}, {'author': 'Herbert, Frank Patrick', 'series': 'Dune Saga 7; Classic Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/81E8B6E153C824892BED50F7ADF97DC5'}, {'id': 0, 'author': 'Dune, Kyra', 'series': 'Dual Realm 1-2', 'title': 'Bonded', 'link': 'http://library.lol/fiction/06C48B85A10BE047BC473D9CF4E85953'}, {'id': 1, 'author': 'Herbert, Brian', 'series': 'Dune Legends 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/4D4977ADE79D2A7FA28303FE04A22646'}, {'id': 2, 'author': 'Herbert, Brian', 'series': 'Legends of Dune 1', 'title': 'Butlerian Jihad', 'link': 'http://library.lol/fiction/19F40FE8C45B0E63C606AF91603A9264'}, {'id': 3, 'author': 'Herbert, Frank', 'series': 'Orignal 3; Dune 1', 'title': 'Children of Dune', 'link': 'http://library.lol/fiction/14389E62EF009743980B5B57C114ED1C'}, {'id': 4, 'author': 'Bell, Cindy', 'series': 'Dune House 1,5', 'title': 'Dodgy Dealings', 'link': 'http://library.lol/fiction/57B8048714F9A431E84EA827F7A0894A'}, {'id': 5, 'author': 'Dune, Kyra', 'series': 'Dragon Within 1', 'title': 'Dragon Within', 'link': 'http://library.lol/fiction/D15FC6A0486EB85FE15E2A1F4B913555'}, {'id': 6, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune [ed.: 40th anniversary edition]', 'link': 'http://library.lol/fiction/C9EF93A39D2B4BCF99D855574BE2B5D7'}, {'id': 7, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/1CE75A3198E73E38AF5BEDF386010E01'}, {'id': 8, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/338629C11EFF27BDA614130F3D066563'}, {'id': 9, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8D1B31E9502A3DBD992EDA5167CEE272'}, {'id': 10, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/A78E6E165DAF668CF91C6D008E631373'}, {'id': 11, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/916C0C3AE6C39BBFA693F37E720B31AD'}, {'id': 12, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/545F009A483C5DEDE12410EE8017298D'}, {'id': 13, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/9E9CC981477E1DCE9935F9B0549DE4C7'}, {'id': 14, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/71A95433505BB22591AF13F47679A19A'}, {'id': 15, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/8BD9390F140A2DEA0FA522E72F2F0D71'}, {'id': 16, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/07C3B66FF181FC78D11E06BB629A79BF'}, {'id': 17, 'author': 'Herbert, Frank Patrick', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C01C35708C29B3AF51FAA072E20A8519'}, {'id': 18, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/D644669BD0F55C5F1E8CD32F978957E2'}, {'id': 19, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/3FEC255E9922F6CC259A76AE57E15290'}, {'id': 20, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/FD4AEAA172214BC87E97EE1763560A82'}, {'id': 21, 'author': 'Herbert, Frank', 'series': 'Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/76C9353813DDEFEB9F42BBBD9EE1440C'}, {'id': 22, 'author': 'Herbert, Frank', 'series': 'Dune Book 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/DA6742DA77EF6BBDD772FB7EAF5FE259'}, {'id': 23, 'author': 'Herbert, Frank', 'series': 'Dune Chronicles 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/C4D2F8619D70403D0DC3FF8851C0E9FD'}, {'id': 24, 'author': 'Herbert, Frank Patrick', 'series': 'Dune Saga 7; Classic Dune 1', 'title': 'Dune', 'link': 'http://library.lol/fiction/81E8B6E153C824892BED50F7ADF97DC5'}]

print('%-4s %-25s %-25s %-25s' % ('Sno', 'Author', 'Series', 'Title'))
print('%-4s %-25s %-25s %-25s' % ('-'*4, '-'*25, '-'*25,'-'*25))

for book in data:
    print('%(n)-4i %(author)-25s %(series)-25s %(title)-25s' % book)
   
selection = input('Enter selection: ')

for book in data:
    if book['n'] == selection:
        link = book['link']
        
page = requests.get(link).text
soup = BeautifulSoup(page, 'lxml')
h2 = soup.find('h2')
download_url = h2.find('a')['href']

print('Downloading...',)

file_online = requests.get(download_url).content
file_name =  name.capitalize() + '.epub'
open(file_name, 'wb').write(file_online)

print('\nSuccessfully Downloaded')