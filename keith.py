import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautiful soup object
soup = bs(r.content)

# Print out our html
print(soup.prettify())

first_header = soup.find("h2")

headers = soup.find_all("h2")
print(headers)

# Pass in a list of elements to look for
first_header = soup.find(["h1", "h2"])

headers = soup.find_all(["h1", "h2"])
headers

# You can pass in attributes to the find/find_all function
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
paragraph

# You can nest find/find_all calls
body = soup.find('body')
div = body.find('div')
header = div.find('h1')
header


# We can search specific strings in our find/find_all calls
import re

paragraphs = soup.find_all("p", string=re.compile("Some"))
paragraphs

headers = soup.find_all("h2", string=re.compile("(H|h)eader"))
headers

print(soup.body.prettify())

content = soup.select("div p")
content

paragraphs = soup.select("h2 ~ p")
paragraphs

bold_text = soup.select("p#paragraph-id b")
bold_text

paragraphs = soup.select("body > p")
print(paragraphs)

for paragraph in paragraphs:
  print(paragraph.select("i"))

# Grab by element with specific property
soup.select("[align=middle]")

# use .string
header = soup.find("h2")
header.string

# If multiple child elements use get_text
div = soup.find("div")
print(div.prettify())
print(div.get_text())

# Get a specific property from an element
link = soup.find("a")
link['href']

paragraphs = soup.select("p#paragraph-id")
paragraphs[0]['id']

# Path Syntax
print(soup.body.prettify())

# Know the terms: Parent, Sibling, Child

soup.body.find("div").find_next_siblings()

