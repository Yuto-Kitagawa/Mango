from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import pandas as pd
import numpy as np

# 使う順
year_list = [2019, 2020]
year_url = []
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_url = []
race_url = []
race_result = []
horse_list = []
father = []
mother = []
child = []

for year in year_list:
    year_url.append("https://keiba.yahoo.co.jp/schedule/list/"+str(year))
# 年分のURLが作成される
# print(year_url)

# 1年ごとのURL
for url in year_url:
    # 月ごとのURL
    for month in month_list:
        # 月ごとのURLが作成される
        month_url.append(url+"/?month="+str(month))
        # print(url+"/?month="+str(month))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
counter = 0
for url in month_url:
    response = requests.get(url=url, headers=headers)
    soup_race_result = BeautifulSoup(response.content, 'lxml')
    for href in soup_race_result.find_all("td", class_="wsLB"):
        # すべてのレースのURLを作成
        race_result.append(" https://keiba.yahoo.co.jp" +
                           str(href.find("a").get("href")))
        counter += 1
        print(counter)
    print(len(race_result))

for url in race_result:
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    for href in soup.find_all("td", class_="fntN"):
        # すべての馬のURLを格納
        horse_list.append("https://keiba.yahoo.co.jp" +
                          str(href.find("a").get("href")))
        counter += 1
        print(counter)
counter = 0
for getParents in horse_list:
    response = requests.get(url=getParents, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    #仔馬１親馬２の割合なので仔馬を二回格納する
    child_name = soup.find("h1", class_="fntB").get_text()    
    child.append(child_name)
    child.append(child_name)
    #親馬はcssセレクタでしか選択できなかったためselect()を使った
    mother = []
    father = []
    for father_list in soup.select("#dirUmaBlood > tr "):
        father.append(father_list.select_one("td:nth-of-type(1)"))
    for mother_list in soup.select("#dirUmaBlood > tr"):
        mother.append(mother_list.select_one("td:nth-of-type(1)"))

print(len(child))
print(len(mother))
print(len(father))

parents_detail = pd.DataFrame(
    {"仔馬": child, "父馬": father, "母馬": mother})
parents_detail.to_excel('./血統.xlsx', header=False, index=False)
