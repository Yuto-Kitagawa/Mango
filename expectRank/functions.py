import openpyxl as openpyxl
import numpy as np

class Functions:
    def toArray(self,min_row, min_col, max_row, max_col):
        wb = openpyxl.load_workbook("./必要データ纏め.xlsx")
        sheet = wb["マスタデータレース一覧"]
        tenkou = []
        # print("ok")
        counter = 0
        # 行単位でセルの値を取得する A2～C5まで
        for cols in sheet.iter_cols(min_row, min_col, max_row, max_col):
            for cell in cols:
                print("ouou")
                tenkou.append(cell.value)
                print(cell.value)
        return tenkou

