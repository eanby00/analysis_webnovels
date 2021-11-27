import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

## csv 데이터 불러오기
main_data = pd.read_csv("./datas/unit_remove_duplication.csv", keep_default_na= False)
print(main_data.head())

### main_data의 내용으로 dict 채우기
dict_main = {}
for i in range(len(main_data)):
    dict_main[main_data["word_error"][i]] = main_data["cnt"][i]

## WordCloud 생성
word_cloud = WordCloud(font_path="./font/NanumGothic.ttf", background_color="white").generate_from_frequencies(dict_main)
print(word_cloud.words_)

## 생성한 것을 plt로 그리고 저장
plt.figure(figsize= (16, 9))
plt.imshow(word_cloud, interpolation="bilinear")
plt.savefig("./img_wordcloud/wordcloud.png")