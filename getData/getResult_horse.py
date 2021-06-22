
####################
# 仔馬の情報はいらないのでこのコードは必要ありません
####################


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
from plyer import notification

# 使う順
year_list = [2019]
year_url = []
month_list = [3, 4]
# month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_url = []
race_url = []
horse_url_array = []
race_result = []
horse_list = []
GI_first = []
GII_first = []
GIII_first = []
otherjusyo_first = []
jusyo_sum_first = []
special_first = []
sum_first = []
GI_second = []
GII_second = []
GIII_second = []
otherjusyo_second = []
jusyo_sum_second = []
special_second = []
sum_second = []
GI_third = []
GII_third = []
GIII_third = []
otherjusyo_third = []
jusyo_sum_third = []
special_third = []
sum_third = []
GI_fourth = []
GII_fourth = []
GIII_fourth = []
otherjusyo_fourth = []
jusyo_sum_fourth = []
special_fourth = []
sum_fourth = []
GI_syussou = []
GII_syussou = []
GIII_syussou = []
otherjusyo_syussou = []
jusyo_sum_syussou = []
special_syussou = []
sum_syussou = []
GI_vic = []
GII_vic = []
GIII_vic = []
otherjusyo_vic = []
jusyo_sum_vic = []
special_vic = []
sum_vic = []
GI_rentai = []
GII_rentai = []
GIII_rentai = []
otherjusyo_rentai = []
jusyo_sum_rentai = []
special_rentai = []
sum_rentai = []
first_temp = []
second_temp = []
third_temp = []
fourth_temp = []
syussou_temp = []
vic_temp = []
rentai_temp = []
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
                for race_result in soup.select(".dataLs.mgnBL > tr"):
                    first_temp.append(
                        race_result.select_one("td:nth-of-type(2)"))
                    second_temp.append(
                        race_result.select_one("td:nth-of-type(3)"))
                    third_temp.append(
                        race_result.select_one("td:nth-of-type(4)"))
                    fourth_temp.append(
                        race_result.select_one("td:nth-of-type(5)"))
                    syussou_temp.append(
                        race_result.select_one("td:nth-of-type(6)"))
                    vic_temp.append(
                        race_result.select_one("td:nth-of-type(7)"))
                    rentai_temp.append(
                        race_result.select_one("td:nth-of-type(8)"))
                time.sleep(3)
                GI_first.append(first_temp[1])
                GII_first.append(first_temp[2])
                GIII_first.append(first_temp[3])
                otherjusyo_first.append(first_temp[4])
                jusyo_sum_first.append(first_temp[5])
                special_first.append(first_temp[6])
                sum_first.append(first_temp[7])
                GI_second.append(second_temp[1])
                GII_second.append(second_temp[2])
                GIII_second.append(second_temp[3])
                otherjusyo_second.append(second_temp[4])
                jusyo_sum_second.append(second_temp[5])
                special_second.append(second_temp[6])
                sum_second.append(second_temp[7])
                GI_third.append(third_temp[1])
                GII_third.append(third_temp[2])
                GIII_third.append(third_temp[3])
                otherjusyo_third.append(third_temp[4])
                jusyo_sum_third.append(third_temp[5])
                special_third.append(third_temp[6])
                sum_third.append(third_temp[7])
                GI_fourth.append(fourth_temp[1])
                GII_fourth.append(fourth_temp[2])
                GIII_fourth.append(fourth_temp[3])
                otherjusyo_fourth.append(fourth_temp[4])
                jusyo_sum_fourth.append(fourth_temp[5])
                special_fourth.append(fourth_temp[6])
                sum_fourth.append(fourth_temp[7])
                GI_syussou.append(syussou_temp[1])
                GII_syussou.append(syussou_temp[2])
                GIII_syussou.append(syussou_temp[3])
                otherjusyo_syussou.append(syussou_temp[4])
                jusyo_sum_syussou.append(syussou_temp[5])
                special_syussou.append(syussou_temp[6])
                sum_syussou.append(syussou_temp[7])
                GI_vic.append(vic_temp[1])
                GII_vic.append(vic_temp[2])
                GIII_vic.append(vic_temp[3])
                otherjusyo_vic.append(vic_temp[4])
                jusyo_sum_vic.append(vic_temp[5])
                special_vic.append(vic_temp[6])
                sum_vic.append(vic_temp[7])
                GI_rentai.append(rentai_temp[1])
                GII_rentai.append(rentai_temp[2])
                GIII_rentai.append(rentai_temp[3])
                otherjusyo_rentai.append(rentai_temp[4])
                jusyo_sum_rentai.append(rentai_temp[5])
                special_rentai.append(rentai_temp[6])
                sum_rentai.append(rentai_temp[7])
                child.append(soup.find("h1", class_="fntB").get_text())
                first_temp = []
                second_temp = []
                third_temp = []
                fourth_temp = []
                syussou_temp = []
                vic_temp = []
                rentai_temp = []
            except:
                pass

# 同じなアガサじゃないとエクセルにできないので長さを表示
print(len(child))
print(len(GI_first))
print(len(GII_first))
print(len(GIII_first))
print(len(otherjusyo_first))
print(len(jusyo_sum_first))
print(len(special_first))
print(len(sum_first))
print(len(GI_second))
print(len(GII_second))
print(len(GIII_second))
print(len(otherjusyo_second))
print(len(jusyo_sum_second))
print(len(special_second))
print(len(sum_second))
print(len(GI_third))
print(len(GII_third))
print(len(GIII_third))
print(len(otherjusyo_third))
print(len(jusyo_sum_third))
print(len(special_third))
print(len(sum_third))
print(len(GI_fourth))
print(len(GII_fourth))
print(len(GIII_fourth))
print(len(otherjusyo_fourth))
print(len(jusyo_sum_fourth))
print(len(special_fourth))
print(len(sum_fourth))
print(len(GI_syussou))
print(len(GII_syussou))
print(len(GIII_syussou))
print(len(otherjusyo_syussou))
print(len(jusyo_sum_syussou))
print(len(special_syussou))
print(len(sum_syussou))
print(len(GI_vic))
print(len(GII_vic))
print(len(GIII_vic))
print(len(otherjusyo_vic))
print(len(jusyo_sum_vic))
print(len(special_vic))
print(len(sum_vic))
print(len(GI_rentai))
print(len(GII_rentai))
print(len(GIII_rentai))
print(len(otherjusyo_rentai))
print(len(jusyo_sum_rentai))
print(len(special_rentai))
print(len(sum_rentai))

race_num_data = pd.DataFrame(
    {"URL": horse_url_array,
     "馬名": child,
     "G1一着": GI_first,
     "G2一着": GII_first,
     "G3一着": GIII_first,
     "その他重賞一着": otherjusyo_first,
     "重賞一着合計": jusyo_sum_first,
     "特別一着": special_first,
     "一着合計": sum_first,
     "G1二着": GI_second,
     "G2二着": GII_second,
     "G3二着": GIII_second,
     "その他重賞二着": otherjusyo_second,
     "重賞二着合計": jusyo_sum_second,
     "特別二着": special_second,
     "合計二着": sum_second,
     "G1三着": GI_third,
     "G2三着": GII_third,
     "G3三着": GIII_third,
     "その他重賞三着": otherjusyo_third,
     "重賞三着合計": jusyo_sum_third,
     "特別三着": special_third,
     "三着合計": sum_third,
     "G1四着以下": GI_fourth,
     "G2四着以下": GII_fourth,
     "G3四着以下": GIII_fourth,
     "その他四着以下": otherjusyo_fourth,
     "その他重賞四着以下": jusyo_sum_fourth,
     "四着以下": special_fourth,
     "四着以下合計": sum_fourth,
     "G1出走数": GI_syussou,
     "G2出走数": GII_syussou,
     "G3出走数": GIII_syussou,
     "その他重賞出走数": otherjusyo_syussou,
     "重賞出走数合計": jusyo_sum_syussou,
     "特別出走数": special_syussou,
     "出走数合計": sum_syussou,
     "G1勝率": GI_vic,
     "G2勝率": GII_vic,
     "G3勝率": GIII_vic,
     "その他重賞勝率": otherjusyo_vic,
     "重賞勝率合計": jusyo_sum_vic,
     "特別勝率": special_vic,
     "勝率合計": sum_vic,
     "G1連対数": GI_rentai,
     "G2連対数": GII_rentai,
     "G3連対数": GIII_rentai,
     "その他重賞連対数": otherjusyo_rentai,
     "重賞連対数合計": jusyo_sum_rentai,
     "特別連対数": special_rentai,
     "連対数合計": sum_rentai}
)

# mode="a"で追記するモードに変換
with pd.ExcelWriter('./excel/成績.xlsx', mode='a') as writer:
    # ExcelWriterを用いて新規シートにDataFrameを保存
    race_num_data.to_excel(writer, sheet_name='2019_03_04', index=False)

# 自分用
notification.notify(title="デスクトップ通知", message="実行完了", timeout=5)
