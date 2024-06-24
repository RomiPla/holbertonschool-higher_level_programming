-- Script para enumerar todas las ciudades en hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id;