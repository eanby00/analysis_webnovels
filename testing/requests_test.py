# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
import random
import time

# 만약 존재하지 않는 link에 접속하려고 할 때 어떤 반응일까?

# 기본 정보
file_name = "test.csv"
url = "https://novel.munpia.com/page/novelous/group/pl.serial/exclusive/1/gpage/16"

# 해당 url에서 데이터 가져오기
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.text, "html.parser")

li_list_author = soup.select("#SECTION-LIST > ul a.author.col-xs-4")
li_list_title = soup.select("#SECTION-LIST > ul a.title.col-xs-6")

# 해당 데이터에서 string 부분만 가져오기
for i in range(len(li_list_author)):
    print(li_list_author[i].string.strip())
    print(li_list_title[i].string.strip())
    print(li_list_title[i].get("href"))
