import requests
from bs4 import BeautifulSoup

def recursiveUrl(url, link, depth):
    if depth == 3:
        return url
    else:
        print(link['href'])
        page = requests.get(url + link['href'])
        soup = BeautifulSoup(page.text, "lxml")
        newlink = soup.find('a')
        if newlink is None or len(newlink) == 0:
            return link
        else:
            return link, recursiveUrl(url, newlink, depth + 1)

def getLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        links.append(recursiveUrl(url, link, 1))
#        print(links)
    return links

links = getLinks("http://10.11.200.126/.hidden/")
print(links)
