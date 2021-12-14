import re
import urllib.request
from bs4 import BeautifulSoup

from src.movie import container

class pirate:
    web = "https://www1.thepiratebay3.to"

    def __init__(self, search) -> None:
        self.search = search
        # /s/0/3/0?q= means sorted by size
        self.url = "".join([
            pirate.web, 
            "/s/0/3/0/page/1/?q=",
            "%20".join(self.search.split(" "))
        ])
        self.soup = pirate.getSoup(self.url)

    def searchContent(self) -> None:
        # initial movie
        movie_index = 0
        movie = container()
        # search every movie info from row <tr>    
        for tr in self.soup.find(
            "table", {"id": "searchResult"}).find("tbody").find_all("tr"):
            movie.getLine(tr, movie_index)
            movie_index += 1
        
        print(movie.movie_set[0]["movie_url"])

    def searchMagnet(self) -> None:
        '''
        pass known idx defined by users
        and open related sub-web to copy magent path
        '''
        pass

    def nextPage(self) -> None:
        '''
        change self.url to next page
        and update related soup file
        e.g.:
        https://www1.thepiratebay3.to/s/0/3/0/page/1/?q=hot%20zone
        '''
        regex = re.compile(r'/page/(\w+)')
        page = int(regex.findall(self.url)[0]) + 1
        page = str(page)
        repl = "/page/" + page
        self.url = regex.sub(repl, self.url)
        self.soup = pirate.getSoup(self.url) 
    
            
            

    @staticmethod
    def getSoup(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read().decode('utf-8')
        return BeautifulSoup(page, features="lxml")
