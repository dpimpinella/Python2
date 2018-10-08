import urllib.request
from bs4 import BeautifulSoup

goodreads = "https://www.forbes.com/sites/samanthasharf/2017/11/28/full-list-americas-most-expensive-zip-codes-2017/#1522269d5d19"
req = urllib.request.Request(goodreads)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

soup = BeautifulSoup(the_page, 'html.parser')

res = soup.ol.ol.find_all("li")
print(res)

for item in res:
    print(str(item)[4:9])
    
