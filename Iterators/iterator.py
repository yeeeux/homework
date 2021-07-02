import requests
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep


class PageParsing:
    def __init__(self, pages, count_articles):
        self.pages = pages
        self.count_articles = count_articles
        self.URL = "https://www.geeksforgeeks.org/page/"
        self.page = 0

    def __iter__(self):

        return self

    def __next__(self):
        if self.page < self.pages:
            wait = randint(2, 10)
            print(f"We wait {wait} seconds")
            sleep(wait)
            self.req = requests.get(self.URL + str(self.page) + "/")
            self.soup = bs(self.req.text, "html.parser")
            self.titles = self.soup.find_all("div", attrs={"class", "head"})
            self.page += 1
            answer = {}
            for article in range(4, self.count_articles):
                if self.page > 1:
                    answer.update(
                        {(article - 3) + self.page * 15: self.titles[article].text}
                    )
                else:
                    answer.update({article - 3: self.titles[article].text})
            print(f"Page {self.page}")
            return answer
        else:
            raise StopIteration


a = PageParsing(10, 19)
for j in a:
    print(j)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
