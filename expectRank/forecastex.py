import xlrd
import pprint

from pandas import Series, DataFrame
import pandas as pd

#エクセルの入力ファイル名、シート名指定
#df = pd.read_excel('./必要データ纏め.xlsx',sheet_name='Sheet1')
df = pd.read_excel('./必要データ纏め.xlsx')
df.head()

a = df.head()
print(a)

df_X = df.copy()
df_Y = df.copy()

#説明変数の格納
#x = df[:, 1:3]
#print(df)