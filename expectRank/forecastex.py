import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd
from jupyterthemes import jtplot
import openpyxl
# 表を表示するためのパッケージ
from pandas.plotting import scatter_matrix
import matplotlib as pyplot

from numpy import mean
from numpy import std
# もう一つのクラスファイルのclass Functionsを継承のためにインストール
from functions import Functions
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


class Main(Functions):
    # Functionsのクラスのインスタンス生成
    functions = Functions()

    # RACE用DataFrame
    df_Race = pd.read_excel("./必要データ纏め.xlsx", sheet_name="RACE")
    idx_race = ["RACE_NAME"]
    df_Race = df_Race.drop(idx_race, axis=1)

    # RACEORDER用DataFrame
    df_RaceOder = pd.read_excel("./必要データ纏め.xlsx", sheet_name="マスタデータレース一覧")
    df_RaceOder = df_RaceOder.drop(
        ["日付", "レース名", "馬名", "騎手", "調教師", "発走時間", "コースの状態", "タイム", "天気", "コースの詳細", "枠", "推定上り", "着差", "レースの各位", "年齢", "コーナー通過", "着順"], axis=1)

    # df_Orderのコピー
    result_p = df_RaceOder.copy()

    # 0~3着まではそれの通り、4着以降はすべて4にする
    # 0は取消、除外を表す
    result_p['着順'] = result_p['tyaku'].map(lambda x: x if x < 4 else 4)
    # 予想するには0か1出ないといけないので1-3を1、それ以外を0にする
    result_p['rank'] = result_p['着順'].map(lambda x: 1 if x in [1, 2, 3] else 0)
    # 振り分けをしたので元データを削除
    result_p = result_p.drop(['着順', 'tyaku'], axis=1)
    result_p = result_p.drop(["weather", "race_type", "gender"], axis=1)

    train, test = functions.split_data(result_p)
    X_train = train.drop(["rank", 'date'], axis=1)
    y_train = train["rank"]
    X_test = test.drop(["rank", 'date'], axis=1)
    y_test = test["rank"]

    X_train.to_excel("./sample.xlsx", index=False)
    # # ランダムフィレストの始まり
    model = RandomForestClassifier()

    #モデルの評価
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    #予想
    n_scores = cross_val_score(
        model, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

