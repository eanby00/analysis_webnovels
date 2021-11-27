drop table unit_error;
create external table if not exists unit_error(
  word string,
  cnt int
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/text_analysis/wordcloud/error'
tblproperties('skip.header.line.count' = '1');

drop table unit_normal;
create external table if not exists unit_normal(
  word string,
  cnt double
)
row format serde 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
location '/user/maria_dev/analysis_webnovels/text_analysis/wordcloud/normal'
tblproperties('skip.header.line.count' = '1');