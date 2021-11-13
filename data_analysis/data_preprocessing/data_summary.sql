-- version 1의 작품 데이터 총 개수: 14713
select count(id) from novel_list where version = 1;

-- version 1의 편당 데이터 총 개수: 1503410
select count(sub_title) from novel_unit_list where version = 1;

