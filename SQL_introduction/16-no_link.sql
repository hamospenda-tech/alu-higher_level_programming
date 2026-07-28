-- lists all records of second_table that have a name, ordered by score desc
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
