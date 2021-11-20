-- version 1의 작품 데이터 총 개수: 14713
select count(id) from novel_list where version = 1;

    -- version 1의 문피아 유료 연재작 데이터의 총 개수: 851
    select count(id) from novel_list where version = 1 and source = '문피아_유료' and ending = '연재작';
    -- version 1의 문피아 유료 완결작 데이터의 총 개수: 4785
    select count(id) from novel_list where version = 1 and source = '문피아_유료' and ending = '완결작';
    -- version 1의 문피아 무료 연재작 데이터의 총 개수: 7650
    select count(id) from novel_list where version = 1 and source = '문피아_무료' and ending = '연재작';
    -- version 1의 문피아 무료 완결작 데이터의 총 개수: 1427
    select count(id) from novel_list where version = 1 and source = '문피아_무료' and ending = '완결작';

-- version 1의 편당 데이터 총 개수: 1503410
select count(sub_title) from novel_unit_list where version = 1;

    -- version 1의 문피아 유료 연재작의 편당 데이터 총 개수: 166492
    select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_유료' and ending = '연재작';
    -- version 1의 문피아 유료 완결작의 편당 데이터 총 개수: 980955
    select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_유료' and ending = '완결작';
    -- version 1의 문피아 무료 연재작의 편당 데이터 총 개수: 258916
    select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_무료' and ending = '연재작';
    -- version 1의 문피아 유료 완결작의 편당 데이터 총 개수: 97047
    select count(sub_title) from novel_unit_list where version = 1 and source = '문피아_무료' and ending = '완결작';

-- 기준 값이 -0.3일 때 이하의 구매 변화율을 보이는 편당 데이터가 많은 순으로 정렬
select n.id, n.author, n.ending, n.source, n.title, n.serial_time, nu.cnt, n.link
from novel_list n join (select version, book_id, source, ending, count(sub_title) cnt 
from novel_unit_list
where version = 1 and rate_change_purchase < -0.3 and unit_id > 26
group by version, book_id, source, ending) nu on n.id = nu.book_id and n.source = nu.source and n.version = nu.version and n.ending = nu.ending
order by nu.cnt desc limit 30;
-- 기준 값이 -0.3일 때 이하의 구매 변화율을 보이는 편당 데이터가 작품의 편수 대비 많은 순으로 정렬

-- 기준 값을 0~-0.95까지 0.05 단위로 변화를 주었을 때의 구매 변화율에 보이는 편당 데이터의 총합

-- -0.3이하의 구매 변화율을 보이는 편당 데이터의 총합: 34093
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.3 and unit_id > 26;