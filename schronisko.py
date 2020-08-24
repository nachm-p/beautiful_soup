import requests
from bs4 import BeautifulSoup as bs
import json
from pandas import DataFrame as df
import re

page = requests.get("https://schroniskopsiepole.pl/do-adopcji/psy/")

links1 = bs(page.text, 'html.parser')

# state_list = soup.find(class_ = 'cmsms_img_rollover_wrap preloader')
# state_list = soup.find_all(class_ = 'cmsms_img_rollover_wrap preloader')

dog_links = [] # initialise empty list

for link in links1.find_all('a', class_ = 'cmsms_open_link'):
    dog_links = link.get('href')
    # print(dog_links)

dog_info = bs(page.content, 'html.parser')

info = dog_info.select("div.project_outer img")
image_url = info[0]['src']
print(image_url)

title = dog_info.find_all('a', class_ = 'cmsms_image_link')
name = title[0]['title']
print(name)





'''
dog_names = bs(page.content, 'html.parser')
dog_links = dog_names.find('a', class_ = 'cmsms_open_link')
names = dog_links.get("title")
print(names)

dog_pics = bs(page.content, 'html.parser')

for img in dog_pics.find('div', class_ = 'project_outer'):
    pic = dog_pics.get('href')
    print(pic)
'''