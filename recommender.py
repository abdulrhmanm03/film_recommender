import random

import requests
from bs4 import BeautifulSoup

films = []


def get_film_title(soup, films):
    elements = soup.find_all(class_="image")
    for element in elements:
        films.append(element.get("alt"))


def main(username):

    url = f"https://letterboxd.com/{username}/watchlist/"
    try:
        r = requests.get(url)
    except:
        print("failed to fetch the data make sure the username is valid")
        return 0

    print("fetching the data...")

    soup = BeautifulSoup(r.content, "html.parser")
    get_film_title(soup, films)
    paginate_page = soup.find_all(class_="paginate-page")
    if paginate_page:
        n = int(paginate_page[-1].text)
        for i in range(2, n + 1):

            url = f"https://letterboxd.com/{username}/watchlist/page/{i}"
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            get_film_title(soup, films)

    print(f"you shall watch {random.choice(films)}")


if __name__ == "__main__":
    username = input("Enter your letterboxd username: ")
    main(username)
