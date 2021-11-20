-- 정상 케이스: 구매 감소율 기준 이하의 데이터들 rate_change_purchase >= -0.1에 해당함
-- 에러 케이스: 구매 감소율 기준 이상의 데이터들 rate_change_purchase < -0.1에 해당함

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 count_comment 비교
select '에러', version, source, ending, max(count_comment) as max_value, min(count_comment) as min_value, avg(count_comment) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(count_comment) as max_value, min(count_comment) as min_value, avg(count_comment) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스의 모든 분야의 평균 댓글가 에러 케이스에 비해 약 2~3배 더 많았음

select '에러', version, max(count_comment) as max_value, min(count_comment) as min_value, avg(count_comment) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(count_comment) as max_value, min(count_comment) as min_value, avg(count_comment) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 정상 케이스의 모든 분야의 평균 댓글은 에러 케이스에 비해 약 3배 더 많았음

-- count_comment, 댓글 횟수와 구매 감소율과는 연관이 있다고 판단됨
-- 댓글 횟수가 많을수록 구매 감소율이 낮을 것으로 예상

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 letter
select '에러', version, source, ending, max(letter) as max_value, min(letter) as min_value, avg(letter) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(letter) as max_value, min(letter) as min_value, avg(letter) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스와 에러 케이스에 아주 미묘한 차이만 있음

select '에러', version, max(letter) as max_value, min(letter) as min_value, avg(letter) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(letter) as max_value, min(letter) as min_value, avg(letter) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 정상 케이스가 에러 케이스에 비해 평균이 약 0.5쪽 더 많지만, 약 12~13쪽임을 감안하면 그렇게 큰 차이가 아니라고 판단됨

-- letter, 글자 수와 구매 감소율과는 연관이 없다고 판단됨

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 purchase
select '에러', version, source, ending, max(purchase) as max_value, min(purchase) as min_value, avg(purchase) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(purchase) as max_value, min(purchase) as min_value, avg(purchase) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스가 에러 케이스보다 평균 약 3~4배 더 많은 구매, 조회수를 보임

-- purchase, 구매량 혹은 조회량은 구매 감소율에 연관되어 있음
-- 구매량이 높을 수록 구매 감소율은 감소할 것
-- 구매 감소율은 구매량에 의해 정의됨으로 당연함

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 rate_change_purchase - X
-- rate_change_purchase는 구매 감소율의 기준이 되는 값으로 의미 X

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 rate_change_purchase_five
select '에러', version, source, ending, max(rate_change_purchase_five) as max_value, min(rate_change_purchase_five) as min_value, avg(rate_change_purchase_five) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(rate_change_purchase_five) as max_value, min(rate_change_purchase_five) as min_value, avg(rate_change_purchase_five) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스의 모든 분류의 평균값이 에러 케이스보다 약 10% 더 높은 수치를 기록함

select '에러', version, max(rate_change_purchase_five) as max_value, min(rate_change_purchase_five) as min_value, avg(rate_change_purchase_five) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(rate_change_purchase_five) as max_value, min(rate_change_purchase_five) as min_value, avg(rate_change_purchase_five) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 정상 케이스의 모든 분류의 평균값이 에러 케이스보다 약 13% 더 높은 수치를 기록함

-- rate_change_purchase_five, 즉 5화 전의 구매량과 현재 구매량의 변화율은 구매 감소율과 연관되어 있다고 판단됨

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 rate_change_purchase_five_avg
select '에러', version, source, ending, max(rate_change_purchase_five_avg) as max_value, min(rate_change_purchase_five_avg) as min_value, avg(rate_change_purchase_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(rate_change_purchase_five_avg) as max_value, min(rate_change_purchase_five_avg) as min_value, avg(rate_change_purchase_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스와 에러 케이스간의 차이가 거의 없음

select '에러', version, max(rate_change_purchase_five_avg) as max_value, min(rate_change_purchase_five_avg) as min_value, avg(rate_change_purchase_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(rate_change_purchase_five_avg) as max_value, min(rate_change_purchase_five_avg) as min_value, avg(rate_change_purchase_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 두 케이스 간에 차이가 존재하지 않음

-- rate_change_purchase_five_avg, 즉 5화 전부터 구매량의 변화율 평균은 구매 감소율과 연관되지 않음 

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 rate_change_recommendation_five
select '에러', version, source, ending, max(rate_change_recommendation_five) as max_value, min(rate_change_recommendation_five) as min_value, avg(rate_change_recommendation_five) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(rate_change_recommendation_five) as max_value, min(rate_change_recommendation_five) as min_value, avg(rate_change_recommendation_five) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스가 에러 케이스에 비해 약 8% ~15% 더 높음

select '에러', version, max(rate_change_recommendation_five) as max_value, min(rate_change_recommendation_five) as min_value, avg(rate_change_recommendation_five) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(rate_change_recommendation_five) as max_value, min(rate_change_recommendation_five) as min_value, avg(rate_change_recommendation_five) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 평균적으로 약 7% 이상 정상 케이스가 더 높은 평균 수치를 보임

-- rate_change_recommendation_five, 즉 5화전의 추천수와 현재의 추천수의 변화율은 구매 감소율과 연관되어 있음

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 rate_change_recommendation_five_avg
select '에러', version, source, ending, max(rate_change_recommendation_five_avg) as max_value, min(rate_change_recommendation_five_avg) as min_value, avg(rate_change_recommendation_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(rate_change_recommendation_five_avg) as max_value, min(rate_change_recommendation_five_avg) as min_value, avg(rate_change_recommendation_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스와 에러 케이스간의 차이가 거의 없음

select '에러', version, max(rate_change_recommendation_five_avg) as max_value, min(rate_change_recommendation_five_avg) as min_value, avg(rate_change_recommendation_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(rate_change_recommendation_five_avg) as max_value, min(rate_change_recommendation_five_avg) as min_value, avg(rate_change_recommendation_five_avg) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 정상 케이스와 에러 케이스간의 차이가 거의 없음

-- rate_change_recommendation_five_avg는 구매 감소율에 연관되지 않음

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- unit_novel_list의 recommendation	
select '에러', version, source, ending, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version, source, ending
union
select '정상', version, source, ending, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version, source, ending;
    -- 정상 케이스가 에러 케이스에 비해 약 2~3배 더 많음

select '에러', version, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by '에러', version
union
select '정상', version, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_unit_list
where rate_change_purchase >= -0.1 and unit_id > 26 and target = 'True'
group by '정상', version;
    -- 정상 케이스가 에러 케이스에 비행 약 4배 더 많음

-- recommendation, 추천 수는 구매 감소율에 연관을 미침
-- 추천 수가 많다면 구매 감소율은 감소할 것이라 추측할 수 있음

-- ---------------------------------------------------------------------------------------------------------------------------------------------------