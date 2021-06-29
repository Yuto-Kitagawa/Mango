import openpyxl as openpyxl
import numpy as np
import pandas as pd
import datetime


class Functions:
    def toNum(self, min_row, min_col, max_row, max_col):
        wb = openpyxl.load_workbook("./必要データ纏め.xlsx")
        sheet = wb["マスタデータレース一覧"]
        tenkou = []

        # 行単位でセルの値を取得
        for cols in sheet.iter_cols(min_col, max_col, min_row, max_row):
            for cell in cols:
                if cell.value == "晴":  # 晴れなら1,#曇りなら2,#その他3
                    sheet.cell(row=4, column=cols).value = 1
                    tenkou.append(1)
                elif cell.value == "雲":
                    tenkou.append(2)
                    sheet.cell(row=4, column=cols).value = 2
                else:
                    tenkou.append(3)
                    sheet.cell(row=4, column=cols).value = 3

        return tenkou

    def split_data(df,test_rate=0.3):
        sorted_id_list = df.sort_values('RACE_NUMBER').index.unique()
        train_id_list = sorted_id_list[:round(len(sorted_id_list)*(1-test_rate))]
        test_id_list = sorted_id_list[round(len(sorted_id_list)*(1-test_rate)):]
        train = df.loc([train_id_list])
        test = df.loc([test_id_list])
        return train,test
