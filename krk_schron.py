import requests
from bs4 import BeautifulSoup as bs

strona = 'http://www.schronisko.krakow.pl/Adopcje/ZWIERZAKI_DO_ADOPCJI/Psy/'

for i in range(0, 13):
    pages = requests.get((strona + "?p={}".format(i)))
    content = bs(pages.content, 'html.parser')

    for name in content.select("div.desc_anim"):
        dog_names = name.find('p').text
        print(dog_names)

    for link in content.find_all(class_='news_short_more'):
        dog_links = link.get('href')
        print('http://www.schronisko.krakow.pl' + dog_links)