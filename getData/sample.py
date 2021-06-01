from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import pandas as pd
import numpy as np

name_array = ["a","b","c","d","e"]
name_col = ["堺田","きたがわ","釜賀","森本","アンデュー"]


print(name_array)

df = pd.DataFrame(
    {'名前': name_array,"名前のやーつ":name_col })
df.to_excel('./Name.xlsx',header=False,index=None)

