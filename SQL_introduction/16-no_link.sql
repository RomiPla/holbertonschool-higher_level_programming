-- Sólo muestra las filas que tienen un valor de nombre
SELECT score, name FROM second_table HAVING name IS NOT NULL ORDER BY score DESC;