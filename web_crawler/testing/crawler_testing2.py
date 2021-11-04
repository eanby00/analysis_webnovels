# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
from random import *
import time

import datetime

# 시간차주기
rand_value = random() * 2
print(rand_value)
time.sleep(rand_value)

req_inner = requests.get("https://novel.munpia.com/277237/page/1", headers={'User-Agent': 'Mozilla/5.0'})
soup_inner = BeautifulSoup(req_inner.text, "html.parser")

# 작품 상세 데이터 가져오기
test1 = soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > div.novel-real-period > span").string
test2 = soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(7) > dd:nth-child(2)").string
test3 = soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(7) > dd:nth-child(4)").string

test4 = int(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(8) > dd:nth-child(2)").string.split(" ")[0])

test5 = int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(8) > dd:nth-child(4)").string.split(",")))
test6 = int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(8) > dd:nth-child(6)").string.split(",")))
test7 = int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > dl:nth-child(8) > dd:nth-child(8)").string.split(",")))
test8 = int("".join(soup_inner.select_one("#board > div.novel-info.dl-horizontal.zoom > div.dd.detail-box > div.button-nav.housing > div.fr > a.button.novel.trigger-subscribe.require-login > span > b").string.string.split(",")))


def cal_period(start, last):
    last_time = datetime.datetime(int(last[0:4]), int(last[5:7]), int(last[8:10]), int(last[11:13]), int(last[14:16]))
    start_time = datetime.datetime(int(start[0:4]), int(start[5:7]), int(start[8:10]), int(start[11:13]), int(start[14:16]))
    return (last_time - start_time).days

print(test1)
print(float(test1.split(" ")[3]))

print(test2)

print(test3)

print(cal_period(test2, test3))

print(test4)

print(test5)

print(test6)

print(test7)

print(test8)