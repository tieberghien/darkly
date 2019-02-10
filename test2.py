import requests
from bs4 import BeautifulSoup

listUrl = []

def recursiveUrl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    if links is None or len(links) == 0:
        listUrl.append(url)
        print(url)
        return 1;
    else:
        listUrl.append(url)
        print(url)
        for link in links:
            #print(url+link['href'][1:])
            recursiveUrl(url+link['href'][1:])


recursiveUrl("http://172.20.10.4/.hidden/")
print(listUrl)
