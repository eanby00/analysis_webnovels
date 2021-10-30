# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
import random
import time

# 기본 정보
file_name = "test.csv"
url = "https://novel.munpia.com/page/hd.platinum/group/pl.serial/exclusive/true/view/allend"

# 해당 url에서 데이터 가져오기
req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.text, "html.parser")

li_list_author = soup.select("#SECTION-LIST > ul a.author.col-xs-4")
li_list_title = soup.select("#SECTION-LIST > ul a.title.col-xs-6")

# 해당 데이터에서 string 부분만 가져오기
temp_author = []
temp_title = []
for i in range(len(li_list_author)):
    temp_author.append(li_list_author[i].string.strip())
    temp_title.append(li_list_title[i].string.strip())

# 시간차주기: 
rand_value = random.randint(1, 5)
time.sleep(rand_value)

# 해당 데이터들을 DataFrame으로 저장하고 csv로 저장
df = pd.DataFrame({"author":temp_author, "temp_title":temp_title})
df.to_csv(file_name, encoding="utf-8")

# vm내에 저장된 csv파일을 hdfs의 maria_dev 아래에 저장
hdfs_path = os.path.join(os.sep, "user", "maria_dev", file_name)
put = Popen(["hadoop", "fs", "-put", file_name, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()

## 참고출처
# vm내의 csv 파일을 hdfs로 전송: https://stackoverflow.com/questions/26606128/how-to-save-a-file-in-hadoop-with-python
# requests와 beautifulsoup4를 이용해 웹 크롤링하기: https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
# 크롤링 차단 방지
    # 크롤링 header 지정: https://blog.naver.com/kiddwannabe/221185808375
    # 크롤링에 시간차주기: https://advenoh.tistory.com/3