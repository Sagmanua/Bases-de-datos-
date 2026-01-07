CREATE DATABASE clientes_Tema3_001;
USE clientes_Tema3_001;

CREATE TABLE clientes(
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  edad INT
);

INSERT INTO clientes VALUES('Juan', 'Pérez', 30), ('Ana', 'López', 25), ('Pedro', 'Martínez', 40);

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |
+--------------------+-----------------------+------------------+


  SELECT * FROM clientes;

+--------+-----------+------+
| nombre | apellidos | edad |
+--------+-----------+------+
| Juan   | Pérez     |   30 |
| Ana    | López     |   25 |
| Pedro  | Martínez  |   40 |
+--------+-----------+------+


SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos;

  +--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |
+--------------------+-----------------------+------------------+



SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC, apellidos ASC;

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
+--------------------+-----------------------+------------------+


SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC;

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
+--------------------+-----------------------+------------------+


SELECT 
  nombre,
  apellidos
FROM 
  clientes;

+--------+-----------+
| nombre | apellidos |
+--------+-----------+
| Juan   | Pérez     |
| Ana    | López     |
| Pedro  | Martínez  |
+--------+-----------+


SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;

+--------------------+-----------------------+------------------+
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
+--------------------+-----------------------+------------------+
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |
+--------------------+-----------------------+------------------+
