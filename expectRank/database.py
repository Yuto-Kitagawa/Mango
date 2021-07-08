# coding: UTF-8
import os
import re
import requests
import pandas as pd
import numpy as np
import MySQLdb
from plyer import notification

# select user, host from mysql.user;(データベースはmysql)でユーザとhostを確認できる
conn = MySQLdb.connect(
    user='root',
    passwd='',
    host='localhost',
    db='sample')

# カーソルを取得する
cur = conn.cursor()

# SQL（データベースを操作するコマンド）を実行する
# userテーブルから、HostとUser列を取り出す
sql = "select race_number from raceorder where raceorder_number = 1"
cur.execute(sql)

#実行結果を取得
rows = cur.fetchall()

for result in rows:
    print(result)


notification.notify(title="通知完了", message="Hello World", timeout=5)
