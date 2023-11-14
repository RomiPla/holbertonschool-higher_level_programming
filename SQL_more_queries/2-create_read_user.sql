-- Corrobora si Database existe, si no existe la crea
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Corrobora si el usuario existe, si no existe lo crea
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Otorgar privilegio en la base de datos específica
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
