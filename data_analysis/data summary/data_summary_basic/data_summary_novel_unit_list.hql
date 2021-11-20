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