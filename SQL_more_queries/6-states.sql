-- Script para crear una tabla dentro de una base de datos
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);