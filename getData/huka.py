import pandas as pd

count = 1
count_array = []
while(True):
    try:
        count_array.append(count)
        count *= 2
    except:
        exit()
df = pd.DataFrame(
    {'負荷レベル': count_array})
df.to_excel("負荷テスト.xlsx", index=False)
