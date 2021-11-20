-- 각 항목별 데이터의 max, min, avg

-- novel_list의 avg_serial_week O
select version, source, ending, max(avg_serial_week), min(avg_serial_week), avg(avg_serial_week) from novel_list group by version, source, ending;
    -- 문피아 유료의 연재작만이 평균 연재 횟수가 null이 아니었음
        -- 문피아 무료의 경우 무료이기 때문에 연재가 불안정한 경우가 많아 제대로 측정이 되지 않는다고 추측
        -- 완결작의 경우 연재 횟수가 제공되지 않는 경우가 많았음

-- novel_list의 favorite O
select version, source, ending, count(favorite) as count_value, max(favorite) as max_value, min(favorite) as min_value, avg(favorite) as avg_value
from novel_list group by version, source, ending;
    -- 문피아 유료 완결작의 경우 최대 선호 독자 수가 가장 많음
    -- 문피아 유료 연재작의 평균 선호 독자 수가 가장 많음
    -- 문피아 무료 연재작이 가장 많음에도 불구하고 가장 적은 평균 선호 독자 수를 가짐

-- novel_list의 letter X
select version, source, ending, max(letter), min(letter), avg(letter) from novel_list group by version, source, ending;
    -- 최대값이 최소값보다 작거나, 최대값이 평균보다 작은 경우가 많아 분석에 적합한 attribute가 아니라고 판단함

-- novel_list의 period X
select version, source, ending, max(period) as max_value, min(period) as min_value, avg(period) as avg_value
from novel_list group by version, source, ending;
    -- 평균의 경우 문피아 무료 연재작은 음의 값을 가지고 있었고 음수의 기간을 가진 것은 무작위적임
    -- 따라서 분석에 적합한 attribute가 아니라고 판단
    -- 그에 따라 period로 만들어지는 view_per_date, recommendation_per_date, favorite_per_date 모두 분석에서 제외함

-- novel_list의 recommendation O
select version, source, ending, max(recommendation) as max_value, min(recommendation) as min_value, avg(recommendation) as avg_value
from novel_list group by version, source, ending;
    -- 최대값과 평균 모두 문피아 유료 연재작이 가장 높았음

-- novel_list의 serial_time X
select version, source, ending, max(serial_time) as max_value, min(serial_time) as min_value, avg(serial_time) as avg_value
from novel_list group by version, source, ending;
    -- period와 마찬가지로 최대값보다 최소값이나 평균이 높은 것이 대다수이며
    -- 모든 종류의 데이터의 최대값이 동일하기 때문에 분석에 적합한 attribute가 아니라고 판단
    -- 따라서 이것으로부터 파생되는 view_per_serial, recommendation_per_serial, letter_per_serial, favorite_per_serial을 모두 분석 대상에서 제외

-- novel_list의 view X
select version, source, ending, max(view) as max_value, min(view) as min_value, avg(view) as avg_value
from novel_list group by version, source, ending;
    -- period와 마찬가지의 이유로 분석에 적합한 attribute가 아니라고 판단됨