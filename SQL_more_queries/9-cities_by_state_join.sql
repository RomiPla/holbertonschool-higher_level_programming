-- Script que liste todas las ciudades contenidas en un Database
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id