set hive.resultset.use.unique.column.names=false;
SELECT e.word_error, e.cnt
FROM (select distinct word as word_error, cnt from unit_error) e
left JOIN (select distinct word as word_normal from unit_normal) n
ON e.word_error = n.word_normal
where n.word_normal is null;