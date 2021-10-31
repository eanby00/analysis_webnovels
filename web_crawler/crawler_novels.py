# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
import random
import time

# 기본 정보
version = 1

# 초기화
url_charged = "https://novel.munpia.com/page/novelous/group/pl.serial/exclusive/1/gpage/"
url_free = ""
file_novel_list = "munpia_novel_list_"+str(version)+".csv"

index_charged = 1
index_free = 1
temp_author = []
temp_title = []
temp_link = []
temp_version = []
temp_source = []

prev_author_charged = ""
prev_title_charged = ""

prev_author_free = ""
prev_title_free = ""

# 문피아 유료 데이터 수집
while True:
    # 해당 url에서 데이터 가져오기
    req = requests.get(url_charged+str(index_charged), headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, "html.parser")
    li_list_author = soup.select("#SECTION-LIST > ul a.author.col-xs-4")
    li_list_title = soup.select("#SECTION-LIST > ul a.title.col-xs-6")

    # while 탈출 조건: prev_author가 현재 페이지의 1번째 작가와 같고 prev_title이 1번째 작품과 같아야함
    if prev_author_charged == li_list_author[0].string.strip() and prev_title_charged == li_list_title[0].string.strip():
        print("completion", index_charged)
        break

    # 해당 데이터에서 string 부분만 가져오기
    for i in range(len(li_list_author)):
        temp_author.append(li_list_author[i].string.strip())
        temp_title.append(li_list_title[i].string.strip())
        temp_link.append(li_list_title[i].get("href"))
        temp_version.append(version)
        temp_source.append("문피아_유료")

    # 시간차주기
    rand_value = random.randint(1, 5)
    # print("rand_value:", rand_value)
    time.sleep(rand_value)

    # 기본 정보 변경
    print("progress:", index_charged)
    index_charged += 1
    prev_author_charged = li_list_author[0].string.strip()
    prev_title_charged = li_list_title[0].string.strip()

# 해당 데이터들을 DataFrame으로 저장하고 csv로 저장
df_list = pd.DataFrame({"author":temp_author, "title":temp_title, "link":temp_link, "version":temp_version, "source":temp_source})
df_list.to_csv(file_novel_list, encoding="utf-8", index_label="ID")

# vm내에 저장된 csv파일을 hdfs의 maria_dev/analysis_webnovels 아래에 저장
hdfs_path = os.path.join(os.sep, "user", "maria_dev", "analysis_webnovels", "novel_list", file_novel_list)

# 소설 리스트를 analysis_webnovels/novel_list에 저장
put = Popen(["hadoop", "fs", "-put", file_novel_list, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()