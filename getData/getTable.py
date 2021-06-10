from bs4 import BeautifulSoup
import os
import re
import requests
import time
import datetime
import pandas as pd
import numpy as np

father = []
mother = []
parents_whole = []
parents_list = []
url = "https://keiba.yahoo.co.jp/directory/horse/2015100635/"
response = requests.get(url=url)
soup = BeautifulSoup(response.content, 'lxml')

for parents_list in soup.select("#dirUmaBlood > tr "):
    parents_whole.append(parents_list.select_one("td:nth-of-type(1)"))
father.append(parents_whole[0].text)
mother.append(parents_whole[4].text)
print("father:")
print(father)
print("mother:")
print(mother)
