from bs4 import BeautifulSoup
import requests
#import matplotlib.pyplot as plt

URL = 'https://www.imdb.com/title/tt2467372/episodes?season='

for season in range(1, 8):
    print('Season', season)
    url = URL + str(season)
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    
    ratings = soup.find_all(class_='ipl-rating-star__rating')
    names = soup.find_all(class_='info')
    #rats = []
    
    for i in range(0, len(ratings), 23):
        name = names[int(i/23)].strong.a.text
        #rats.append(float(ratings[i].text))
        print(name, ':', ratings[i].text)
        
    print()
        
    #x = [x for x in range(len(rats))]
    #plt.scatter(x, rats, label=season)
    
#plt.legend()