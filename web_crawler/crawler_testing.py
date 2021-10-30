from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from subprocess import PIPE, Popen

url = "https://novel.munpia.com/page/hd.platinum/group/pl.serial/exclusive/true/view/allend"

req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(req.text, "html.parser")

li_list_author = soup.select("#SECTION-LIST > ul a.author.col-xs-4")
li_list_title = soup.select("#SECTION-LIST > ul a.title.col-xs-6")

temp_author = []
temp_title = []
for i in range(len(li_list_author)):
    temp_author.append(li_list_author[i].string)
    temp_title.append(li_list_title[i].string.strip())

df = pd.DataFrame({"author":temp_author, "temp_title":temp_title})

file_name = "test.csv"
df.to_csv(file_name, encoding="utf-8")

hdfs_path = os.path.join(os.sep,  "user", "maria_dev", file_name)

put = Popen(["hadoop", "fs", "-put", file_name, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()
