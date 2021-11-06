# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
from random import *
import time
import datetime

def parseInt(num_string):
    return int("".join(num_string.split(",")))

def parseIntremove(num_string):
    return int("".join(num_string.strip().replace(u"쪽", "").split(",")))

# 기본 정보
version_main = 1

# 초기화
url_inner = "https://novel.munpia.com/290376/page/"
inner_index = 1
id = 0
main_id = []
inner_version = []
inner_serial = []
inner_charge = []
inner_sub_title = []
inner_count_comment = []
inner_date = []
inner_purchase = []
inner_recommendation = []
inner_letter = []
inner_target = []

inner_rate_change_purchase = []

inner_rate_change_purchase_five = []
inner_rate_change_purchase_five_avg = []

inner_rate_change_recommendation_five = []
inner_rate_change_recommendation_five_avg = []

inner_prev_serial = 0

while True:
    # 해당 url에서 데이터 가져오기
    req = requests.get(url_inner+str(inner_index), headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.text, "html.parser")
    temp_soup = soup.select("#ENTRIES > tbody > tr")
    

    # while 탈출 조건: prev_serial가 현재 페이지의 1번째 serial과 같아야 함
    if inner_prev_serial == temp_soup[0].select_one("td.index > span").string:
        print("completion", inner_index)
        break

    # 데이터 가져오기
    for i in range(len(temp_soup)):
        if temp_soup[i].select_one("td.index > span").string != u"공지":
        # 작품 데이터 가져오기
            main_id.append(id)
            inner_version.append(version_main)
            inner_serial.append(parseInt(temp_soup[i].select_one("td.index > span").string))

            if temp_soup[i].select_one("td.subject > span.coin") == None:
                inner_charge.append("무료_작품")
            elif temp_soup[i].select_one("td.subject > span.coin.coin-free") == None:
                inner_charge.append("유료")
            else:
                inner_charge.append("무료")

            inner_sub_title.append(temp_soup[i].select("td.subject > a")[0].string)

            if len(temp_soup[i].select("td.subject > a")) == 1:
                inner_count_comment.append(0)
            else:
                inner_count_comment.append(int(temp_soup[i].select("td.subject > a")[1].string.replace("+", ""))) # 댓글 수
            
            date = temp_soup[i].select_one("td.date").string 
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

            inner_purchase.append(parseInt(temp_soup[i].select_one("td:nth-of-type(5)").string))
            inner_recommendation.append(parseInt(temp_soup[i].select_one("td:nth-of-type(6) span").string))
            inner_letter.append(parseIntremove(temp_soup[i].select_one("td:nth-of-type(7)").string))

    # 기본 정보 변경
    print(inner_index)
    inner_index += 1
    inner_prev_serial = temp_soup[0].select_one("td.index > span").string

    # 시간차주기
    rand_value = random() * 2
    time.sleep(rand_value)

# 데이터 정리
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

# 데이터 추가
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


# 해당 데이터들을 DataFrame으로 저장하고 csv로 저장
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

df_inner_list.to_csv("test.csv", encoding="utf-8", index_label= "unit_id")