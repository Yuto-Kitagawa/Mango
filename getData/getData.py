from bs4 import BeautifulSoup
import os
import re
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
weather_array = []
tyakujun_array = []

#取り出す年を配列に記入
#~2017,2018,2019~でクラス名が分けられている
year_list = [2019,2020,2021]

whole_race_url_array = []
race_url_array = []

#取り出し処理がどのくらい終わっているかわかりやすく表示するためのcounter
#別に処理に必要ではない
#2019～2021は340レースなので
counter = 340

# yearがfor文の中に入っていないので判定で使えるようにcounterを用意
year_counter = 2019

# for文でURL作成
for year in year_list:
    whole_race_url_array.append(
        "https://www.jra.go.jp/datafile/seiseki/replay/" + str(year) + "/jyusyo.html")
        

# 年の分、レースのURL文回す
for race_number in whole_race_url_array:
    race_html = requests.get(race_number)
    soup = BeautifulSoup(race_html.content, "lxml")

    for race_url in soup.find_all("td", class_="result"):  # 年ごとの１レースのurl
        if(race_url is not None and len(race_url) > 0):     # class="result"があるかどうかを判定

            # class="result"の1つ目の子要素(a href="")のhrefのURLをrace_urlに格納
            race_url = "https://www.jra.go.jp" + race_url.contents[0].get("href")
            detail_html = requests.get(race_url)
            soup = BeautifulSoup(detail_html.content, "lxml")

            #####################################
            #年でクラス名が違うが2019年からしかとっていないので判定は書いていない
            #書くならここにif文でyear_counterを使って判定する
            #####################################       

            #レースのリスト作成時必要データ
            date_array.append(soup.find("div", class_="date").get_text())
            race_name_array.append(soup.find("span", class_="race_name").contents[0])
            weather_array.append(soup.find("li", class_="weather").get_text())
            course_dis_array.append(soup.find("div", class_="course").contents[1])
            course_detail_array.append(soup.find("div", class_='course').contents[3].text)
            grade_array.append(soup.find("span", class_="grade_icon").contents[0].get("alt"))
            
            #レースの詳細作成時必要データ
            #着順
            for tyaku in soup.find_all("td", class_='place'):
                tyakujun_array.append(tyaku.text)

            #馬番
            for umaban in soup.find_all("td", class_='num'):
                umaban_array.append(umaban.text)
            
            #馬名
            for name in soup.find_all("td", class_='horse'):
                name_array.append(name.text)

            # 年齢
            for age in soup.find_all("td", class_='age'):
                age_array.append(age.text)

            # 斤量
            for add_weight in soup.find_all("td", class_='weight'):
                add_weight_array.append(add_weight.text)

            #騎手
            for jockey in soup.find_all("td", class_='jockey'):
                jockey_array.append(jockey.text)

            # 馬体重
            for weight in soup.find_all("td", class_='h_weight'):
                weight_array.append(weight.contents[0])

            # タイム
            for time in soup.find_all("td", class_='time'):
                time_array.append(time.text)

            # 着差
            for margin in soup.find_all("td", class_='margin'):
                margin_array.append(margin.text)

            #調教師
            for trainer in soup.find_all("td", class_='trainer'):
                trainer_array.append(trainer.text)

            # コーナー通過順位
            for corner in soup.find_all("td", class_='corner'):
                corner_array.append(corner.text)
            
            #残りレースの処理数を表示
            counter -= 1
            print(counter)
            
#レースのリストの行数
print(len(date_array))
print(len(grade_array))
print(len(course_dis_array))
print(len(course_detail_array))
print(len(weather_array))

#レースの詳細の行数
print(len(umaban_array))
print(len(name_array))
print(len(age_array))
print(len(add_weight_array))
print(len(jockey_array))
print(len(time_array))
print(len(weight_array))
print(len(trainer_array))
print(len(margin_array))
print(len(corner_array))

########################################
#エクセルファイルにするには同じ行数でないといけない
#なので二つのファイルに分けた
#もしレースの詳細のデータが見にくかったら配列に空白を入れてレースごとに分ける
#########################################

#レースのリストをエクセルファイルにエクスポート
# race_list = pd.DataFrame({'日付': date_array, 'レース名': race_name_array, '階級': grade_array,
#                          'コースの詳細': course_detail_array, 'コースの距離': course_dis_array, '天気': weather_array})
# race_list.to_excel('./レースデータ.xlsx', header=False, index=False)

# レースの詳細をエクセルファイルにエクスポート
race_detail = pd.DataFrame(
    {'着順':tyakujun_array,'馬番': umaban_array, '馬名': name_array, '斤量': add_weight_array, '年齢': age_array, '騎手': jockey_array, 'タイム': time_array, '体重': weight_array, '調教師': trainer_array, '着差': margin_array, 'コーナー通過': corner_array})
race_detail.to_excel('./レース詳細.xlsx', header=False, index=False)
