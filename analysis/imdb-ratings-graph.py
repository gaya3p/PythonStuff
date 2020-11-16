from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import csv
import matplotlib.pyplot as plt

SHOWS = {
    'Game of Thrones': 'tt0944947',
    'Mr. Robot': 'tt4158110',
    'Stranger Things': 'tt4574334',
    'Breaking Bad': 'tt0903747',
    'Chernobyl': 'tt7366338',
    'Friends': 'tt0108778',
    'The Office': 'tt0386676',
    'Narcos': 'tt2707408',
    'The Mandalorian': 'tt8111088',
    'Money Heist': 'tt6468322',
    'Brooklyn Nine-Nine': 'tt2467372',
    'Sherlock': 'tt1475582',
    'The Big Bang Theory': 'tt0898266',
}

WRITE_FILE = False
show_id = SHOWS['Breaking Bad']
URL = f'https://www.imdb.com/title/{show_id}/episodes?season='
info = {}

url = URL + '1'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

dropdown = soup.find(id='bySeason')
seasons_opt = dropdown.find_all('option')
SEASONS = len(seasons_opt)
TITLE = soup.find(itemprop='url').text

# Write a csv file    
def writeFile():
    with open(TITLE+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Season', 'Episode', 'Title', 'Rating'])
        for season in info:
            writer.writerows(info[season])
 
# Draw the graph
def drawPlot():
    eps = 0
    for season, season_info in info.items():
        y = [float(season_info[i][3]) for i in range(len(season_info))]
        x = [eps+i+1 for i in range(len(season_info))]
        eps += len(x)
        lbl = 'S' + str(season).zfill(2)
        plt.scatter(x, y, label=lbl)
        
    plt.xlabel('Episodes')
    plt.ylabel('Rating')
    plt.ylim(top=10)
    plt.title(TITLE)
    plt.legend()
    plt.show()
        
# Web Scraping
for season in range(1, SEASONS+1):
    season_info = []
    url = URL + str(season)
    try:
        page = requests.get(url).text
    except ConnectionError:
        print('No internet connection.')
        break

    soup = BeautifulSoup(page, 'lxml')
    
    ratings = soup.find_all(class_='ipl-rating-star__rating')
    names = soup.find_all(class_='info')
    
    ratings = [ratings[x] for x in range(0, len(ratings), 23)]
    
    print(f'Season {season} loaded.')
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
    
if info:
    drawPlot()
if WRITE_FILE:
    writeFile()
