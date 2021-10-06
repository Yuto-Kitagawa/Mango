import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd
from jupyterthemes import jtplot
#表を表示するためのパッケージ
from pandas.plotting import scatter_matrix
import matplotlib as pyplot

from numpy import mean
from numpy import std
# もう一つのクラスファイルのclass Functionsを継承のためにインストール
#from functions import Functions
# 以下ランダムフォレスト仕様のためのモジュールをインストール
# https://qiita.com/Hawaii/items/5831e667723b66b46fba 参照
# from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier  # ランダムフォレスト
from sklearn.model_selection import train_test_split as split
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold



# https://www.youtube.com/watch?v=yrnzv9wP10c 参照
#scatter_matrix()
#pyplot.show()


# RACEORDER用DataFrame
df_RaceOder = pd.read_excel("./必要データ纏め.xlsx", sheet_name="マスタデータレース一覧")
# df_Orderのコピー
result_p = df_RaceOder.copy()
result_p = result_p.drop(
    ["日付", "レース名", "馬名","発走時間", "コースの状態","天気", "コースの詳細", "枠", "推定上り", "着差", "レースの各位", "年齢", "コーナー通過","weather","race_type","gender","age","weight_change","waku","斤量","体重"], axis=1)
#result_pをCSV化
result_p.to_csv('csv-data.csv',encoding='utf-8-sig')



#着順に数字以外(着順：中止など)を取り除く
result_p = result_p[~(result_p['着順'].astype(str).str.contains('\D'))]
result_p['着順'] = result_p['着順'].astype(int)


#1~3着まではそれの通り、4着以降はすべて4にする
clip_rank = lambda x: x if x < 4 else 4
result_p['rank'] = result_p['着順'].map(clip_rank)
result_p.to_excel("./samp.xlsx",index=False)

#確認
#print(result_p['rank'].value_counts())


#ValueError: could not convert string to float:エラーの回避策
result_p['騎手'] = result_p['騎手'].astype(object)
#print(type(result_p))

result_p['騎手'] = result_p['騎手'].replace('','"')

result_d = pd.get_dummies(result_p)

#result_d.to_excel("./samp.xlsx",index=False)


#ロジステック回帰
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = result_d.drop(['rank'],axis=1)
y = result_d['rank']

X_train,X_test,y_train,y_test = train_test_split(X,y, stratify=y, test_size = 0.3, random_state = 0)

model = LogisticRegression()
model.fit(X_train,y_train)


#正答率確認
#print(model.score(X_train,y_train),model.score(X_test,y_test))


y_pred = model.predict(X_test)

#print(y_train.value_counts())


#アンダーサンプリング
from imblearn.under_sampling import RandomUnderSampler

#print(result_p['tyaku'].value_counts())

rank_1 = y_train.value_counts()[1]
rank_2 = y_train.value_counts()[2]
rank_3 = y_train.value_counts()[3]

strategy = {1:rank_1, 2:rank_2, 3:rank_3, 4:rank_1}  #4データの数を1,2,3と同じくらいにする
rus = RandomUnderSampler(random_state=71, sampling_strategy = strategy)
X_train_rus,y_train_rus = rus.fit_resample(X_train,y_train)

#print(pd.Series(y_train_rus).value_counts())


#アンダーサンプリングしたデータを用いて
model = LogisticRegression()
model.fit(X_train_rus,y_train_rus)


#正答率確認
print(model.score(X_train,y_train),model.score(X_test,y_test))


y_pred = model.predict(X_test)

pred_df = pd.DataFrame({'pred':y_pred, 'actual':y_test}) #データの数が違うからエラー


#予測した項目確認(係数がマイナス程負けやすく、プラス程勝ちやすい)
print(pd.Series(model.coef_[0],index=X.columns).sort_values())


#勝ちやすい騎手の詳細確認
print(result_p[result_p['騎手']=='C.ルメール'])#指定騎手のデータ表示
print(result_p[result_p['騎手']=='C.ルメール']['rank'].value_counts()) #何着でゴールしたことがるかの回数
#負けやすい　〃
print(result_p[result_p['騎手']=='M.デムーロ'])#指定騎手のデータ表示
print(result_p[result_p['騎手']=='M.デムーロ']['rank'].value_counts())


"""
#確認用(どの項目を参考にしているか(マイナス程参考にしている))
coefs = pd.Series(model.coef_[0], index=X.columns).sort_values()
print(coefs[['連番', 'コースの距離', '着順', '馬番', 'date', 'tyaku']])
"""