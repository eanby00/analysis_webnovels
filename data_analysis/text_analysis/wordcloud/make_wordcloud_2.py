from konlpy.tag import Okt
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

twitter_tag = Okt()

## 인공지능 konltk 예제 코드, 숫자들도 제외함
## 문자열을 검사해 pos로 표준화를 한 후 조사, 어미등을 제외한 나머지를 list로 반환
def twitter_tokenizer_filter(text):
    malist = twitter_tag.pos(text, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "KoreanParticle", "Number"]:
            r.append(word[0])
    return r

## 열이 리스트로 이루어진 데이터 프레임의 전체 값을 하나의 리스트로 결합시키기
def dataframe_dict(df):
    temp = []
    for sub_title_list in df.sub_title:
        temp += sub_title_list
    return temp

# --------------------------------------------------------------------------------------
# 에러 케이스의 wordcloud

## csv 데이터 불러오기
sub_title_error = pd.read_csv("./datas/unit_error.csv", keep_default_na= False)

## dataframe의 각 열에 filter 적용
sub_title_error["sub_title"] = sub_title_error["sub_title"].apply(twitter_tokenizer_filter)

## WordCloud에 적용하기 위해 리스트와 빈도수를 구하여 dict으로 변환
temp_error = dataframe_dict(sub_title_error)
count_error = Counter(temp_error)
dict_error = dict(count_error)

## WordCloud 생성
word_cloud_error = WordCloud(font_path="./font/NanumGothic.ttf", background_color="white").generate_from_frequencies(dict_error)
print(word_cloud_error.words_)

## 생성한 것을 plt로 그리고 저장
plt.figure(figsize= (16, 9))
plt.imshow(word_cloud_error, interpolation="bilinear")
plt.savefig("./img_wordcloud/wordcloud_error.png")

# --------------------------------------------------------------------------------------
# 정상 케이스의 wordcloud

## csv 데이터 불러오기
sub_title_normal = pd.read_csv("./datas/unit_normal.csv", keep_default_na= False)

## dataframe의 각 열에 filter 적용
sub_title_normal["sub_title"] = sub_title_normal["sub_title"].apply(twitter_tokenizer_filter)

## WordCloud에 적용하기 위해 리스트와 빈도수를 구하여 dict으로 변환
temp_normal = dataframe_dict(sub_title_normal)
count_normal = Counter(temp_normal)
dict_normal = dict(count_normal)

## WordCloud 생성
word_cloud_normal = WordCloud(font_path="./font/NanumGothic.ttf", background_color="white").generate_from_frequencies(dict_normal)
print(word_cloud_normal.words_)

## 생성한 것을 plt로 그리고 저장
plt.figure(figsize= (16, 9))
plt.imshow(word_cloud_normal, interpolation="bilinear")
plt.savefig("./img_wordcloud/wordcloud_normal.png")