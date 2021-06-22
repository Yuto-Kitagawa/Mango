import openpyxl as openpyxl
import numpy as np


class Functions:
    def toNum(self, min_row, min_col, max_row, max_col):
        wb = openpyxl.load_workbook("./必要データ纏め.xlsx")
        sheet = wb["マスタデータレース一覧"]
        tenkou = []

        # 行単位でセルの値を取得
        for cols in sheet.iter_cols(min_row, min_col, max_row, max_col):
            for cell in cols:
                if cell.value == "晴":  # 晴れなら1,#曇りなら2,#その他3
                    tenkou.append(1)
                elif cell.value == "雲":
                    tenkou.append(2)
                else:
                    tenkou.append(3)

        return tenkou
