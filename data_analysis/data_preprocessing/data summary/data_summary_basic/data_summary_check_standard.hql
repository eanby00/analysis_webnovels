-- 기준 값을 0~-0.95까지 0.05 단위로 변화를 주었을 때의 구매 변화율에 보이는 편당 데이터의 총합

select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < 0 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.05 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.1 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.15 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.20 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.25 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.3 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.35 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.4 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.45 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.5 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.55 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.6 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.65 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.7 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.75 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.8 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.85 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.9 and unit_id > 26 and target = 'True'
union
select count(sub_title) cnt from novel_unit_list
where version = 1 and rate_change_purchase < -0.95 and unit_id > 26 and target = 'True';