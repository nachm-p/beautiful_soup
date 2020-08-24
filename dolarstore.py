import requests
from bs4 import BeautifulSoup as bs
import json
from pandas import DataFrame as df

page = requests.get("https://www.familydollar.com/locations/")
# page = requests.get("https://keithgalli.github.io/web-scraping/example.html")
# page.encoding = 'ISO-885901'
soup = bs(page.text, 'html.parser')

# soup = bs(page.content, 'html.parser')

# print(soup)
# print(soup.prettify()) #caly source code

# state_list = soup.find_all('href')
# print(state_list)

state_list = soup.find_all(class_ = 'itemlist')
# for i in state_list[:2]:
#    print(i)

# type(state_list)
# len(state_list)

# example = state_list[2] # a representative example
# example_content = example.contents[0]
# print(example_content)

state_links = [] # initialise empty list

for i in state_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)

# print(state_links)

#  check to be sure all went well
# for i in city_hrefs[:2]:
    # print(i)

city_links = []

for link in state_links:
    page = requests.get(link)
    soup = bs(page.text, 'html.parser')
    familydollar_list = soup.find_all(class_ = 'itemlist')
    for store in familydollar_list:
        cont = store.contents[0]
        attr = cont.attrs
        city_hrefs = attr['href']
        city_links.append(city_hrefs)

# print(city_links)

# page2 = requests.get(city_hrefs[2]) # again establish a representative example
# soup2 = bs(page2.text, 'html.parser')

# arkansas = soup2.find_all(class_ = 'itemlist_fullwidth')
# print(arkansas)

# to get individual store links
store_links = []

for link in city_links:
    locpage = requests.get(link)
    locsoup = bs(locpage.text, 'html.parser')
    locinfo = locsoup.find_all(type="application/ld+json")
    for i in locinfo:
        loccont = i.contents[0]
        locjson = json.loads(loccont)
        try:
            store_url = locjson['url']
            store_links.append(store_url)
        except:
            pass

# get address and geolocation information
stores = []

for store in store_links:
    storepage = requests.get(store)
    storesoup = bs(storepage.text, 'html.parser')
    storeinfo = storesoup.find_all(type="application/ld+json")
    for i in storeinfo:
        storecont = i.contents[0]
        storejson = json.loads(storecont)
        try:
            store_addr = storejson['address']
            store_addr.update(storejson['geo'])
            stores.append(store_addr)
        except:
            pass

print(store_addr)

# final data parsing
stores_df = df.from_records(stores)
stores_df.drop(['@type', 'addressCountry'], axis = 1, inplace = True)
stores_df['Store'] = "Family Dollar"

df.to_csv(stores_df, "family_dollar_locations.csv", sep = ",", index = False)

'''
page.text() for text (most common)
page.content() for byte-by-byte output
page.json() for JSON objects
page.raw() for the raw socket response (no thank you)

page = requests.get(URL)
page.encoding = 'ISO-885901'
soup = bs(page.text, 'html.parser')

state_list = soup.find_all(class = 'itemlist')

state_links = []:

for i in state_list:
    cont = i.contents[0]
    attr = cont.attrs
    hrefs = attr['href']
    state_links.append(hrefs)
'''
