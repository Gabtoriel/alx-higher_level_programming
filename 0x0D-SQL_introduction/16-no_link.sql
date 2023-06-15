-- Mysql script to list the score of students that have names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
