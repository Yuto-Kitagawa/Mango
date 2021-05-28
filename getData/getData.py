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

year_list = [2019, 2020, 2021]
#全体のレースのリストが載っている年ごとのURL
whole_race_url_array = []
race_url_array = []
for year in year_list:
    whole_race_url_array.append(
        "https://www.jra.go.jp/datafile/seiseki/replay/" + str(year) + "/jyusyo.html")

# レースのURL文回す
for  race_number in whole_race_url_array:
    race_html = requests.get(race_number)
    soup = BeautifulSoup(race_html.content,"lxml")

    for race_url in soup.find_all("td",class_="result"):
        race_url_array.append("https://www.jra.go.jp" +
                              race_url.contents[0].get("href"))
        #年ごとの全重賞のレースのurl
        print(race_url_array)

        for race_detail in race_url_array:
            detail_html = requests.get(race_detail)
            soup = BeautifulSoup(detail_html.content,"lxml")
            
            umaban_array = []
            name_array = []
            age_array = []
            add_weight_array = []
            jockey_array = []
            time_array = []
            trainer_array = []
            margin_array = []
            corner_array = []
            wheather = ""

            # すべてのliタグを検索して、その文字列を表示する
            print("\n/**********馬番************/")
            for umaban in soup.find_all("td", class_='num'):    # すべてのliタグを検索して表示
                umaban_array.append(umaban.text)
            print(umaban_array)

            print("\n/***********馬名***********/")
            for name in soup.find_all("td", class_='horse'):
                name_array.append(name.text)
            print(name_array)

            print("\n/************年齢**************/")
            for age in soup.find_all("td", class_='age'):
                age_array.append(age.text)
            print(age_array)

            print("\n/*************負担重量***********/")
            for add_weight in soup.find_all("td", class_='weight'):
                add_weight_array.append(add_weight.text)
            print(add_weight_array)

            print("\n/***************騎手名**************/")
            for jockey in soup.find_all("td", class_='jockey'):
                jockey_array.append(jockey.text)
            print(jockey_array)

            print("\n/****************タイム**************/")
            for time in soup.find_all("td", class_='time'):
                time_array.append(time.text)
            print(time_array)

            print("\n/****************着差****************/")
            for margin in soup.find_all("td", class_='margin'):
                margin_array.append(margin.text)
            print(margin_array)

            print("\n/****************調教師****************/")
            for corner in soup.find_all("td", class_='trainer'):
                # corner_newをcorner_arrayの最後に格納
                trainer_array.append(corner.text)
            print(trainer_array)

            print("\n/****************コーナー通過順位****************/")
            for corner in soup.find_all("td", class_='corner'):
                # corner_newをcorner_arrayの最後に格納
                corner_array.append(corner.text)
            print(corner_array)

            print("\n/****************天気****************/")
            for weather in soup.find_all("li", class_='weather'):
                # print(weather)
                weather_span = weather.contents[0]
                weather_content = weather_span.contents[1].text
            print(weather_content)

            print("\n/****************レースの距離****************/")
            for course in soup.find_all("div", class_='course'):
                course_dis = course.contents[2]  # 距離(m)
                course_detail = course.contents[3]  # コースの詳細
                print(course_dis)
            print(course_detail.text)

            print("\n/****************レースの階級****************/")
            for grade in soup.find_all("span", class_="grade_icon"):
                grade_content = grade.contents[0].get("alt")  # 子要素の初めのaltを取得(Grade→G1など)
            print(grade_content)
