# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen
from random import *
import time
import datetime

version_main = 1
main_id = 0
unit_serial = 0

author = u"켄치"

comment_main_id = []
comment_unit_serial = []
comment_version = []
comment_commenter = []
comment_content = []
comment_isauth = []

req_comment = requests.get("https://novel.munpia.com/287638/page/1/neSrl/4261434/nvView/viewComments/window-mode/true", headers={'User-Agent': 'Mozilla/5.0'})
soup_comment = BeautifulSoup(req_comment.text, "html.parser")
li_list_commenter = soup_comment.select("ul.comments dl dd:nth-child(2) a strong")
li_list_content = soup_comment.select("ul.comments div p:nth-child(1)")

for comment_index in range(len(li_list_commenter)):
    comment_main_id.append(main_id)
    comment_unit_serial.append(unit_serial)
    comment_version.append(version_main)
    comment_commenter.append(li_list_commenter[comment_index].string)
    comment_content.append(li_list_content[comment_index].getText())
    comment_isauth.append(author == comment_commenter[comment_index].string)

df_comment = pd.DataFrame({
    "book_id": comment_main_id,
    "unit_serial":comment_unit_serial,
    "version": comment_version,
    "commenter":comment_commenter,
    "content":comment_content,
    "isauth":comment_isauth
})

df_comment.to_csv("test.csv", encoding="utf-8")