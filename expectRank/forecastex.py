import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
# もう一つのクラスファイルのclass Functionsを継承のためにインストール
from functions import Functions
# ランダムフォレスト仕様のためのモジュールをインストール
# https://qiita.com/Hawaii/items/5831e667723b66b46fba 参照
from sklearn.ensemble import RandomForestClassifier  # ランダムフォレスト


class Main(Functions):
    # Functionsのクラスのインスタンス生成
    functions = Functions()

    # https://www.youtube.com/watch?v=yrnzv9wP10c 参照

    # RACE用DataFrame
    df_Race = pd.read_excel("./必要データ纏め.xlsx", sheet_name="RACE")
    idx_race = ["RACE_NAME"]
    df_Race = df_Race.drop(idx_race, axis=1)
    #エクセルにエクスポート
    # df_Race.to_excel("./sample.xlsx", index=None)

    # RACEORDER用DataFrame
    df_RaceOder = pd.read_excel("./必要データ纏め.xlsx", sheet_name="RACEORDER")
    def cf(x): return 1 if x in [1] else 0
    df_RaceOder["1着"] = df_RaceOder["RACEORDER_NUMBER"].map(cf)

    def cf2(x): return 1 if x in [2] else 0
    df_RaceOder["2着"] = df_RaceOder["RACEORDER_NUMBER"].map(cf2)

    def cf3(x): return 1 if x in [3] else 0
    df_RaceOder["3着"] = df_RaceOder["RACEORDER_NUMBER"].map(cf3)

    def cf3(x): return 1 if x in [1, 2, 3] else 0
    df_RaceOder["3着以内"] = df_RaceOder["RACEORDER_NUMBER"].map(cf3)

    print(df_RaceOder['3着以内'].value_counts())
    # df_RaceOder.to_excel("./sample.xlsx", index=None)

    train,test = functions.split_data(df_RaceOder)

    # 訓練用データ、評価用データに分割
    # x_train, x_test, y_train, y_test = split(
    #     df_X, df_Y, train_size=0.8, test_size=0.2)

# """ロジスティック回帰ではない"""
# # 教師あり学習の実行(ロジスティック回帰)
# # model = LogisticRegression()
# # model.fit(x_train, y_train)

# """ランダムフォレストを使用"""
# # ランダムフォレスト
# model = RandomForestClassifier(random_state=1234)
# model.fit(x_train, y_train)

# print("score=", model.score(x_test, y_test))

# # 評価の実行
# #y_pred = model.predict(x_test)

# #plt.scatter(y_test, y_pred)
# # 精度の計算
# #print(metrics.accuracy_score(y_test, y_pred))
