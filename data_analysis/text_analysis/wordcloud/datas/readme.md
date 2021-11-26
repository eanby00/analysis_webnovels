### wordcloud 생성을 위해 hive에서 뽑아낸 데이터들

#### 오류 케이스의 데이터를 뽑기 위한 hql
- select distinct sub_title from novel_unit_list where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'

#### 정상 케이스의 데이터를 뽑기 위한 hql
- select distinct sub_title from novel_unit_list where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'