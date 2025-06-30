-- Lists all records of the table second_table where name is not NULL
-- Results display score and name (in this order)
-- Records are listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
