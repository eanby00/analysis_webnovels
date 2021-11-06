from bs4 import BeautifulSoup
import requests
import datetime

def parseInt(num_string):
    return int("".join(num_string.split(",")))

def parseIntremove(num_string):
    return int("".join(num_string.strip().replace("쪽", "").split(",")))

url_charged = "https://novel.munpia.com/259775/page/1"
req = requests.get(url_charged, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(req.text, "html.parser")
temp_soup = soup.select("#ENTRIES > tbody > tr")
print(temp_soup[0].select_one("td.index > span").string)
# for i in range(len(temp_soup)):
#     if temp_soup[i].select_one("td.index > span").string != u"공지":
#         print(parseInt(temp_soup[i].select_one("td.index > span").string)) # 편수
#         print(temp_soup[i].select("td.subject > a")[0].string) # 제목

#         if temp_soup[i].select("td.subject > a")[1].string == None:
#             print(0)
#         else:
#             print(temp_soup[i].select("td.subject > a")[1].string) # 댓글 수
        
#         if temp_soup[i].select_one("td.subject > span.coin") == None:
#             print("무료_작품")
#         elif temp_soup[i].select_one("td.subject > span.coin.coin-free") == None:
#             print("유료")
#         else:
#             print("무료")

#         date = temp_soup[i].select_one("td.date").string 
#         flag_h = date.find(u"시간")
#         flag_m = date.find(u"분")
#         flag_s = date.find(u"초")

#         if flag_h != -1 or flag_m != -1 or flag_s != -1:
#             print("find")
#             print(str(datetime.datetime.now().year)+"."+str(datetime.datetime.now().month)+"."+str(datetime.datetime.now().day))
#         else:
#             date_temp = date.split(".")
#             date_temp[0] = str(20) + date_temp[0]
#             print(".".join(date_temp))
#         print(parseInt(temp_soup[i].select_one("td:nth-of-type(5)").string))
#         print(parseInt(temp_soup[i].select_one("td:nth-of-type(6) span").string))
#         print(parseIntremove(temp_soup[i].select_one("td:nth-of-type(7)").string))
#         print("-------------------------------")