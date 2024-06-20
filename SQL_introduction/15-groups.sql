--Este script lista el número de registros con la misma puntuación en la tabla second_table.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;