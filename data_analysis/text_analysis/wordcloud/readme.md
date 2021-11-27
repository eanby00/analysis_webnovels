### wordcloud 파일 생성 관련 코드

#### datas 폴더에는 hive에서 select를 통해 뽑아낸 데이터들을 저장함

#### font에는 wordcloud를 그릴 때 한국어라서 발생하는 에러를 해결하기 위한 폰트파일이 존재

#### img_wordcloud 폴더에는 결과로써 만들어진 wordcloud 사진 파일들이 존재

#### temp_data 폴더에는 hdfs로 저장해야 하는 csv 파일들 존재

#### 작동 순서
- make_wordcloud_1.py 실행: datas의 뽑아낸 데이터들을 통해 소제목 토큰화, 형태소 분석, temp_data 폴더에 2개의 csv 파일이 생성됨
- temp_data 폴더의 csv 파일을 hdfs의 maria_dev/analysis_webnovels/text_analysis/wordcloud에 저장
- make_tables.hql 실행: csv 파일 기반의 table 2개 생성
- hive에서 remove_duplication.hql 내부의 query 실행 후 결과를 csv로 datas 폴더에 저장 : 정상 케이스와 오류 케이스 간의 중복되는 값들을 제거 
- make_wordcloud_2.py 실행: 실행 결과로 img_wordcloud 폴더에 이미지 파일이 생겨남

#### 작동 순서를 어렵게 한 이유
- 정상 케이스와 오류 케이스 모두 가장 많은 빈도수를 보여주는 값이 비슷하며
- wordcloud 특성상 두 케이스에서 중복되는 데이터를 한 눈에 보기 어려웠음
- 따라서 중복을 제거할 필요성이 생겼고 따라서 과정이 복잡해짐