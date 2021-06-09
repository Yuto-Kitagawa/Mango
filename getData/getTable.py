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
url = "https://keiba.yahoo.co.jp/directory/horse/2015100635/"
response = requests.get(url=url)
soup = BeautifulSoup(response.content, 'lxml')

for father_list in soup.select("#dirUmaBlood > tr "):
    father.append(father_list.select_one("td:nth-of-type(1)"))
print(father[0].text)
for mother_list in soup.select("#dirUmaBlood > tr"):
    mother.append(mother_list.select_one("td:nth-of-type(1)"))
print(mother[4].text)


