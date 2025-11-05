CREATE DATABASE ejemploclaves;

USE ejemploclaves;

CREATE TABLE personas(
    nombre VARCHAR(50),
    apellidos VARCHAR(255)
);

ALTER TABLE personas
ADD COLUMN idificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

SHOW TABLES;