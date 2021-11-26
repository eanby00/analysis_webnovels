from konlpy.tag import Okt
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

twitter_tag = Okt()

## 인공지능 konltk 예제 코드, return 부분만 string으로 list를 결합해서 return하도록 변형
## 문자열을 검사해 pos로 표준화를 한 후 조사, 어미등을 제외한 나머지를 " "로 구분된 string으로 반환
def twitter_tokenizer_filter(text):
    malist = twitter_tag.pos(text, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "KoreanParticle"]:
            r.append(word[0])
    return r

def dataframe_dict(df):
    temp = []
    for sub_title_list in df.sub_title:
        temp += sub_title_list
    return temp

# def twitter_tokenizer_filter(text):
#     malist = twitter_tag.pos(text, norm=True, stem=True)
#     r = []
#     for word in malist:
#         if not word[1] in ["Josa", "Eomi", "Punctuation", "KoreanParticle"]:
#             r.append(word[0])
#     return " ".join(r)

# --------------------------------------------------------------------------------------
# 에러 케이스의 wordcloud

## csv 데이터 불러오기
sub_title_error = pd.read_csv("./datas/unit_error.csv")

## dataframe의 각 열에 filter 적용
sub_title_error["sub_title"] = sub_title_error["sub_title"].apply(twitter_tokenizer_filter)

## WordCloud에 적용하기 위해 dataframe에 열로 분리된 string들을 하나로 결합
temp_error = dataframe_dict(sub_title_error)
count_error = Counter(temp_error)
dict_error = dict(count_error)

print(dict_error)

## WordCloud 생성
word_cloud_error = WordCloud(font_path="./font/NanumGothic.ttf", background_color="white").generate_from_frequencies(dict_error)
print(word_cloud_error.words_)

## 생성한 것을 plt로 그리고 저장
plt.figure(figsize= (16, 9))
plt.imshow(word_cloud_error, interpolation="bilinear")
plt.savefig("./img_wordcloud/wordcloud_error.png")