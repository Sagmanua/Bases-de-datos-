# 1.-Indroduccion brece y contexalizacion
Este ejercicio se enfoca en el desarrollo de un sistema de gestión de contenidos (CMS) básico. El objetivo es aprender a estructurar una base de datos relacional donde la información de los autores y las noticias esté conectada de forma lógica. Mediante el uso de SQL y PHP, simulamos el entorno real de un periódico digital, priorizando la integridad de los datos y el control de acceso mediante un panel administrativo.




# 2.-Desarrollo técnico correcto y preciso
## create_data_bases.sql 
### creo una base de datos `periodico_Tema8_ej003`
```
CREATE DATABASE periodico_Tema8_ej003

USE periodico_Tema8_ej003;
```
### creo tabla `noticias` y `autores`
```
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
```

### hago una insert in base de datos
```
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
```
### creo una user para conectar base de datos
```
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
```
## index.php
### hago include la pagina `listar_articulos.php`
```
<?php
include 'inc/listar_articulos.php';
?>
``` 
## listar_articulos.php
### conexion de la bases de datos
```
$host = "localhost";
$user = "periodico";
$pass = "Periodico123$";
$db   = "periodico";
$conexion = new mysqli($host, $user, $pass, $db);
```
### hago un select de la tabla `noticias` 
```
$sql = "SELECT * FROM noticias";
```

### hago una HTTP request
```
$resultado = $conexion->query($sql);
        while ($fila = $resultado->fetch_assoc()) {
```

### cuando HTTP request es trabajo hace una demuestra de la informacion de la pagina
``` 
while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha_publicacion'].'</time>
              <p>'.$fila['autor_id'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }
```
# Codigo Completo
Project\  
├─ explicacion.md 
├─ inc\
|   └─ listar_articulos.php  
├─ create_data_bases.sql  
└─ index.php  
## create_data_bases.sql 
```
CREATE DATABASE periodico_Tema8_ej003


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

```
## index.php 
```
<?php
include 'inc/listar_articulos.php';
?>

```
## listar_articulos.php
```
<?php
        $host = "localhost";
        $user = "periodico";
        $pass = "Periodico123$";
        $db   = "periodico";
        $conexion = new mysqli($host, $user, $pass, $db);
        $sql = "SELECT * FROM noticias";
        $resultado = $conexion->query($sql);
        while ($fila = $resultado->fetch_assoc()) {
          echo '
            <article>
              <h3>'.$fila['titulo'].'</h3>
              <time>'.$fila['fecha_publicacion'].'</time>
              <p>'.$fila['autor_id'].'</p>
              <p>'.$fila['contenido'].'</p>
            </article>
          ';
        }
        $conexion->close();
      ?>
```

# 4.-Cierre/Conclusión enlazando con la unidad

La actividad integra los conceptos clave de la unidad: administración, seguridad y consulta de datos. Al configurar privilegios de usuario y automatizar identificadores con AUTO_INCREMENT, hemos creado un entorno robusto para el almacenamiento de información. En conclusión, este flujo de trabajo demuestra cómo la correcta comunicación entre el servidor de base de datos y la aplicación es esencial para garantizar que el contenido llegue al usuario final de manera dinámica y organizada.


