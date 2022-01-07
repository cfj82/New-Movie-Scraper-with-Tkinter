import tkinter as tk
from bs4 import BeautifulSoup
import requests

def scrape_soon():
    coming_soon_url = "https://www.moviefone.com/coming-soon/"
    rcoming_url = requests.get(coming_soon_url)
    # print(rcoming_url)
    if rcoming_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(rcoming_url.text, "html.parser")
        # print(soup.prettify())
        coming_names = soup.find_all('a', {'class':'hub-movie-title'})
        # print(coming_names)
        # loop to return all text
        for word in soup.find_all('a', {'class':'hub-movie-title'}):
            titles = word.get_text()
            print(titles)

def scrape_comedy():
    url = "https://www.moviefone.com/coming-soon/comedy/"
    req_url = requests.get(url)
    # print(req_url)
    if req_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(req_url.text, "html.parser")
        # print(soup.prettify())
        movie_names = soup.find_all('a', {'class':'hub-movie-title'})
        # print(movie_names)
        # loop to return all text
        for word in soup.find_all('a', {'class':'hub-movie-title'}):
            titles = word.get_text()
            print(titles)


def scrape_drama():
    url = "https://www.moviefone.com/coming-soon/drama/"
    req_url = requests.get(url)
    # print(req_url)
    if req_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(req_url.text, "html.parser")
        # print(soup.prettify())
        movie_names = soup.find_all('a', {'class': 'hub-movie-title'})
        # print(movie_names)
        # loop to return all text
        for word in soup.find_all('a', {'class': 'hub-movie-title'}):
            titles = word.get_text()
            print(titles)


def scrape_scifi():
    url = "https://www.moviefone.com/coming-soon/science-fiction/"
    req_url = requests.get(url)
    # print(req_url)
    if req_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(req_url.text, "html.parser")
        # print(soup.prettify())
        movie_names = soup.find_all('a', {'class': 'hub-movie-title'})
        # print(movie_names)
        # loop to return all text
        for word in soup.find_all('a', {'class': 'hub-movie-title'}):
            titles = word.get_text()
            print(titles)

def scrape_crime():
    url = "https://www.moviefone.com/coming-soon/crime/"
    req_url = requests.get(url)
    # print(req_url)
    if req_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(req_url.text, "html.parser")
        # print(soup.prettify())
        movie_names = soup.find_all('a', {'class': 'hub-movie-title'})
        # print(movie_names)
        # loop to return all text
        for word in soup.find_all('a', {'class': 'hub-movie-title'}):
            titles = word.get_text()
            print(titles)

def scrape_adventure():
    url = "https://www.moviefone.com/coming-soon/adventure/"
    req_url = requests.get(url)
    # print(req_url)
    if req_url == "404":
        print("Failed Request")
    else:
        soup = BeautifulSoup(req_url.text, "html.parser")
        # print(soup.prettify())
        movie_names = soup.find_all('a', {'class': 'hub-movie-title'})
        # print(movie_names)
        # loop to return all text
        for word in soup.find_all('a', {'class': 'hub-movie-title'}):
            titles = word.get_text()
            print(titles)


scrape_adventure()