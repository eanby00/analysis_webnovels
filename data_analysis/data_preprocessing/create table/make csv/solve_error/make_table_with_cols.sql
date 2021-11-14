drop table novel_unit_list_1_1;
create table novel_unit_list_1_1 as 
select unit_id,book_id, charge,count_comment,date_serial,'완결작',letter,purchase,rate_change_purchase,rate_change_purchase_five,rate_change_purchase_five_avg,rate_change_recommendation_five,rate_change_recommendation_five_avg,recommendation,serial,'문피아_유료',sub_title,target,version from temp_novel_unit_list_charge_ending

drop table novel_unit_list_1_2;
create table novel_unit_list_1_2 as 
select unit_id,book_id, charge,count_comment,date_serial,'연재작',letter,purchase,rate_change_purchase,rate_change_purchase_five,rate_change_purchase_five_avg,rate_change_recommendation_five,rate_change_recommendation_five_avg,recommendation,serial,'문피아_유료',sub_title,target,version from temp_novel_unit_list_charge_serial

drop table novel_unit_list_1_3;
create table novel_unit_list_1_3 as 
select unit_id,book_id, charge,count_comment,date_serial,'완결작',letter,purchase,rate_change_purchase,rate_change_purchase_five,rate_change_purchase_five_avg,rate_change_recommendation_five,rate_change_recommendation_five_avg,recommendation,serial,'문피아_무료',sub_title,target,version from temp_novel_unit_list_free_ending

drop table novel_unit_list_1_4;
create table novel_unit_list_1_4 as 
select unit_id,book_id, charge,count_comment,date_serial,'연재작',letter,purchase,rate_change_purchase,rate_change_purchase_five,rate_change_purchase_five_avg,rate_change_recommendation_five,rate_change_recommendation_five_avg,recommendation,serial,'문피아_무료',sub_title,target,version from temp_novel_unit_list_free_serial;

alter table novel_unit_list_1_1 change `_c5` `ending` string;
alter table novel_unit_list_1_1 change `_c15` `source` string;

alter table novel_unit_list_1_2 change `_c5` `ending` string;
alter table novel_unit_list_1_2 change `_c15` `source` string;

alter table novel_unit_list_1_3 change `_c5` `ending` string;
alter table novel_unit_list_1_3 change `_c15` `source` string;

alter table novel_unit_list_1_4 change `_c5` `ending` string;
alter table novel_unit_list_1_4 change `_c15` `source` string;