# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
from random import *
import time
import datetime

# 기본 정보
version_main = 1

# 초기화
url_charged = "https://novel.munpia.com/page/novelous/group/pl.serial/exclusive/1/gpage/"
url_free = ""
file_novel_list = "munpia_novel_list_"+str(version_main)+".csv"

## index
index_charged = 1
index_free = 1

## DataFrame 내부 데이터 - 작품 기본
author = [] # 작가
title = [] # 타이틀
link = [] # 작품 link
version = [] # 데이터를 수집한 version
source = [] # 문피아 유료인가? 문피아 무료인가?
ending = [] # 연재작품인가? 완결작품인가?

## DataFrame 내부 데이터 - 작품 상세
avg_serial_week = [] # 주당 평균 연재 횟수
serial_start = [] # 연재 시작 날짜
serial_last = [] # 최근 연재 날짜
period = [] # 일 기준의 연재 기간
serial_time = [] # 총 연재 횟수
view = [] # 조회 횟수
recommendation = [] # 추천 횟수
letter = [] # 글자 수
favorite = [] # 해당 작품을 선호하는 독자 인원

## index 체크용
prev_author_charged = ""
prev_title_charged = ""

prev_author_free = ""
prev_title_free = ""

# 연재 시작일과 최근 연재일을 이용한 기간 계산
def cal_period(start, last):
    last = list(map(int, last.split(" ")[0].split(".")))
    start = list(map(int, start.split(" ")[0].split(".")))
    last_time = datetime.datetime(last[0], last[1], last[2])
    start_time = datetime.datetime(start[0], start[1], start[2])
    return (last_time - start_time).days

# 문피아 유료 데이터 수집
while True:
    # 해당 url에서 데이터 가져오기
    req = requests.get(url_charged+str(index_charged), headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, "html.parser")
    li_list_author = soup.select("#SECTION-LIST > ul a.author.col-xs-4")
    li_list_title = soup.select("#SECTION-LIST > ul a.title.col-xs-6")

    # 테스팅용
    if index_charged == 2:
        break

    # while 탈출 조건: prev_author가 현재 페이지의 1번째 작가와 같고 prev_title이 1번째 작품과 같아야함
    if prev_author_charged == li_list_author[0].string.strip() and prev_title_charged == li_list_title[0].string.strip():
        print("completion", index_charged)
        break

    # 데이터 가져오기
    for i in range(len(li_list_author)):
        # 작품 데이터 가져오기
        author.append(li_list_author[i].string.strip())
        temp_title = li_list_title[i].string.strip()
        title.append(temp_title)
        link.append(li_list_title[i].get("href"))
        version.append(version_main)
        source.append("문피아_유료")
        ending.append("연재작")

        # 작품 상세 데이터 접근
        index_inner = 1
        url_inner = li_list_title[i].get("href")+"/page/"
        req_inner = requests.get(url_inner+str(index_inner), headers={'User-Agent': 'Mozilla/5.0'})
        soup_inner = BeautifulSoup(req_inner.text, "html.parser")

        # 작품 상세 데이터 가져오기
        nth = 6
        if soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(7) > dt:nth-child(1)").string == u"작품등록일 :":
            nth = 7
    
        avg_serial_week.append(float(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > div.novel-real-period > span").string.split(" ")[3])) 

        temp_start = soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(2)" % nth).string
        temp_last = soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(4)" % nth).string

        serial_start.append(temp_start) 
        serial_last.append(temp_last)
        period.append(cal_period(temp_start, temp_last))
        serial_time.append(int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(2)" % (nth + 1)).string.split(" ")[0].split(",")))) 
        view.append(int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(4)" % (nth + 1)).string.split(",")))) 
        recommendation.append(int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(6)" % (nth + 1)).string.split(",")))) 
        letter.append(int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(8)" % (nth + 1)).string.split(",")))) 
        favorite.append(int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > div.button-nav.housing > div.fr > a.button.novel.trigger-subscribe.require-login > span > b").string.string.split(",")))) 

        # 작품의 편당 데이터 가져오기


        # 진행률 체크
        print(index_charged, "progress:", i)

        # 시간차주기
        rand_value = random() * 2
        time.sleep(rand_value)

    # 기본 정보 변경
    print("progress:", index_charged, "done")
    index_charged += 1
    prev_author_charged = li_list_author[0].string.strip()
    prev_title_charged = li_list_title[0].string.strip()

# 해당 데이터들을 DataFrame으로 저장하고 csv로 저장
df_list = pd.DataFrame({
    "author":author,
    "title":title,
    "link":link,
    "version":version,
    "source":source,
    "ending": ending,
    "avg_serial_week":avg_serial_week,
    "serial_start": serial_start,
    "serial_last":serial_last,
    "period": period,
    "serial_time":serial_time,
    "view":view,
    "recommendation":recommendation,
    "letter":letter,
    "favorite":favorite})

df_list.to_csv(file_novel_list, encoding="utf-8", index_label="ID")

# vm내에 저장된 csv파일을 hdfs의 maria_dev/analysis_webnovels 아래에 저장
hdfs_path = os.path.join(os.sep, "user", "maria_dev", "analysis_webnovels", "novel_list", file_novel_list)

# 소설 리스트를 analysis_webnovels/novel_list에 저장
put = Popen(["hadoop", "fs", "-put", file_novel_list, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()

print("done")