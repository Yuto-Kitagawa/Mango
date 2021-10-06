from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd
from jupyterthemes import jtplot

import MySQLdb
import csv

import numpy as np
from numpy import mean
from numpy import ndarray
from numpy import std

np.set_printoptions(threshold=np.inf)
# 以下ランダムフォレスト仕様のためのモジュールをインストール
# https://qiita.com/Hawaii/items/5831e667723b66b46fba 参照
# from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as split


# https://www.youtube.com/watch?v=yrnzv9wP10c 参照

# excelデータの取り込み
df_RaceOder = pd.read_excel("./race_order_1.xlsx")

# df_Orderのコピー
result_p = df_RaceOder.copy()
result_p = result_p.drop(
    ["RACE_NUMBER",  "ADD_WEIGHT", "MARGIN", "FRAME_NUMBER", "HORSE_NUMBER", "ENDUP", "HORSE_AGE", "HORSE_WEIGHT", "H_WEIGHT_INDECREASE"], axis=1)
# result_pをCSV化
result_p.to_csv('csv-data2.csv', encoding='utf-8-sig')


# ---データの整理---
# 着順に数字以外(着順：中止など)を取り除く
result_p = result_p[~(
    result_p['RACEORDER_NUMBER'].astype(str).str.contains('\D'))]
result_p['RACEORDER_NUMBER'] = result_p['RACEORDER_NUMBER'].astype(int)


# 1~3着まではそれの通り、4着以降はすべて4にする
def clip_rank(x): return x if x < 4 else 4


result_p['rank'] = result_p['RACEORDER_NUMBER'].map(clip_rank)
# result_p.to_excel("./samp.xlsx",index=False)

# 確認
# print(result_p['rank'].value_counts())

"""
# ValueError: could not convert string to float:エラーの回避策
result_p['騎手'] = result_p['騎手'].astype(object)
# print(type(result_p))

result_p['騎手'] = result_p['騎手'].replace('','"')

result_d = pd.get_dummies(result_p)

# result_d.to_excel("./samp.xlsx",index=False)

"""

result_d = pd.get_dummies(result_p)

# ロジステック回帰

X = result_d.drop(['rank'], axis=1)
y = result_d['rank']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.3, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)


# 正答率確認(79%だが、過学習の可能性あり)
# print(model.score(X_train,y_train),model.score(X_test,y_test))


y_pred = model.predict(X_test)

# print(y_train.value_counts())

# 過学習の改善策
# アンダーサンプリング

# print(result_p['RACEORDER_NUMBER'].value_counts())

rank_1 = y_train.value_counts()[1]
rank_2 = y_train.value_counts()[2]
rank_3 = y_train.value_counts()[3]

strategy = {1: rank_1, 2: rank_2, 3: rank_3,
            4: rank_1}  # 4データの数を1,2,3と同じくらいにする
rus = RandomUnderSampler(random_state=71, sampling_strategy=strategy)
X_train_rus, y_train_rus = rus.fit_resample(X_train, y_train)

# print(pd.Series(y_train_rus).value_counts())


# アンダーサンプリングしたデータを用いて
model = LogisticRegression()
model.fit(X_train_rus, y_train_rus)


# 正答率確認
print(model.score(X_train, y_train), model.score(X_test, y_test))


y_pred = model.predict(X_test)

pred_df = pd.DataFrame({'pred': y_pred, 'actual': y_test})  # データの数が違うからエラー


# 予測した項目確認(係数がマイナス程負けやすく、プラス程勝ちやすい)
# print(pd.Series(model.coef_[0],index=X.columns).sort_values())

# 項目取り出し
result = pd.Series(model.coef_[0], index=X.columns).sort_values(
    ascending=False)
print(result)

result_index = result.index.values
result_value = result.values


result_value_array = str(result_index).split()
result_value_array.pop(0)


# 項目のみ取り出し、r_indexに格納

# conn = MySQLdb.connect(
#     user='root',
#     passwd='',
#     host='localhost',
#     db='mango',
#     charset="utf8")

# cur = conn.cursor()
# sql = "TRUNCATE `mango`.`temp`;ALTER TABLE temp AUTO_INCREMENT = 1;"
# cur.execute(sql)
# for index in result_index:
#     sql += "INSERT INTO mango.`temp` (data) VALUE ('" + str(index) + "');"
    
# cur.execute(sql)
# cur.close()
# conn.commit()
# conn.close()


# #r_indexをcsv化で確認
# with open("resultlist.csv","w",encoding="Shift_jis") as f:
#     writer = csv.writer(f, lineterminator = "\n")
#     writer.writerows(r_index)

# result_list = result.values.tolist()

# print(result_list)

# 項目を元に勝ちやすい騎手の取り出し(未完成)

# result_list.to_csv('result-data2.csv',encoding='utf-8-sig')


"""
# 勝ちやすい騎手の詳細確認
print(result_p[result_p['騎手']=='C.ルメール'])#指定騎手のデータ表示
print(result_p[result_p['騎手']=='C.ルメール']
      ['rank'].value_counts()) #何着でゴールしたことがるかの回数
# 負けやすい　〃
print(result_p[result_p['騎手']=='M.デムーロ'])#指定騎手のデータ表示
print(result_p[result_p['騎手']=='M.デムーロ']['rank'].value_counts())


"""


# print(result)

"""
# 確認用(どの項目を参考にしているか(マイナス程参考にしている))
coefs = pd.Series(model.coef_[0], index=X.columns).sort_values()
print(coefs[['連番', 'コースの距離', '着順', '馬番', 'date', 'tyaku']])
"""
