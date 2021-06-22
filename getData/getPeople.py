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

url = ['https://db.netkeiba.com/?pid=sire_leading&year=2020&page=1', 'https://db.netkeiba.com/?pid=sire_leading&year=2020&page=2',
       'https://db.netkeiba.com/?pid=sire_leading&year=2020&page=3', 'https://db.netkeiba.com/?pid=sire_leading&year=2020&page=4', 'https://db.netkeiba.com/?pid=sire_leading&year=2020&page=5']

syussou_array = []
syouritu_array = []
EI_array = []
child = []

for number in url:
    response = requests.get(url=number)
    soup = BeautifulSoup(response.content, 'lxml')
    try:
        for getname in soup.select(".nk_tb_common.race_table_01 > tr"):
            child.append(getname.select_one("td:nth-of-type(2) > a"))
            syussou_array.append(getname.select_one("td:nth-of-type(5)"))
            syouritu_array.append(getname.select_one("td:nth-of-type(17)"))
            EI_array.append(getname.select_one("td:nth-of-type(18)"))
    except:
        import traceback
        traceback.print_exc()
        pass

people_detail = pd.DataFrame(
    {"馬名": child, "出走回数": syussou_array, "勝率": syouritu_array, "EI": EI_array})

#mode=wで新規作成モード
with pd.ExcelWriter('.\excel\p.xlsx', mode='w') as writer:
    people_detail.to_excel(writer, sheet_name="種馬", index=None)
# 自分用
notification.notify(title="デスクトップ通知", message="実行完了", timeout=5)
