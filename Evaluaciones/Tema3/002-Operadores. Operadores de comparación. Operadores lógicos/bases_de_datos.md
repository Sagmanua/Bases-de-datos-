-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS clientes_Tema3_ej002;

-- Usarla
USE clientes_Tema3_ej002;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellidos VARCHAR(50),
    edad INT,
    saldo DECIMAL(10,2)
);

INSERT INTO clientes (nombre, apellidos, edad, saldo) VALUES
('Ana', 'Pérez', 25, 1500.50),
('Luis', 'Gómez', 40, 3200.75),
('María', 'López', 30, 2100.00),
('Juan', 'Rodríguez', 35, 500.25),
('Sofía', 'Martínez', 28, 1800.00);

-- Sumar 500 a la edad
SELECT nombre, apellidos, edad + 500 AS edad_aumentada FROM clientes;
+--------+------------+----------------+
| nombre | apellidos  | edad_aumentada |
+--------+------------+----------------+
| Ana    | Pérez      |            525 |
| Luis   | Gómez      |            540 |
| María  | López      |            530 |
| Juan   | Rodríguez  |            535 |
| Sofía  | Martínez   |            528 |
+--------+------------+----------------+


-- Restar 500 de la edad
SELECT nombre, apellidos, edad - 500 AS edad_reducida FROM clientes;
+--------+------------+---------------+
| nombre | apellidos  | edad_reducida |
+--------+------------+---------------+
| Ana    | Pérez      |          -475 |
| Luis   | Gómez      |          -460 |
| María  | López      |          -470 |
| Juan   | Rodríguez  |          -465 |
| Sofía  | Martínez   |          -472 |
+--------+------------+---------------+

-- Multiplicar la edad por 500
SELECT nombre, apellidos, edad * 500 AS edad_multiplicada FROM clientes;
+--------+------------+-------------------+
| nombre | apellidos  | edad_multiplicada |
+--------+------------+-------------------+
| Ana    | Pérez      |             12500 |
| Luis   | Gómez      |             20000 |
| María  | López      |             15000 |
| Juan   | Rodríguez  |             17500 |
| Sofía  | Martínez   |             14000 |
+--------+------------+-------------------+

-- Dividir la edad entre 500
SELECT nombre, apellidos, edad / 500 AS edad_dividida FROM clientes;
+--------+------------+---------------+
| nombre | apellidos  | edad_dividida |
+--------+------------+---------------+
| Ana    | Pérez      |        0.0500 |
| Luis   | Gómez      |        0.0800 |
| María  | López      |        0.0600 |
| Juan   | Rodríguez  |        0.0700 |
| Sofía  | Martínez   |        0.0560 |
+--------+------------+---------------+

-- Operaciones combinadas con saldo
SELECT nombre, apellidos, edad + 5 AS edad_futura, saldo - 200 AS saldo_actualizado
FROM clientes;

+--------+------------+-------------+-------------------+
| nombre | apellidos  | edad_futura | saldo_actualizado |
+--------+------------+-------------+-------------------+
| Ana    | Pérez      |          30 |           1300.50 |
| Luis   | Gómez      |          45 |           3000.75 |
| María  | López      |          35 |           1900.00 |
| Juan   | Rodríguez  |          40 |            300.25 |
| Sofía  | Martínez   |          33 |           1600.00 |
+--------+------------+-------------+-------------------+
