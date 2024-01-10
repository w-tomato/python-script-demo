import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "}

for start_num in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(start_num) + "&filter="
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    for title in soup.select(".title"):
        if "/" not in title.string:
            print(title.string)
