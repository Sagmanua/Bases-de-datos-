# Introduce de la practica 
En este practica vamos usar y aprender  CONSTRAN para hacer reglas en la tablas de bases tamboen añadiomos una columna nuevo y borar clomnas.Creamos una nuevo tabla de productos la aplicación de restricciones para garantizar la integridad de los datos y al final asegurando la preservacion de la informacion 

#  Aplicación Práctica
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 




### Abre este bases de datos que luego puedo trabajar en este bases de datos 
```
USE empresadam;
```
### Uso desribe para ver que columnas tiene y con que 
DESCRIBE Clientes;

| Field     | Type         | Null | Key | Default | Extra |
|:-------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| dni       | varchar(9)   | NO   | PRI | NULL    |       |
| nombre    | varchar(50)  | NO   |     | NULL    |       |
| apellidos | varchar(255) | NO   |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |




### Ahora voy a crear una nuevo columnas direccion
```
ALTER TABLE Clientes ADD COLUMN direccion VARCHAR(255);
```
| Field     | Type         | Null | Key | Default | Extra |
|:-------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| dni       | varchar(9)   | NO   | PRI | NULL    |       |
| nombre    | varchar(50)  | NO   |     | NULL    |       |
| apellidos | varchar(255) | NO   |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |
| direccion | varchar(255) | YES  |     | NULL    |       |


### Ahora voya borrar este columno 
```
ALTER TABLE Clientes DROP COLUMN direccion;
```

| Field     | Type         | Null | Key | Default | Extra |
|:-------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| dni       | varchar(9)   | NO   | PRI | NULL    |       |
| nombre    | varchar(50)  | NO   |     | NULL    |       |
| apellidos | varchar(255) | NO   |     | NULL    |       |
| email     | varchar(100) | YES  |     | NULL    |       |
# 3

### Ahora cambiar nombre de colimna dni a dninie para ser mas completa 
```
ALTER TABLE Clientes RENAME COLUMN dni TO dninie;
```

### Ahora borarr CONSTRAINT por que esta mal escribe y no guarda dni nie corecta por que no tiene todos estrictos de dni y nie 
```
ALTER TABLE Clientes DROP CONSTRAINT comprobar_dni_nie_letra;
```

### Ahora voy a añadir nuevo CONSTRAINT correcta y completa que tiene todos los estrictos de dni nie 
```
ALTER TABLE Clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      -- DNI: 8 dígitos + letra
      dninie REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      -- NIE: X/Y/Z + 7 dígitos + letra
      dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dninie, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dninie, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );
```
# 5


## Ahora creo nuevo tabla de productos. Creo paso a paso 


### Creo una tabla de productos con differente columnas
```
CREATE TABLE productos ( 
    id INT, nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT, 
    precio DECIMAL(7,2) NOT NULL, 
    stock INT NOT NULL ) 
    ENGINE=InnoDB;
```
### Añado Primary key a id 
```
ALTER TABLE productos MODIFY id INT NOT NULL, ADD PRIMARY KEY (id);
```
### Añado AUTO_INCREMENT por no valores igual
```
ALTER TABLE productos MODIFY id INT NOT NULL AUTO_INCREMENT;
```
### Añado CONSTRAINT que correge es stock es major o igual a 0

```
ALTER TABLE productos ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0);
```
### Añado CONSTRAINT que correge es precio es major o igual a 0

```
ALTER TABLE productos ADD CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0);
```
### Añado CONSTRAINT que correge es precio es menor o igual a 5000

```
ALTER TABLE productos ADD CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000);
```
### Añado CONSTRAINT que correge es CHAR_LENGTH es mas de 5 leteras o igual

```
ALTER TABLE productos ADD CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5);
```
```
DESCIBE productos;
```
| Field       | Type         | Null | Key | Default | Extra          |
|:-------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| id          | int          | NO   | PRI | NULL    | auto_increment |
| nombre      | varchar(255) | NO   |     | NULL    |                |
| descripcion | text         | YES  |     | NULL    |                |
| precio      | decimal(7,2) | NO   |     | NULL    |                |
| stock       | int          | NO   |     | NULL    |                |

### Insertar values en la tabla productos
```
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES ('Patito Clásico', 'El patito de goma amarillo tradicional.', 3.50, 120), 
('Patito Pirata', 'Patito de goma con parche y sombrero pirata.', 4.25, 80), ('Patito Vampiro', 'Patito con colmillos y capa roja.', 4.75, 60), 
('Patito Doctor', 'Patito con bata blanca y estetoscopio.', 5.10, 40), ('Patito Policía', 'Patito de goma con gorra y placa.', 4.90, 50), 
('Patito Bombero', 'Patito con casco rojo y manguera.', 5.30, 70), 
('Patito Rockero', 'Patito con guitarra y gafas de sol.', 6.20, 25), 
('Patito Chef', 'Patito con gorro de cocinero y cucharón.', 4.80, 45), ('Patito Astronauta', 'Patito con traje espacial blanco.', 7.00, 30), ('Patito Pirata Rosa', 'Versión rosa del patito pirata.', 4.25, 35), 
('Patito Samurai', 'Patito de goma con katana y kimono.', 6.75, 20), 
('Patito Vaquero', 'Patito con sombrero y botas del oeste.', 5.50, 40), ('Patito Zombie', 'Patito con aspecto terrorífico y verde.', 3.99, 100), ('Patito Cupido', 'Patito con arco y alas rosadas.', 5.15, 55), 
('Patito DJ', 'Patito con auriculares y tocadiscos.', 6.40, 25), 
('Patito Científico', 'Patito con gafas de laboratorio.', 5.70, 60), 
('Patito Pirata Dorado', 'Edición especial dorada del patito pirata.', 9.99, 10), 
('Patito Ninja', 'Patito de goma con cinta y shuriken.', 6.10, 35), 
('Patito Sirena', 'Patito mitad pez, mitad pato.', 5.90, 45),
('Patito Gigante', 'Patito de goma de gran tamaño.', 24.99, 5);
```
### Voy a ver que todo inserto vien 
```
SELECT * FROM productos
```
| id | nombre               | descripcion                                  | precio | stock |
|:----:|:----------------------:|:----------------------------------------------:|:--------:|:-------:|
|  1 | Patito Clásico       | El patito de goma amarillo tradicional.      |   3.50 |   120 |
|  2 | Patito Pirata        | Patito de goma con parche y sombrero pirata. |   4.25 |    80 |
|  3 | Patito Vampiro       | Patito con colmillos y capa roja.            |   4.75 |    60 |
|  4 | Patito Doctor        | Patito con bata blanca y estetoscopio.       |   5.10 |    40 |
|  5 | Patito Policía       | Patito de goma con gorra y placa.            |   4.90 |    50 |
|  6 | Patito Bombero       | Patito con casco rojo y manguera.            |   5.30 |    70 |
|  7 | Patito Rockero       | Patito con guitarra y gafas de sol.          |   6.20 |    25 |
|  8 | Patito Chef          | Patito con gorro de cocinero y cucharón.     |   4.80 |    45 |
|  9 | Patito Astronauta    | Patito con traje espacial blanco.            |   7.00 |    30 |
| 10 | Patito Pirata Rosa   | Versión rosa del patito pirata.              |   4.25 |    35 |
| 11 | Patito Samurai       | Patito de goma con katana y kimono.          |   6.75 |    20 |
| 12 | Patito Vaquero       | Patito con sombrero y botas del oeste.       |   5.50 |    40 |
| 13 | Patito Zombie        | Patito con aspecto terrorífico y verde.      |   3.99 |   100 |
| 14 | Patito Cupido        | Patito con arco y alas rosadas.              |   5.15 |    55 |
| 15 | Patito DJ            | Patito con auriculares y tocadiscos.         |   6.40 |    25 |
| 16 | Patito Científico    | Patito con gafas de laboratorio.             |   5.70 |    60 |
| 17 | Patito Pirata Dorado | Edición especial dorada del patito pirata.   |   9.99 |    10 |
| 18 | Patito Ninja         | Patito de goma con cinta y shuriken.         |   6.10 |    35 |
| 19 | Patito Sirena        | Patito mitad pez, mitad pato.                |   5.90 |    45 |
| 20 | Patito Gigante       | Patito de goma de gran tamaño.               |  24.99 |     5 |

### Ahora voy a hacer una beckup de bases de datos 
sudo mysqldump -u root -p empresadam > copiadeseguridad.sql
# Codigo completa 
```
USE empresadam;
-- ver a tabla clientes;
DESCRIBE Clientes;
-- añado y borar columna direccion
ALTER TABLE Clientes ADD COLUMN direccion VARCHAR(255);
ALTER TABLE Clientes DROP COLUMN direccion;
--cambio nombre de dni a dninie
ALTER TABLE Clientes RENAME COLUMN dni TO dninie;
-- borar CONSTRAINT de dninie
ALTER TABLE Clientes DROP CONSTRAINT comprobar_dni_nie_letra;
--Añado nuevo CONSTRAINT
ALTER TABLE Clientes
  ADD CONSTRAINT comprobar_dni_nie_letra
  CHECK (
    (
      -- DNI: 8 dígitos + letra
      dninie REGEXP '^[0-9]{8}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (CAST(SUBSTRING(dninie, 1, 8) AS UNSIGNED) MOD 23) + 1,
                1)
    )
    OR
    (
      -- NIE: X/Y/Z + 7 dígitos + letra
      dninie REGEXP '^[XYZxyz][0-9]{7}[A-Za-z]$'
      AND
      UPPER(SUBSTRING(dninie, 9, 1)) =
      SUBSTRING('TRWAGMYFPDXBNJZSQVHLCKE',
                (
                  CAST(CONCAT(
                        CASE UPPER(SUBSTRING(dninie, 1, 1))
                          WHEN 'X' THEN '0'
                          WHEN 'Y' THEN '1'
                          WHEN 'Z' THEN '2'
                        END,
                        SUBSTRING(dninie, 2, 7)
                  ) AS UNSIGNED) MOD 23
                ) + 1,
                1)
    )
  );
--- Voy a crear nuevo tabla de productos
CREATE TABLE productos ( 
    id INT, nombre VARCHAR(255) NOT NULL, 
    descripcion TEXT, 
    precio DECIMAL(7,2) NOT NULL, 
    stock INT NOT NULL ) 
    ENGINE=InnoDB;
ALTER TABLE productos MODIFY id INT NOT NULL, ADD PRIMARY KEY (id);
ALTER TABLE productos MODIFY id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE productos ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0);
ALTER TABLE productos ADD CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0);
ALTER TABLE productos ADD CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000);
ALTER TABLE productos ADD CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5);
--si paso vien
DESCRIBE productos;
-- Inserta a productos
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES ('Patito Clásico', 'El patito de goma amarillo tradicional.', 3.50, 120), 
('Patito Pirata', 'Patito de goma con parche y sombrero pirata.', 4.25, 80), ('Patito Vampiro', 'Patito con colmillos y capa roja.', 4.75, 60), 
('Patito Doctor', 'Patito con bata blanca y estetoscopio.', 5.10, 40), ('Patito Policía', 'Patito de goma con gorra y placa.', 4.90, 50), 
('Patito Bombero', 'Patito con casco rojo y manguera.', 5.30, 70), 
('Patito Rockero', 'Patito con guitarra y gafas de sol.', 6.20, 25), 
('Patito Chef', 'Patito con gorro de cocinero y cucharón.', 4.80, 45), ('Patito Astronauta', 'Patito con traje espacial blanco.', 7.00, 30), ('Patito Pirata Rosa', 'Versión rosa del patito pirata.', 4.25, 35), 
('Patito Samurai', 'Patito de goma con katana y kimono.', 6.75, 20), 
('Patito Vaquero', 'Patito con sombrero y botas del oeste.', 5.50, 40), ('Patito Zombie', 'Patito con aspecto terrorífico y verde.', 3.99, 100), ('Patito Cupido', 'Patito con arco y alas rosadas.', 5.15, 55), 
('Patito DJ', 'Patito con auriculares y tocadiscos.', 6.40, 25), 
('Patito Científico', 'Patito con gafas de laboratorio.', 5.70, 60), 
('Patito Pirata Dorado', 'Edición especial dorada del patito pirata.', 9.99, 10), 
('Patito Ninja', 'Patito de goma con cinta y shuriken.', 6.10, 35), 
('Patito Sirena', 'Patito mitad pez, mitad pato.', 5.90, 45),
('Patito Gigante', 'Patito de goma de gran tamaño.', 24.99, 5);

--Ver paso vien o no
SELECT * FROM producto;


```
# Conclusión enlazando con la actividad 

La práctica permitió aplicar de manera práctica conceptos fundamentales de gestión de bases de datos, como la modificación de tablas, manejo de restricciones, creación de nuevas estructuras y realización de copias de seguridad. Estas tareas refuerzan la comprensión sobre la integridad de los datos y la organización eficiente de la información, tal como se planteó en la actividad.

