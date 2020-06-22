from bs4 import BeautifulSoup
import requests
import csv

url = 'https://pastr.io/view/0uD5dtI5gv4'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')  

'''
URL = 'https://www.imdb.com/title/tt2467372/episodes?season='
info = {}
for season in range(1, 8):
    season_info = []
    url = URL + str(season)
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    
    ratings = soup.find_all(class_='ipl-rating-star__rating')
    names = soup.find_all(class_='info')
    
    ratings = [ratings[x] for x in range(0, len(ratings), 23)]
    
    for i in range(0, len(names)):
        name = names[i].strong.a.text
        
        ep_info = []
        ep_info.append(season)
        ep_info.append(i+1)
        ep_info.append(name)
        try:
            ep_info.append(ratings[i].text)
        except IndexError:
            ep_info.append('')
        
        season_info.append(ep_info)
        
    info[season] = season_info

with open('b99.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Season', 'Episode', 'Title', 'Rating'])
    for season in info:
        writer.writerows(info[season])
'''


