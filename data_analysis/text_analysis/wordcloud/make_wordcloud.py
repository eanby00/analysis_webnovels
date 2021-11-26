import nltk
import konlpy
import pandas as pd

sub_title_1 = pd.read_csv("./datas/unit_sub_title_1.csv")

for i in sub_title_1.sub_title:
    print(i)