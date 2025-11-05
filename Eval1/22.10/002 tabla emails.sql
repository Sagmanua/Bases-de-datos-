CREATE DATABASE ejemploclaves;

USE ejemploclaves;

CREATE TABLE emails(
    direcciones VARCHAR(50),
    personas VARCHAR(255)
);

ALTER TABLE emails
ADD COLUMN idificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

SHOW TABLES;