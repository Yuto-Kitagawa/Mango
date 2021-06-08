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
parents = []
get_href = []
umamei = []
td = []
# 調べる年を下の配列に記入
year_list = [2020]
#処理が長いのでカウンターで残り時間を表示
counter = 150

#年ごとのURLを作成
for year in year_list:
    url_first.append(
        "https://www.keibalab.jp/db/race/grade.html?year="+str(year))

#年ごとの重賞レースのリストWebページを表示
for url_second in url_first:
    # headersがないと404で拒否されるので記載
    # headersは下のサイトで確認可
    # https: // www.ugtop.com/spill.shtml
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }
    soup = BeautifulSoup(requests.get(
        url_second, headers=headers).content, "lxml")

    for race_url in soup.find_all("td", class_="bold"):
        get_href = race_url.contents[2].get("href")
        #レース結果の詳細のURL作成→url_thirdに格納
        url_third_str = "https://www.keibalab.jp"+str(get_href)
        url_third.append(url_third_str)
        soup = BeautifulSoup(requests.get(url_third_str,headers=headers).content,"lxml")

        #馬1頭の詳細のURLを取得
        for url in soup.find_all("table",class_="DbTable stripe resulttable"):
            for tbody in url.find_all("tbody"):
                for tr in tbody.find_all("tr"):
                    href = tr.contents[7].contents[0].get("href")
                    url_horse = "https://www.keibalab.jp" + str(href)
                    #仔馬の名前を格納
                    umamei.append(tr.contents[7].contents[0].text)
                    umamei.append(" ")
                    # URLを読み込み
                    soupsan = BeautifulSoup(requests.get(
                    url_horse, headers=headers).content, "lxml")
                    # 親馬の名前を取得
                    for parent in soupsan.find_all("span", class_='bold std15'):
                        parents.append(parent.text)
    # print(url_third)

horse_parents = pd.DataFrame(
    {"馬名":umamei,"馬親":parents})
race_detail.to_excel('./馬親.xlsx', header=False, index=False)
    
