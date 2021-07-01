import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd

# もう一つのクラスファイルのclass Functionsを継承のためにインストール
from functions import Functions
# 以下ランダムフォレスト仕様のためのモジュールをインストール
# https://qiita.com/Hawaii/items/5831e667723b66b46fba 参照
# from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier  # ランダムフォレスト
from sklearn.model_selection import train_test_split as split
from sklearn.metrics import roc_curve, roc_auc_score
from jupyterthemes import jtplot
import matplotlib as plt


class Main(Functions):
    # Functionsのクラスのインスタンス生成
    functions = Functions()

    # https://www.youtube.com/watch?v=yrnzv9wP10c 参照

    # RACE用DataFrame
    df_Race = pd.read_excel("./必要データ纏め.xlsx", sheet_name="RACE")
    idx_race = ["RACE_NAME"]
    df_Race = df_Race.drop(idx_race, axis=1)
    # エクセルにエクスポート
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
    df_RaceOder.to_excel("./sample.xlsx", index=None)

    #文字のデータをdrop
    df_RaceOder.drop(["HORSE_NAME"], axis=1, inplace=True)
    df_RaceOder.drop(["RACE_TIME"], axis=1, inplace=True)
    df_RaceOder.drop(["MARGIN"], axis=1, inplace=True)
    df_RaceOder.drop(["FRAME_NUMBER"], axis=1, inplace=True)
    df_RaceOder.drop(["JOCKEY_NUMBER"],axis=1,inplace=True)

    # データを0.3に分ける
    # 訓練用データ、評価用データに分割
    # Functoinのsplit_data関数を実行
    train, test = functions.split_data(df_RaceOder)


    X_train = train.drop(["RACEORDER_NUMBER"], axis=1)
    y_train = train["RACEORDER_NUMBER"]
    X_test = test.drop(["RACEORDER_NUMBER"], axis=1)
    y_test = test["RACEORDER_NUMBER"]
    X_train.to_excel("sample.xlsx",index=None)

    print(X_train)
    print(y_train)

    # ランダムフィレストの始まり
    model = RandomForestClassifier(random_state=100)
    model.fit(X_train, y_train)
    
    y_pred = model.predict_proba(X_test)
    print(y_pred)
    # jtplotstyle(theme='monokai')

    fpr, tpr, thresholds = roc_curve(y_test, y_pred)
    plt.plot(fpr,tpr,marker='o')
    plt.xlabel('False positive rate')
    plt.ylabel('True positive rate')
    plt.grid()
    plt.show()


# """ロジスティック回帰ではない"""
# # 教師あり学習の実行(ロジスティック回帰)
# # model = LogisticRegression()
# # model.fit(x_train, y_train)
