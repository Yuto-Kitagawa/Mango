#from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

import xlrd
import pprint

#マスターデータ用
df = pd.read_excel('./必要データ纏め.xlsx')

df_X = df.copy()
df_Y = df.copy()

# 説明変数の格納
drop_idx_x = ['URL', '着順']
# drop_idx_xの配列の項目を排除
df_X = df_X.drop(drop_idx_x, axis=1)

# 不要な列の削除
drop_idx_y = ['URL', '日付', 'レース名', '天気', '発走時間', 'コースの距離', 'コースの詳細', 'コースの状態', 'レースの各位',
                '枠', '馬番', '馬名', '斤量', '年齢', '騎手', 'タイム', '推定上り', '体重', '調教師', '着差', 'コーナー通過', '連番']
# drop_idx_yの項目を排除
df_Y = df_Y.drop(drop_idx_y, axis=1)


cf = lambda  x: 1 if x in[1,2,3] else 0
df['3着以内'] = df['着順'].map(cf)
print (df)
#df.to_excel("./data1.xlsx", index = None)


#もう一回！
dfRace = pd.read_excel('./必要データ纏め.xlsx', sheet_name = 'RACE')

dfRace_X = dfRace.copy()
dfRace_Y = dfRace.copy()

#print(dfRace_X)



dropRace_x = ['RACE_NAME','RACE_DATE']
dfRace_X = dfRace_X.drop(dropRace_x, axis=1)

#print(dfRace_X)

dfRace = pd.get_dummies(dfRace,columns = ['RACE_GRADE'])
dfRace = pd.get_dummies(dfRace,columns = ['HORSEBACK_STATUS'])
print(dfRace)


#dfRace.to_excel("./test2.xlsx", index = None)
