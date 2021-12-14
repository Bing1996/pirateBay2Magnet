import os
from datetime import datetime

class container:
    '''
    save each row movie info from <td> </td>
    this class shoud have index, movie name, movie size and movie update time
    '''
    def __init__(self) -> None:
        
        self.movie_set = {}

    def show(self) -> None:
        for p_id, p_info in self.movie_set.items():
            print("{} : ".format(p_id))
            for key in p_info:
                print("  {:<11} : {}".format(key, p_info[key]))

        
    def getLine(self, tr, idx):
        # td is class BesautifulSoup.Tag
        info = tr.find_all("td")
        try:
            # some tr contains white space
            tr.find("a", {"class": "detLink"}).contents[0]
        except:
                pass
        else:
            '''
            !!! core code part !!!
            the index in td is const due to website html
            !!! dont change this part !!!
            '''
            movie_size = info[4].contents[0]
            movie_name = info[1].find("a").contents[0]
            movie_url = info[1].find("a").get("href")
            if len(str(info[2].contents[0])) < 13:
                movie_date = "-".join([
                    str(datetime.now().year),
                    str(info[2].contents[0])])
            else:
                movie_date = str(info[2].contents[0])

            self.movie_set[idx] = {
                "movie_size" : movie_size,
                "movie_date" : movie_date,
                "movie_name" : movie_name,
                "movie_url" : movie_url
                }
    