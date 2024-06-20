-- This script lists all records from second_table excluding rows without a name.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;