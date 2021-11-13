# 데이터 설명

## munpia_novel_list: 문피아 작품 작품 list 정보
## munpia_novel_list_[charge/free] _ [serial/ending] _ [version] _ [page].csv
- charge / free: 데이터 수집 장소가 유료인지 무료인지
- serial / ending: 해당 작품이 연재 중인지 완결되었는지
- version: 데이터를 수집한 버전
- page: 해당 version에서의 n번째 데이터, 하나의 csv로 저장하기에는 memory 부족이 일어남

- header 소개: author,avg_serial_week,check_count,ending,favorite,id,letter,link,period,recommendation,serial_last,serial_start,serial_time,source,title,version,view,view_per_date,recommendation_per_date,letter_per_date,favorite_per_date,view_per_serial,recommendation_per_serial,letter_per_serial,favorite_per_serial
    - author: 소설의 저자
    - avg_serial_week: 소설이 일주일에 연재되는 평균 횟수
    - check_count: 소설이 기준값 이하의 구매량 감소를 겪은 횟수
    - ending: 연재중, 완결의 구분
    - favorite: 해당 작품을 선호하는 독자 수
    - id: 소설의 id, 평범한 id와는 달리 version과 함께 쓸 때에만 고유함
    - letter: 소설의 글자수
    - link: 소설 link
    - period: 소설이 연재된 기간
    - recommendation: 소설이 받은 추천 횟수
    - serial_last: 연재가 된 가장 마지막 날짜
    - serial_start: 연재가 시작된 날짜
    - serial_time: 연재된 횟수
    - source: 해당 데이터를 수집한 곳이 유료인지 무료인지
    - title: 소설의 제목
    - version: 해당 데이터를 획득한 버전
    - view: 소설의 총 조회수
    - view_per_date: 소설이 하루당 받은 조회수
    - recommendation_per_date: 소설이 하루당 받은 추천 횟수
    - letter_per_date: 소설이 하루당 추가된 글자수
    - favorite_per_date: 하루당 추가된 선호하는 독자 수
    - view_per_serial: 1편당 받은 조회수
    - recommendation_per_serial: 1편당 받은 추천 횟수
    - letter_per_serial: 1편당 추가된 글자 수
    - favorite_per_serial: 1편당 추가된 선호하는 독자 수  

## munpia_novel_unit_list: 문피아 작품의 각 작품당 편당 데이터
## munpia_novel_unit_list_[charge/free] _ [serial/ending] _ [version] _ [index].csv

- header 소개: unit_id,book_id,charge,count_comment,date,letter,purchase,rate_change_purchase,rate_change_purchase_five,rate_change_purchase_five_avg,rate_change_recommendation_five,rate_change_recommendation_five_avg,recommendation,serial,sub_title,target,version
    - unit_id: 책의 편당 id, book_id, unit_id, version을 결합할 때 유일한 값이 됨
    - book_id: 책의 id
    - charge: 해당 편이 유료 작품의 무료, 유료인지, 무료 작품의 무료인지 구분
    - count_comment: 해당 편의 댓글 갯수
    - date: 해당 편이 연재된 날짜
    - letter: 해당 편의 쪽 수
    - purchase: 해당 편의 구매횟수, 조회횟수
    - rate_change_purchase: 전편 대비 변화한 구매횟수의 변화율
    - rate_change_purchase_five: 5편 전 대비 변화한 구매횟수의 변화율
    - rate_change_purchase_five_avg: 5편 전부터의 rate_change_purchase의 평균
    - rate_change_recommendation_five: 5편 전 대비 변화한 추천 수의 변화율
    - rate_change_recommendation_five_avg: 5편 전부터의 편당 변화한 추천 수의 변화율의 평균
    - recommendation: 해당 편의 추천 횟수
    - serial: 해당 편의 편 수
    - sub_title: 해당 편의 소제목
    - target: 해당 편이 후에 처리될 때 대상이 되는가 여부, n 시간 전, n 분 전, n 초 전의 데이터를 포함하기 적합하지 않다고 판단
    - version: 해당 데이터를 수집한 버전