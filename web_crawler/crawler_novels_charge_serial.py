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
file_novel_list = "munpia_novel_list_charge_serial_"+str(version_main)+".csv"
file_novel_unit_list = "munpia_novel_unit_list_charge_serial_"+str(version_main)+".csv"

## index
index_charged = 1
index_work = 0

## DataFrame 내부 데이터 - 작품 기본
id = [] # 작품 id, 해당 version에서만 의미가 있음 
author = [] # 작가
title = [] # 타이틀
link = [] # 작품 link
version = [] # 데이터를 수집한 version
source = [] # 문피아 유료인가? 문피아 무료인가?, 해당 코드에서는 모두 "문피아_유료"로 통일
ending = [] # 연재작품인가? 완결작품인가?, 해당 코드에서는 모두 "연재작"으로 통일

## DataFrame 내부 데이터 - 작품 상세
avg_serial_week = [] # 주당 평균 연재 횟수
serial_start = [] # 연재 시작 날짜
serial_last = [] # 최근 연재 날짜
serial_time = [] # 총 연재 횟수
view = [] # 조회 횟수
recommendation = [] # 추천 횟수
letter = [] # 글자 수
favorite = [] # 해당 작품을 선호하는 독자 인원

## 추가 데이터
period = [] # 일 기준의 연재 기간, 최근 연재 날짜 - 연재 시작 날짜
check_count = [] # 작품 당 기준 값 이상 감소한 편의 갯수, 해당 코드에서는 모두 0으로 통일

## index 체크용
prev_author_charged = ""
prev_title_charged = ""

# 편당 정보 데이터
main_id = [] # 작품의 id
inner_version = [] # 데이터를 수집한 version
inner_serial = [] # 해당 편의 편수
inner_charge = [] # 해당 편이 유료인지 무료인지, 무료_작품, 유료, 무료로 나뉘어짐
inner_sub_title = [] # 해당 편의 소제목
inner_count_comment = [] # 해당 편의 댓글 수
inner_date = [] # 해당 편의 연재 날짜
inner_purchase = [] # 해당 편의 구매량
inner_recommendation = [] # 해당 편의 추천량
inner_letter = [] # 해당 편의 글자수(정확히는 쪽수)
inner_target = [] # 해당 편이 분석의 대상인지, n 시간 전, n 분 전 등은 분석하기에 적합하지 않다고 판단

inner_rate_change_purchase = [] # 전 편에 대비해 얼마나 구매 데이터가 변했는지 확인

inner_rate_change_purchase_five = [] # 5 편 전에 대비해 구매 데이터가 얼마나 변했는지 확인
inner_rate_change_purchase_five_avg = [] # 5 편 전부터 구매 데이터 변화율의 평균

inner_rate_change_recommendation_five = [] # 5 편 전에 대비해 추천 데이터가 얼마나 변했는지 확인
inner_rate_change_recommendation_five_avg = [] # 5 편 전부터 추천 데이터 변화율의 평균

# 연재 시작일과 최근 연재일을 이용한 기간 계산
def cal_period(start, last):
    last = list(map(int, last.split(" ")[0].split(".")))
    start = list(map(int, start.split(" ")[0].split(".")))
    last_time = datetime.datetime(last[0], last[1], last[2])
    start_time = datetime.datetime(start[0], start[1], start[2])
    return (last_time - start_time).days

# ,가 포함된 string 타입의 숫자 데이터를 숫자로 변형 ex) 123,456 => 123456
def parseInt(num_string):
    return int("".join(num_string.split(",")))

# string에서 불필요한 글자를 제외하고 숫자 데이터로 변환
def parseIntremove(num_string):
    return int("".join(num_string.strip().replace(u"쪽", "").split(",")))

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
        id.append(index_work)
        author.append(li_list_author[i].string.strip())
        temp_title = li_list_title[i].string.strip()
        title.append(temp_title)
        link.append(li_list_title[i].get("href"))
        version.append(version_main)
        source.append("문피아_유료")
        ending.append("연재작")
        check_count.append(0)

        # 작품 상세 데이터 접근
        inner_index = 1
        url_inner = li_list_title[i].get("href")+"/page/"
        req_inner = requests.get(url_inner+str(inner_index), headers={'User-Agent': 'Mozilla/5.0'})
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
        serial_time.append(parseInt(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(2)" % (nth + 1)).string.split(" ")[0])) 
        view.append(parseInt(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(4)" % (nth + 1)).string)) 
        recommendation.append(parseInt(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(6)" % (nth + 1)).string)) 
        letter.append(parseInt(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(%d) > dd:nth-child(8)" % (nth + 1)).string)) 
        favorite.append(parseInt(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > div.button-nav.housing > div.fr > a.button.novel.trigger-subscribe.require-login > span > b").string)) 

        # 시간차주기
        rand_value = random() * 2
        time.sleep(rand_value)

        # 작품의 편당 데이터 가져오기
        inner_prev_serial = 0
        retry = 0
        while True:
            try:
                # 해당 url에서 데이터 가져오기
                req = requests.get(url_inner+str(inner_index), headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(req.text, "html.parser")
                temp_soup = soup.select("#ENTRIES > tbody > tr")
                

                # while 탈출 조건: prev_serial가 현재 페이지의 1번째 serial과 같아야 함
                if inner_prev_serial == temp_soup[0].select_one("td.index > span").string:
                    break

                for j in range(len(temp_soup)):
                    if temp_soup[j].select_one("td.index > span").string != u"공지":
                    # 작품 데이터 가져오기
                        main_id.append(index_work)
                        inner_version.append(version_main)
                        inner_serial.append(parseInt(temp_soup[j].select_one("td.index > span").string))

                        if temp_soup[j].select_one("td.subject > span.coin") == None:
                            inner_charge.append("무료_작품")
                        elif temp_soup[j].select_one("td.subject > span.coin.coin-free") == None:
                            inner_charge.append("유료")
                        else:
                            inner_charge.append("무료")

                        inner_sub_title.append(temp_soup[j].select("td.subject > a")[0].string)

                        if len(temp_soup[j].select("td.subject > a")) == 1:
                            inner_count_comment.append(0)
                        else:
                            inner_count_comment.append(parseInt(temp_soup[j].select("td.subject > a")[1].string.replace("+", ""))) # 댓글 수
                        
                        date = temp_soup[j].select_one("td.date").string 
                        flag_h = date.find(u"시간")
                        flag_m = date.find(u"분")
                        flag_s = date.find(u"초")
                        now = datetime.datetime.now()

                        if flag_h != -1 or flag_m != -1 or flag_s != -1:
                            inner_date.append(str(now.year)+"."+str(now.month)+"."+str(now.day))
                            inner_target.append(False)
                        else:
                            date_temp = date.split(".")
                            date_temp[0] = str(20) + date_temp[0]
                            inner_date.append(".".join(date_temp))
                            inner_target.append(True)

                        inner_purchase.append(parseInt(temp_soup[j].select_one("td:nth-of-type(5)").string))

                        inner_recommendation.append(parseInt(temp_soup[j].select_one("td:nth-of-type(6) span").string))
                        inner_letter.append(parseIntremove(temp_soup[j].select_one("td:nth-of-type(7)").string))

                        print(index_charged, "progress:", i, j)

                # 기본 정보 변경
                inner_index += 1
                inner_prev_serial = temp_soup[0].select_one("td.index > span").string

                # 시간차주기
                rand_value = random() * 2
                time.sleep(rand_value)
            except:
                time.sleep(randint(10, 15))
                print("retry", retry)
                retry += 1

        # 정보 변경
        index_work += 1

        # 진행률 체크
        print(index_charged, "progress:", i)

    # 기본 정보 변경
    print("progress:", index_charged, "done")
    index_charged += 1
    prev_author_charged = li_list_author[0].string.strip()
    prev_title_charged = li_list_title[0].string.strip()

    time.sleep(5)

# 편당 데이터 정리
main_id.reverse()
inner_version.reverse()
inner_serial.reverse()
inner_charge.reverse()
inner_sub_title.reverse()
inner_count_comment.reverse()
inner_date.reverse()
inner_purchase.reverse()
inner_recommendation.reverse()
inner_letter.reverse()
inner_target.reverse()

# 편당 데이터 추가
for index in range(len(inner_serial)):
    temp_rate_of_change = None

    now_purchase = float(inner_purchase[index])
    if index > 0:
        prev_purchase_1 = float(inner_purchase[index-1])
        temp_rate_of_change = (now_purchase - prev_purchase_1) / prev_purchase_1
    inner_rate_change_purchase.append(temp_rate_of_change)

    temp_rate_change_purchase_five = None
    temp_rate_change_purchase_five_avg = None
    temp_rate_change_recommendation_five = None
    temp_rate_change_recommendation_five_avg = None

    if index > 3:
        prev_purchase_1 = float(inner_purchase[index-1])
        prev_purchase_2 = float(inner_purchase[index-2])
        prev_purchase_3 = float(inner_purchase[index-3])
        prev_purchase_4 = float(inner_purchase[index-4])

        now_recommendation = float(inner_recommendation[index])
        prev_recommendation_1 = float(inner_recommendation[index-1])
        prev_recommendation_2 = float(inner_recommendation[index-2])
        prev_recommendation_3 = float(inner_recommendation[index-3])
        prev_recommendation_4 = float(inner_recommendation[index-4])

        temp_rate_change_purchase_five = (now_purchase - prev_purchase_4) / prev_purchase_4
        temp_rate_change_purchase_five_avg = ((now_purchase - prev_purchase_1) / prev_purchase_1 + (prev_purchase_1 - prev_purchase_2) / prev_purchase_2 + (prev_purchase_2 - prev_purchase_3) / prev_purchase_3 + (prev_purchase_3 - prev_purchase_4) / prev_purchase_4) / 4

        temp_rate_change_recommendation_five = (now_recommendation - prev_recommendation_4) / prev_recommendation_4
        temp_rate_change_recommendation_five_avg = ((now_recommendation - prev_recommendation_1) / prev_recommendation_1 + (prev_recommendation_1 - prev_recommendation_2) / prev_recommendation_2 + (prev_recommendation_2 - prev_recommendation_3) / prev_recommendation_3 + (prev_recommendation_3 - prev_recommendation_4) / prev_recommendation_4) / 4

    inner_rate_change_purchase_five.append(temp_rate_change_purchase_five)
    inner_rate_change_purchase_five_avg.append(temp_rate_change_purchase_five_avg)
    inner_rate_change_recommendation_five.append(temp_rate_change_recommendation_five)
    inner_rate_change_recommendation_five_avg.append(temp_rate_change_recommendation_five_avg)

# 편당 데이터를 data frame으로 저장
df_inner_list = pd.DataFrame({
    "book_id":main_id,
    "version":inner_version,
    "serial":inner_serial,
    "charge":inner_charge,
    "sub_title":inner_sub_title,
    "count_comment": inner_count_comment,
    "date":inner_date,
    "purchase": inner_purchase,
    "recommendation":inner_recommendation,
    "letter": inner_letter,
    "target": inner_target,
    "rate_change_purchase": inner_rate_change_purchase,
    "rate_change_purchase_five": inner_rate_change_purchase_five,
    "rate_change_purchase_five_avg": inner_rate_change_purchase_five_avg,
    "rate_change_recommendation_five": inner_rate_change_recommendation_five,
    "rate_change_recommendation_five_avg": inner_rate_change_recommendation_five_avg})

# 편당 데이터 프레임을 csv로 저장
df_inner_list.to_csv(file_novel_unit_list, encoding="utf-8", index_label= "unit_id")

# 해당 데이터들을 DataFrame으로 저장
df_list = pd.DataFrame({
    "id":id,
    "author":author,
    "title":title,
    "link":link,
    "version":version,
    "source":source,
    "ending": ending,
    "check_count":check_count,
    "avg_serial_week":avg_serial_week,
    "serial_start": serial_start,
    "serial_last":serial_last,
    "period": period,
    "serial_time":serial_time,
    "view":view,
    "recommendation":recommendation,
    "letter":letter,
    "favorite":favorite})

# 데이터프레임에 추가 데이터 삽입
# view_per_date 하루별 평균 조회수, view / period
# recommendation_per_date 하루별 평균 추천수, recommendation / period
# letter_per_date 하루별 평균 글자수, letter / period
# favorite_per_date 하루별 평균 선호자수, favorite / period
# 
# view_per_serial 편당 평균 조회수, view / serial_time
# recommendation_per_serial 편당 평균 조회수, recommendation / serial_time
# letter_per_serial 편당 평균 조회수, letter / serial_time
# favorite_per_serial 편당 평균 조회수, favorite / serial_time

df_list["view_per_date"] = df_list["view"] / df_list["period"]
df_list["recommendation_per_date"] = df_list["recommendation"] / df_list["period"]
df_list["letter_per_date"] = df_list["letter"] / df_list["period"]
df_list["favorite_per_date"] = df_list["favorite"] / df_list["period"]

df_list["view_per_serial"] = df_list["view"] / df_list["serial_time"]
df_list["recommendation_per_serial"] = df_list["recommendation"] / df_list["serial_time"]
df_list["letter_per_serial"] = df_list["letter"] / df_list["serial_time"]
df_list["favorite_per_serial"] = df_list["favorite"] / df_list["serial_time"]

# 데이터프레임 csv로 저장
df_list.to_csv(file_novel_list, encoding="utf-8", index=None)

# vm내에 저장된 csv파일을 hdfs의 maria_dev/analysis_webnovels 아래에 저장
hdfs_path = os.path.join(os.sep, "user", "maria_dev", "analysis_webnovels", "novel_list", file_novel_list)
hdfs_path_unit = os.path.join(os.sep, "user", "maria_dev", "analysis_webnovels", "novel_unit_list", file_novel_list)

# 소설 리스트를 analysis_webnovels/novel_list에 저장
put = Popen(["hadoop", "fs", "-put", file_novel_list, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()

put_unit = Popen(["hadoop", "fs", "-put", file_novel_list, hdfs_path_unit], stdin=PIPE, bufsize=-1)
put_unit.communicate()

print("done")