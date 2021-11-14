drop table temp_novel_unit_list_charge_ending;
create external table if not exists temp_novel_unit_list_charge_ending(
  unit_id int,
  book_id int, 
  charge string,
  count_comment int,
  date_serial string,
  letter int,
  purchase int,
  rate_change_purchase double,
  rate_change_purchase_five double,
  rate_change_purchase_five_avg double,
  rate_change_recommendation_five double,
  rate_change_recommendation_five_avg double,
  recommendation int,
  serial int,
  sub_title string,
  target boolean,
  version int
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/novel_unit_list/munpia_novel_unit_list_charge_ending'
tblproperties('skip.header.line.count' = '1');

drop table temp_novel_unit_list_charge_serial;
create external table if not exists temp_novel_unit_list_charge_serial(
  unit_id int,
  book_id int, 
  charge string,
  count_comment int,
  date_serial string,
  letter int,
  purchase int,
  rate_change_purchase double,
  rate_change_purchase_five double,
  rate_change_purchase_five_avg double,
  rate_change_recommendation_five double,
  rate_change_recommendation_five_avg double,
  recommendation int,
  serial int,
  sub_title string,
  target boolean,
  version int
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/novel_unit_list/munpia_novel_unit_list_charge_serial'
tblproperties('skip.header.line.count' = '1');

drop table temp_novel_unit_list_free_ending;
create external table if not exists temp_novel_unit_list_free_ending(
  unit_id int,
  book_id int, 
  charge string,
  count_comment int,
  date_serial string,
  letter int,
  purchase int,
  rate_change_purchase double,
  rate_change_purchase_five double,
  rate_change_purchase_five_avg double,
  rate_change_recommendation_five double,
  rate_change_recommendation_five_avg double,
  recommendation int,
  serial int,
  sub_title string,
  target boolean,
  version int
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/novel_unit_list/munpia_novel_unit_list_free_ending'
tblproperties('skip.header.line.count' = '1');

drop table temp_novel_unit_list_free_serial;
create external table if not exists temp_novel_unit_list_free_serial(
  unit_id int,
  book_id int, 
  charge string,
  count_comment int,
  date_serial string,
  letter int,
  purchase int,
  rate_change_purchase double,
  rate_change_purchase_five double,
  rate_change_purchase_five_avg double,
  rate_change_recommendation_five double,
  rate_change_recommendation_five_avg double,
  recommendation int,
  serial int,
  sub_title string,
  target boolean,
  version int
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/novel_unit_list/munpia_novel_unit_list_free_serial'
tblproperties('skip.header.line.count' = '1');