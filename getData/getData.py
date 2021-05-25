from bs4 import BeautifulSoup
import urllib.error
import os
import re
import urllib.request
import requests
import time
import datetime
import pandas as pd
import numpy as np

year_list = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
victoria_list = []
for year in year_list:
        victoria_list.append('https://www.jra.go.jp/datafile/seiseki/g1/victoria/result/victoria' +str(year) + '.html')

#作成したvictoriaレースのurl
for url in victoria_list:
        # print(url + "\r")
        print()

##############つかわんやつ###############
# ua = 'Mozilla/5.0 (Macuntosh; Intel Mac OS X 10_12_3)'\
#     'Apple Webkit/537.36(KHTML, like Gecko)'\
#     'Chrome/55.0.2883.95 Safari/537.36'
# req = urllib.request.Request(url, headers={'User-Agent': ua})
# html = urllib.request.urlopen(req)
# soup = BeautifulSoup(html, "lxml")
# td_all = soup.find_all('td',class_='num')
# print(td_all)


url_netkeiba = 'https://db.sp.netkeiba.com/?pid=race_list&word=&start_year=2021&start_mon=1&end_year=none&end_mon=none&jyoken%5B%5D=1&jyoken%5B%5D=2&jyoken%5B%5D=4&jyoken%5B%5D=5&jyoken%5B%5D=6&grade%5B%5D=1&grade%5B%5D=2&grade%5B%5D=3&grade%5B%5D=4&grade%5B%5D=5&grade%5B%5D=6&grade%5B%5D=7&grade%5B%5D=8&kyori_min=&kyori_max=&sort=date&submit='
html = requests.get(url_netkeiba)
soup = BeautifulSoup(html.content, "lxml")
race_array = []
race_name_array = []

print("\n/**********レースのURL************/")
search = re.compile('^https://db.sp.netkeiba.com/race/')

#レースのURL
for race in soup.find_all("a"):
    print(race.get("href"))
    # race_name_array.append(race)
    # print(race_name_array)
    # print(race_array)

#レース名
print("\n/**********レースの名前************/")
for race_name in soup.find_all(class_='LimitsWidth'):
    race_name_array.append(race_name.text)
    print(race_name.text)

# html = requests.get(victoria_list[11])
# soup = BeautifulSoup(html.content, "lxml")
# umaban_array = []
# name_array = []
# age_array = []
# add_weight_array = []
# jockey_array = []
# time_array = []
# margin_array = []
# corner_array = []

# # すべてのliタグを検索して、その文字列を表示する
# print("\n/**********馬番************/")
# for umaban in soup.find_all("td", class_='num'):    # すべてのliタグを検索して表示
#     umaban_array.append(umaban.text)
#     print(umaban.text)

# print("\n/***********馬名***********/")
# for name in soup.find_all("td", class_='horse'):
#     name_array.append(name.text)
#     print(name.text)

# print("\n/************年齢**************/")
# for age in soup.find_all("td", class_='age'):
#     age_array.append(age.text)
#     print(age.text)

# print("\n/*************負担重量***********/")
# for add_weight in soup.find_all("td", class_='weight'):
#     add_weight_array.append(add_weight.text)
#     print(add_weight.text)

# print("\n/***************騎手名**************/")
# for jockey in soup.find_all("td", class_='jockey'):
#     jockey_array.append(jockey.text)
#     print(jockey.text)

# print("\n/****************タイム**************/")
# for time in soup.find_all("td", class_='time'):
#     time_array.append(time.text)
#     print(time.text)

# print("\n/****************着差****************/")
# for margin in soup.find_all("td", class_='margin'):
#     margin_array.append(margin.text)
#     print(margin.text)

# for corner in soup.find_all("td", class_='corner'):
#     # \nを消したい→正規表現で\nを消す
#     corner_new = re.sub(r'\n', '', corner,count=0)
#     # corner_newをcorner_arrayの最後に格納
#     corner_array.append(corner.text)

