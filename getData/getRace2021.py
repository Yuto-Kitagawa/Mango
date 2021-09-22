# coding: UTF-8
from bs4 import BeautifulSoup
import os
import re
import urllib3
import requests
import time
import datetime
import pandas as pd
import numpy as np


# 宣言/初期化
date_array = []
umaban_array = []
race_name_array = []
name_array = []
age_array = []
add_weight_array = []
jockey_array = []
time_array = []
weight_array = []
trainer_array = []
margin_array = []
corner_array = []
grade_array = []
course_dis_array = []
course_detail_array = []
course_dis_array_sub = []
weather_array = []
tyakujun_array = []
url_array = []
status_array = []
hour_array = []
hour_array_sub = []
waku_array = []
ftime_array = []
race_url_array = []
increase_array = []
race_number = []


year = 2021
whole_race_url_array = []
whole_race_url_array = []

url = "https://www.keibalab.jp/db/race/grade.html?year=2021"

# headersがないとpage not foundになる
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}

url_parent = requests.get(url=url, headers=headers)
soup = BeautifulSoup(url_parent.content, "lxml")

for race_url in soup.select(".tC > a"):
    if(race_url is not None and len(race_url) > 0):
        race_url_str = "https://www.keibalab.jp" + race_url.get("href")
        race_url_array.append(race_url_str)

for url in race_url_array:
    request = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(request.content, "lxml")
    print(url)

    # レース名とグレードを配列に格納
    for name in soup.select("h1.raceTitle"):
        rename = name.text.strip()
        grade_array.append(rename[-3:-1])
        race_name_array.append(rename[:10])

    for date in soup.select("div.fL.ml10 > p.bold"):
        date_array.append(date.text[:13])

    # コースの距離と種類を配列に格納
    for race_style in soup.select("ul.classCourseSyokin.clearfix > li:nth-child(2)"):
        course_detail_array.append(race_style.text[:1])
        course_dis_array.append(race_style.text[1:5])

    # 着順を配列に格納
    for tyaku in soup.select("tr > td.tC:first-child"):
        tyakujun_array.append(tyaku.text)

    # 馬名を配列に格納
    for umamei in soup.select("table.resulttable > tbody >  tr > td:nth-child(4) > a"):
        name_array.append(umamei.text)

    # 枠番を配列に格納
    for waku in soup.select("table.resulttable > tbody >  tr > td:nth-child(2)"):
        waku_array.append(waku.text)

    # 馬番を配列に格納
    for umaban in soup.select("tr > td.tC:nth-child(3)"):
        umaban_array.append(umaban.text)

    # 年齢を配列に格納
    for age in soup.select("table.resulttable > tbody >  tr > td.tC:nth-child(5)"):
        age_array.append(age.text[1:])

    # 騎手を配列に格納
    for jockey in soup.select("table.resulttable > tbody >  tr > td.tC:nth-child(7)"):
        jockey_array.append(jockey.text)

    # 斤量を配列に格納
    for add_weight in soup.select("table.resulttable > tbody >  tr > td.tC:nth-child(6)"):
        add_weight_array.append(add_weight.text)

    # 時間を配列に格納
    for time in soup.select("table.resulttable > tbody >  tr > td:nth-child(10)"):
        time_array.append(time.text)

    # 着差を配列に格納
    for margin in soup.select("table.resulttable > tbody >  tr > td:nth-child(11)"):
        margin_array.append(margin.text)

    # 上りを配列に格納
    for corner in soup.select("table.resulttable > tbody >  tr > td:nth-child(13)"):
        corner_array.append(corner.text)

    # 馬体重を配列に格納
    for weight in soup.select("table.resulttable > tbody >  tr > td:nth-child(15)"):
        weight_array.append(weight.text[:3])

    # 体重の増減を配列に格納
    for increase in soup.select("table.resulttable > tbody >  tr > td:nth-child(15)"):
        increase_array.append(increase.text[-4:])

print(len(race_url_array))
print(len(race_name_array))
print(len(date_array))
print(len(grade_array))
print(len(course_detail_array))
print(len(course_dis_array))


print(len(tyakujun_array))
print(len(waku_array))
print(len(umaban_array))
print(len(name_array))
print(len(age_array))
print(len(add_weight_array))
print(len(jockey_array))
print(len(time_array))
print(len(margin_array))
print(len(corner_array))
print(len(weight_array))
print("end")

race_detail = pd.DataFrame(
    {'URL': race_url_array, 'レース名': race_name_array, '日付': date_array, '階位': grade_array, 'コースの詳細': course_detail_array, 'コースの距離': course_dis_array})

horse_detail = pd.DataFrame(
    {'着順': tyakujun_array,  '馬番': umaban_array, '枠': waku_array, '馬名': name_array, '年齢': age_array, '斤量': add_weight_array, '騎手': jockey_array, '着差': margin_array, '時間': time_array, '上り': corner_array, '馬体重': weight_array, '体重増減': increase_array})


race_detail.to_excel('./excel/レース2021.xlsx',
                     index=False, sheet_name='all_data')
horse_detail.to_excel('./excel/出馬表2021.xlsx',
                      index=False, sheet_name='all_data')
