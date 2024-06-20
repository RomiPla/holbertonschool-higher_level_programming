-- Este script lista todos records from second_table excluyendo rows un nombre.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;