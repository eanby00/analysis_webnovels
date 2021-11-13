drop table novel_list;
create external table if not exists novel_list(
  author
  avg_serial_week
  check_count
  ending
  favorite
  id
  letter
  link
  period,recommendation,serial_last,serial_start,serial_time,source,title,version,view,view_per_date,recommendation_per_date,letter_per_date,favorite_per_date,view_per_serial,recommendation_per_serial,letter_per_serial,favorite_per_serial

)