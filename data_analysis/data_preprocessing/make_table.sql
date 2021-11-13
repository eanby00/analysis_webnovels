drop table novel_list;
create external table if not exists novel_list(
  author string,
  avg_serial_week double,
  check_count int,
  ending string,
  favorite int,
  id int,
  letter int,
  link string,
  period int,
  recommendation int,
  serial_last string,
  serial_start string,
  serial_time int,
  source string,
  title string,
  version int,
  view int,
  view_per_date double,
  recommendation_per_date double,
  letter_per_date double,
  favorite_per_date double,
  view_per_serial double,
  recommendation_per_serial double,
  letter_per_serial double,
  favorite_per_serial double
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/novel_list'
tblproperties('skip.header.line.count' = '1');

drop table novel_unit_list;
create external table if not exists novel_unit_list(
  unit_id int,
  book_id int, 
  charge string,
  count_comment int,
  date string,
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
location '/user/maria_dev/analysis_webnovels/novel_unit_list'
tblproperties('skip.header.line.count' = '1');