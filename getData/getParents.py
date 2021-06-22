# coding UTF-8
from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import random
import pandas as pd
import openpyxl as opx
import numpy as np
# 情報を取得し終わったら通知するようにするパッケージ
from plyer import notification

# 使う順
year_list = [2020]
year_url = []
month_list = [11, 12]
# month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_url = []
race_url = []
horse_url_array = []
race_result = []
horse_list = []

father = []
mother = []
parents_whole = []
parents_list = []
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

for url in month_url:
    response = requests.get(url=url, headers=headers)
    soup_race_result = BeautifulSoup(response.content, 'lxml')
    for href in soup_race_result.find_all("td", class_="wsLB"):
        # すべてのレースのURLを作成
        race_url_str = " https://keiba.yahoo.co.jp" + \
            str(href.find("a").get("href"))

        response = requests.get(url=race_url_str, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')
        for href in soup.find_all("td", class_="fntN"):
            # すべての馬のURLを格納
            horse_url = "https://keiba.yahoo.co.jp" + \
                str(href.find("a").get("href"))
            print(horse_url)
            horse_url_array.append(horse_url)
            response = requests.get(url=horse_url, headers=headers)
            soup = BeautifulSoup(response.content, 'lxml')
            # データ削除されている馬があるのでそのエラーをパスする
            try:
                # 親の情報
                parents_whole = []
                for parents_list in soup.select("#dirUmaBlood > tr "):
                    parents_whole.append(parents_list.select_one("td:nth-of-type(1)"))
                father.append(parents_whole[0].text)
                mother.append(parents_whole[4].text)
            except:
                pass

print(len(mother))
print(len(father))


parents_detail = pd.DataFrame(
    {"URL": horse_url_array, "仔馬": child, "父馬": father, "母馬": mother})

parents_detail.to_excel("./excel/parents.xlsx",sheet_name="血統", index=None)
# 自分用
notification.notify(title="デスクトップ通知", message="実行完了", timeout=5)
