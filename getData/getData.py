from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import pandas as pd
import numpy as np
# import urllib.error
# import urllib.request

##############つかわんやつ###############
# ua = 'Mozilla/5.0 (Macuntosh; Intel Mac OS X 10_12_3)'\
#     'Apple Webkit/537.36(KHTML, like Gecko)'\
#     'Chrome/55.0.2883.95 Safari/537.36'
# req = urllib.request.Request(url, headers={'User-Agent': ua})
# html = urllib.request.urlopen(req)
# soup = BeautifulSoup(html, "lxml")
# td_all = soup.find_all('td',class_='num')
# print(td_all)
#########################################


#############netkeiba参照###############
# url_netkeiba = 'https://db.sp.netkeiba.com/?pid=race_list&word=&start_year=2021&start_mon=1&end_year=none&end_mon=none&jyoken%5B%5D=1&jyoken%5B%5D=2&jyoken%5B%5D=4&jyoken%5B%5D=5&jyoken%5B%5D=6&grade%5B%5D=1&grade%5B%5D=2&grade%5B%5D=3&grade%5B%5D=4&grade%5B%5D=5&grade%5B%5D=6&grade%5B%5D=7&grade%5B%5D=8&kyori_min=&kyori_max=&sort=date&submit='
# netkeiba_html = requests.get(url_netkeiba)
# soup = BeautifulSoup(netkeiba_html.content, "lxml")
# race_array = []
# race_url_array = []
# race_name_array = []

# print("\n/**********レースのURL************/")
# search = re.compile('^https://db.sp.netkeiba.com/race/')

# # レースのURL
# for race in soup.find_all("li", class_="fc"):
#     race_url_array.append(race.contents[1].contents[3].get("href"))
# print(race_url_array)

# # レース名
# print("\n/**********レースの名前************/")
# for race_name in soup.find_all(class_='LimitsWidth'):
#     race_name_array.append(race_name.text)
# print(race_name_array)
#########################################

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
year_list = [2019,2020,2021]
# 全体のレースのリストが載っている年ごとのURL
whole_race_url_array = []
race_url_array = []
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

            #レースのリスト作成時必要データ
            
            date_array.append(soup.find("div", class_="date").get_text())
            race_name_array.append(soup.find("span", class_="race_name").contents[0])
            weather_array.append(soup.find("li", class_="weather").get_text())
            course_dis_array.append(soup.find("div", class_="course").contents[1])
            course_detail_array.append(soup.find("div", class_='course').contents[3].text)
            grade_array.append(soup.find("span", class_="grade_icon").contents[0].get("alt"))
            counter -= 1
            print(counter)
            
            #レースの詳細作成時必要データ

            for umaban in soup.find_all("td", class_='num'):
                umaban_array.append(umaban.text)
            
            # print("\n/***********馬名***********/")
            for name in soup.find_all("td", class_='horse'):
                name_array.append(name.text)

            # print("\n/************年齢**************/")
            for age in soup.find_all("td", class_='age'):
                age_array.append(age.text)

            # print("\n/*************負担重量***********/")
            for add_weight in soup.find_all("td", class_='weight'):
                add_weight_array.append(add_weight.text)

            # print("\n/***************騎手名**************/")
            for jockey in soup.find_all("td", class_='jockey'):
                jockey_array.append(jockey.text)

            # print("\n/****************馬体重****************/")
            for weight in soup.find_all("td", class_='h_weight'):
                weight_array.append(weight.contents[0])

            # print("\n/****************タイム**************/")
            for time in soup.find_all("td", class_='time'):
                time_array.append(time.text)

            # print("\n/****************着差****************/")
            for margin in soup.find_all("td", class_='margin'):
                margin_array.append(margin.text)

            # print("\n/****************調教師****************/")
            for trainer in soup.find_all("td", class_='trainer'):
                # corner_newをcorner_arrayの最後に格納
                trainer_array.append(trainer.text)

            # print("\n/****************コーナー通過順位****************/")
            for corner in soup.find_all("td", class_='corner'):
                corner_array.append(corner.text)

            # umaban_array.append(soup.find_all("td", class_="num"))
            # name_array.append(soup.find_all("td", class_="horse"))
            # age_array.append(soup.find("td", class_="age").text)
            # add_weight_array.append(soup.find("td", class_="weight").text)
            # jockey_array.append(soup.find("td", class_="jockey").text)
            # weight_array.append(soup.find("td", class_="h_weight").text)
            # time_array.append(soup.find("td", class_="time").text)
            # margin_array.append(soup.find("td", class_="margin").text)
            # trainer_array.append(soup.find("td", class_="trainer").text)
            # corner_array.append(soup.find("td", class_="corner").text)

            

print(len(date_array))
print(len(grade_array))
print(len(course_dis_array))
print(len(course_detail_array))
print(len(weather_array))

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

#レースのリスト作成は完成済み
# race_list = pd.DataFrame({'日付': date_array, 'レース名': race_name_array, '階級': grade_array,
#                          'コースの詳細': course_detail_array, 'コースの距離': course_dis_array, '天気': weather_array})
# race_list.to_excel('./レースデータ.xlsx', header=False, index=False)


race_detail = pd.DataFrame(
    {'馬番': umaban_array, '馬名': name_array, '斤量': add_weight_array, '年齢': age_array, '騎手': jockey_array, 'タイム': time_array, '体重': weight_array, '調教師': trainer_array, '着差': margin_array, 'コーナー通過': corner_array})
race_detail.to_excel('./レース詳細.xlsx', header=False, index=False)
