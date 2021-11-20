-- version 1의 작품 데이터 총 개수: 14713
select count(id) from novel_list where version = 1;

-- version 별 작품 데이터의 총 개수
select version, count(id) from novel_list group by version;

-- version 1의 문피아 유료 연재작 데이터의 총 개수: 851
select count(id) from novel_list where version = 1 and source = '문피아_유료' and ending = '연재작';
-- version 1의 문피아 유료 완결작 데이터의 총 개수: 4785
select count(id) from novel_list where version = 1 and source = '문피아_유료' and ending = '완결작';
-- version 1의 문피아 무료 연재작 데이터의 총 개수: 7650
select count(id) from novel_list where version = 1 and source = '문피아_무료' and ending = '연재작';
-- version 1의 문피아 무료 완결작 데이터의 총 개수: 1427
select count(id) from novel_list where version = 1 and source = '문피아_무료' and ending = '완결작';

-- version, source, ending 별 데이터 개수
select version, source, ending, count(id) from novel_list group by version, source, ending;
    -- 문피아 무료 연재작의 작품 개수가 가장 많고 문피아 유료 연재작의 경우 가장 적었음

----------------------------------------------------------------------------------------------------------------

-- version 1의 편당 데이터 총 개수: 1503410
select count(sub_title) from novel_unit_list where version = 1;

-- version 별 평당 데이터 개수
select version, count(sub_title) from novel_unit_list group by version;

-- version 1의 문피아 유료 연재작의 편당 데이터 총 개수: 166492
select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_유료' and ending = '연재작';
-- version 1의 문피아 유료 완결작의 편당 데이터 총 개수: 980955
select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_유료' and ending = '완결작';
-- version 1의 문피아 무료 연재작의 편당 데이터 총 개수: 258916
select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_무료' and ending = '연재작';
-- version 1의 문피아 무료 완결작의 편당 데이터 총 개수: 97047
select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_무료' and ending = '완결작';

-- version, source, ending 별 데이터 개수
select version, source, ending, count(sub_title) from novel_unit_list group by version, source, ending;
    -- 문피아 무료 완결작의 경우 가장 적었고 문피아 유료 완결작의 경우 가장 많음
-----------------------------------------------------------------------------------------------

-- 기준 값이 -0.1일 때 이하의 구매 변화율을 보이는 편당 데이터가 많은 순으로 정렬
select n.id, n.author, n.ending, n.source, n.title, n.serial_time, nu.cnt, n.link
from novel_list n join (select version, book_id, source, ending, count(sub_title) cnt 
from novel_unit_list
where version = 1 and rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by version, book_id, source, ending) nu on n.id = nu.book_id and n.source = nu.source and n.version = nu.version and n.ending = nu.ending
order by nu.cnt desc limit 30;

-- 기준 값이 -0.1일 때 이하의 구매 변화율을 보이는 편당 데이터가 작품의 편수 대비 많은 순으로 정렬
select n.id, n.author, n.ending, n.source, n.title, n.serial_time, nu.cnt, (nu.cnt / n.serial_time) as cnt_per_serial, n.link
from novel_list n join (select version, book_id, source, ending, count(sub_title) cnt 
from novel_unit_list
where version = 1 and rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by version, book_id, source, ending) nu on n.id = nu.book_id and n.source = nu.source and n.version = nu.version and n.ending = nu.ending
order by cnt_per_serial desc limit 30;

-------------------------------------------------------------------------------------------------------------

-- version별 기준 구매 감소율 이상인 편당 데이터 개수
select version, count(sub_title) cnt from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by version;

-- version별, source별, ending별 기준 구매 감소율 이상인 편당 데이터의 개수
select version, source, ending, count(sub_title) cnt from novel_unit_list
where rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
group by version, source, ending;
    -- 문피아 무료 연재작이 가장 많았고 문피아 유료 연재작이 가장 적음