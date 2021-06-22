import xlrd
import pprint
from pandas import Series, DataFrame
import pandas as pd
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from functions import Functions

class Main(Functions):
    tenkou = []
    functions = Functions()
    tenkou_array = functions.toArray(4, 2, 4, 100)
    print(tenkou_array)

    # エクセルの+Y.drop(drop_idx_y, axis=1)

    """ ここから下未完成"""

    # # 訓練用データ、評価用データに分割
    # x_train, x_test, y_train, y_test = split(
    #     df_X, df_Y, train_size=0.8, test_size=0.2)

    # # 教師あり学習の実行(ロジスティック回帰)
    # model = LogisticRegression()
    # model.fit(x_train, y_train)

    # # 評価の実行
    # y_pred = model.predict(x_test)

    # # plt.scatter(y_test, y_pred)
    # # 精度の計算
    # print(metrics.accuracy_score(y_test, y_pred))
