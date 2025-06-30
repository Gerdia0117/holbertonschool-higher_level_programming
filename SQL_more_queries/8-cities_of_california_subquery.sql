-- List all cities of California from the database hbtn_0d_usa
-- Results must be sorted in ascending order by cities.id
-- Cannot use JOIN keyword, must use subquery
-- Database name will be passed as argument to mysql command

SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
