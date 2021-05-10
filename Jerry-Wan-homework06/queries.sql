-- write your queries underneath each number:
 
-- 1. the total number of rows in the database
SELECT count(*) FROM esport;
-- 2. show the first 15 rows, but only display 3 columns (your choice)
SELECT (game_name,release_date,genre) FROM esport LIMIT 15;
-- 3. do the same as above, but chose a column to sort on, and sort in descending order
SELECT (game_name,release_date,genre) FROM esport ORDER BY release_date DESC LIMIT 15;
-- 4. add a new column without a default value
ALTER TABLE esport ADD is_game INTEGER；
-- 5. set the value of that new column
ALTER TABLE esport ALTER COLUMN is_game SET DEFAULT 1;
-- 6. show only the unique (non duplicates) of a column of your choice
SELECT DISTINCT release_date FROM esport;
-- 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
SELECT release_date, SUM(total_earning) FROM esport GROUP BY release_date;
-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 
 SELECT release_date, SUM(total_earning) FROM esport GROUP BY release_date HAVING SUM(total_earning)>10000000;
-- 9. write a comment about your query 9
-- find the order of sum of income of the game after 2000
SELECT release_date, SUM(total_earning) FROM esport WHERE release_date >2000 GROUP BY release_date ORDER BY sum DESC;
-- 10. write a comment about your query 10
-- find the order of avg of income of the game before 2000
SELECT release_date, AVG(total_earning) FROM esport WHERE release_date <2000 GROUP BY release_date ORDER BY avg DESC;
-- 11. write a comment about your query 11
-- add a new column get earning per player
 ALTER TABLE esport ADD per_player numeric;
-- 12. write a comment about your query 12
-- calculate the result
UPDATE esport SET per_player = total_earning/total_player WHERE total_player>0;
