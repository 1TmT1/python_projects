import threading
import time
import requests


def print_time(timer):
    for x in range(timer, 0, -1):
        time.sleep(1)
        print(str(x))


def download_all(url):
    movies = []
    for x in range(0, 32):
        movies.append(requests.get(url + "movie" + str(x+1) + ".txt"))
        print(movies[x].text)


def main():
    url = "https://data.cyber.org.il/os/demo/"
    download_all(url)


if __name__ == "__main__":
    main()
