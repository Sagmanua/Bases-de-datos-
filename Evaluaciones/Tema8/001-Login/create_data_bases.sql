CREATE DATABASE IF NOT EXISTS superaplicacion
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE superaplicacion;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nombrecompleto VARCHAR(150) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE USER 
'superaplicacion'@'localhost' 
IDENTIFIED  BY 'Superaplicacion123$';

GRANT USAGE ON *.* TO 'superaplicacion'@'localhost';

ALTER USER 'superaplicacion'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON superaplicacion.* 
TO 'superaplicacion'@'localhost';

FLUSH PRIVILEGES;