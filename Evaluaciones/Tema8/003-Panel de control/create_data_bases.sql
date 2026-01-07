-- Crear la base de datos
CREATE DATABASE periodico_Tema8_ej003
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

-- Seleccionar la base de datos
USE periodico_Tema8_ej003;

-- Tabla de autores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    bio TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de noticias
CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor_id INT NULL,   -- ← Debe permitir NULL

    CONSTRAINT fk_noticias_autores
        FOREIGN KEY (autor_id)
        REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
INSERT INTO autores (nombre, email, bio) VALUES
('María López', 'maria.lopez@example.com', 'Periodista especializada en política nacional.'),
('Carlos Fernández', 'carlos.fernandez@example.com', 'Redactor de tecnología y startups.'),
('Ana Martínez', 'ana.martinez@example.com', 'Corresponsal internacional con base en Bruselas.'),
('Javier Ruiz', 'javier.ruiz@example.com', 'Experto en economía y mercados financieros.');


INSERT INTO noticias (titulo, contenido, autor_id) VALUES
('El Gobierno anuncia nuevas medidas económicas',
 'El presidente ha detallado un conjunto de reformas destinadas a impulsar el crecimiento y reducir el desempleo.',
 1),

('Una startup española desarrolla un dron autónomo revolucionario',
 'La empresa valenciana AeroTech ha presentado su nuevo dron capaz de realizar rutas complejas sin intervención humana.',
 2),

('La Unión Europea debate un nuevo acuerdo climático',
 'Los representantes de los estados miembros negocian un paquete de medidas para acelerar la transición energética.',
 3),

('El mercado bursátil cierra la semana con una subida inesperada',
 'Los principales índices han registrado incrementos tras la publicación de datos positivos sobre empleo.',
 4),

('Nuevas inversiones en energías renovables para 2025',
 'El Ministerio de Industria ha anunciado un plan que prevé incrementar la producción solar en un 30%.',
 1);

 
CREATE USER 
'periodico'@'localhost' 
IDENTIFIED  BY 'Periodico123$';

GRANT USAGE ON *.* TO 'periodico'@'localhost';

ALTER USER 'periodico'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON periodico.* 
TO 'periodico'@'localhost';

FLUSH PRIVILEGES;
