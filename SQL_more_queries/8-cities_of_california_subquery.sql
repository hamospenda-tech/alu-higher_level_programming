-- lists all cities of California in the database hbtn_0d_usa (no JOIN)
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
