# coding: UTF-8
from plyer import notification
import MySQLdb
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import os
import re
import requests
##
# 今週の重賞レースのレース名と出馬表を
# 最終的に配列に格納するスクレイピング
##

race_name = []
race_href = []
horse = []
waku = []
kisyu = []
ninki = []

url = "https://umanity.jp/racedata/graderace/"
url_html = requests.get(url)
soup = BeautifulSoup(url_html.content, "lxml")
race_name.append(soup.select_one(".g_race_racename > span > a").text)
for race_name_array in soup.select(".race_box_name > span > a"):
    race_name.append(race_name_array.text)
    race_href.append(race_name_array.get("href"))

i = 0
# たしかかっこの中は継続条件なので、とりたいレース分iを変化させる
while(i < 2):
    for race_detail_array in race_href:
        race_url_html = requests.get(race_detail_array)
        soup = BeautifulSoup(race_url_html.content, "lxml")
        # 馬名
        for horse_name in soup.select(""):
            horse.append(horse_name.text)
        # 枠
        for waku_num in soup.select(""):
            waku.append(waku_num.text)
        # 人気
        for ninki_array in soup.select(""):
            ninki.append(ninki_array.text)
        # 騎手
        for kisyu_array in soup.select(""):
            kisyu.append(kisyu_array.text)

notification.notify(title="実行完了", message="SQLの処理が完了しました", timeout=5)
