from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import pandas as pd
import numpy as np

url_first = []
url_third = []
get_href = []
# 調べる年
year_list = [2019, 2020,2021]
for year in year_list:
    url_first.append(
        "https://www.keibalab.jp/db/race/grade.html?year="+str(year))

print(url_first[0])

for url_second in url_first:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }

    soup = BeautifulSoup(requests.get(url_second, headers=headers).content, "lxml")

    for race_url in soup.find_all("td", class_="bold"):
        if(race_url is not None and len(race_url) > 0):
            get_href = race_url.contents[2].get("href")
            url_third.append("https: // www.keibalab.jp/"+str(get_href))
        else:
            print("success")
    print(url_third)
    print(len(url_third))
