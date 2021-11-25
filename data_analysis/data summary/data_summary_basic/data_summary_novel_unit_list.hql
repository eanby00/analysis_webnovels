-- unit_novel_list의 count_comment
select version, source, ending, max(count_comment) as max_value, min(count_comment) as min_value, avg(count_comment) as avg_value
from novel_unit_list group by version, source, ending;
    -- 문피아 유료 연재작의 평균 댓글 수가 가장 많았고 문피아 무료의 평균 댓글 수가 비슷하게 적었음

-- unit_novel_list의 letter
select version, source, ending, max(letter) as max_value, min(letter) as min_value, avg(letter) as avg_value
from novel_unit_list group by version, source, ending;
    -- 평균값이 모두 12로 일정했음

-- unit_novel_list의 purchase
select version, source, ending, max(purchase) as max_value, min(purchase) as min_value, avg(purchase) as avg_value
from novel_unit_list group by version, source, ending;
    -- 문피아 유료 완결작 데이터가 평균 3920으로 다른 데이터에 비해 높았음

-- unit_novel_list의 rate_change_purchase
select version, source, ending, max(rate_change_purchase) as max_value, min(rate_change_purchase) as min_value, avg(rate_change_purchase) as avg_value
from novel_unit_list group by version, source, ending;
    -- 모든 데이터의 평균값이 약 0에 수렴

-- unit_novel_list의 rate_change_purchase_five
select version, source, ending, max(rate_change_purchase_five) as max_value, min(rate_change_purchase_five) as min_value, avg(rate_change_purchase_five) as avg_value
from novel_unit_list group by version, source, ending;
    -- 모든 데이터의 평균값이 약 2%씩 감소하고 있었지만, 문피아 유료 연재작 데이터는 약 10%씩 감소함

-- unit_novel_list의 rate_change_purchase_five_avg
select version, source, ending, max(rate_change_purchase_five_avg) as max_value, min(rate_change_purchase_five_avg) as min_value, avg(rate_change_purchase_five_avg) as avg_value
from novel_unit_list group by version, source, ending;
    -- 모든 데이터의 평균값이 약 0에 수렴

-- unit_novel_list의 rate_change_recommendation_five
select version, source, ending, max(rate_change_recommendation_five) as max_value, min(rate_change_recommendation_five) as min_value, avg(rate_change_recommendation_five) as avg_value
from novel_unit_list group by version, source, ending;
    -- 문피아 유료 데이터는 평균 4% 감소하며 문피아 무료 연재작 데이터는 평균 7% 감소하고 있음

-- unit_novel_list의 rate_change_recommendation_five_avg
select version, source, ending, max(rate_change_recommendation_five_avg) as max_value, min(rate_change_recommendation_five_avg) as min_value, avg(rate_change_recommendation_five_avg) as avg_value
from novel_unit_list group by version, source, ending;
    -- 모든 데이터의 평균값이 약 0에 수렴

-- unit_novel_list의 recommendation	
select version, source, ending, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_unit_list group by version, source, ending;
    -- 추천 수의 평균이 문피아 유료가 문피아 무료에 비해 압도적으로 높음

-- table 생성
drop table data_summary_basic;
create table data_summary_basic as
select version, source, ending,
max(count_comment) as max_value_cnt, min(count_comment) as min_value_cnt, avg(count_comment) as avg_value_cnt,
max(letter) as max_value_letter, min(letter) as min_value_letter, avg(letter) as avg_value_letter,
max(purchase) as max_value_purchase, min(purchase) as min_value_purchase, avg(purchase) as avg_value_purchase,
max(rate_change_purchase_five) as max_value_purchase_five, min(rate_change_purchase_five) as min_value_purchase_five, avg(rate_change_purchase_five) as avg_value_purchase_five,
max(recommendation) as max_value_recommendation, min(recommendation) as min_value_recommendation, avg(recommendation) as avg_value_recommendation,
max(rate_change_recommendation_five) as max_value_recommendation_five, min(rate_change_recommendation_five) as min_value_recommendation_five, avg(rate_change_recommendation_five) as avg_value_recommendation_five
from novel_unit_list group by version, source, ending;

select version, source, ending, max_value_cnt, min_value_cnt, avg_value_cnt from data_summary_basic;

select version, source, ending, max_value_letter, min_value_letter, avg_value_letter from data_summary_basic;

select version, source, ending, max_value_purchase, min_value_purchase, avg_value_purchase from data_summary_basic;

select version, source, ending, max_value_purchase_five, min_value_purchase_five, avg_value_purchase_five from data_summary_basic;

select version, source, ending, max_value_recommendation, min_value_recommendation, avg_value_recommendation from data_summary_basic;

select version, source, ending, max_value_recommendation_five, min_value_recommendation_five, avg_value_recommendation_five from data_summary_basic;