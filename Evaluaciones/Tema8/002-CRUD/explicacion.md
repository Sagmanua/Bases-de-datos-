# 1.-Indroduccion brece y contexalizacion


Esta práctica aborda la gestión de bases de datos mediante el ciclo de vida de los datos. Nos enfocamos en la creación de estructuras SQL y la interacción dinámica mediante PHP y HTML. El objetivo es dominar las operaciones de creación y actualización (C y U del modelo CRUD) en un entorno de gestión de empleados.


# 2.-Desarrollo técnico correcto y preciso
## 001-Creamos base de datos de clientes.sql
### creo una base de datos `empleados`
```
CREATE DATABASE IF NOT EXISTS empleados
    DEFAULT CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

USE empleados;
```
### creo una tabla `empleados` con columnas
* id
* nombre
* puesto
* salario
* fecha_contratacion
* departamento
```
DROP TABLE IF EXISTS empleados;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento VARCHAR(100)
);
```
### hago una insert into tabla `empleados`

```
-- 4. Insert sample data
INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion, departamento) VALUES
('Ana Torres', 'Administrativa', 21000.00, '2021-03-15', 'Administración'),
('Luis Martínez', 'Desarrollador Backend', 32000.00, '2020-11-02', 'IT'),
('Marta López', 'Desarrolladora Frontend', 30000.00, '2022-01-10', 'IT'),
('Carlos Pérez', 'Comercial', 25000.00, '2019-07-08', 'Ventas'),
('Elena García', 'Marketing Specialist', 27000.00, '2021-09-23', 'Marketing'),
('Javier Ruiz', 'Técnico de Soporte', 24000.00, '2020-02-14', 'Soporte'),
('Patricia Sánchez', 'Recursos Humanos', 26000.00, '2018-06-20', 'RRHH'),
('Sergio Gómez', 'Data Analyst', 35000.00, '2022-05-01', 'Datos'),
('Raquel Navarro', 'Diseñadora UX/UI', 29000.00, '2021-12-01', 'IT'),
('David Fernández', 'Contable', 23000.00, '2019-10-30', 'Finanzas');
```
### creo usario para conectar a bases de datos
```
CREATE USER 
'empleados'@'localhost' 
IDENTIFIED  BY 'Empleados123$';

GRANT USAGE ON *.* TO 'empleados'@'localhost';

ALTER USER 'empleados'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empleados.* 
TO 'empleados'@'localhost';

FLUSH PRIVILEGES;
```
## 001-Miniformulario.html 
### creo una facil structura de la HTML
```
<!doctype html>
<html lang="es">
  <head>
    <title>Jose Vicente Carratala</title>
    <meta charset="utf-8">
  </head>
  <body>
  </body>
</html>
```
### dentro de `body` creo una `form` creo una `method` con POST que envia informacion a file `002-procesamodificar.php` para procesar informacion
```
<form action="002-procesamodificar.php" method="POST">
    <p>Introduce el ID del elemento que quieres modificar</p>
    <input type="number" name="id" placeholder="id">
    <input type="submit">
</form>
```
## 002-procesamodificar.php
### Primero cogemos la info que viene del formulario
```
    $nombre = $_POST['nombre'];
    $puesto = $_POST['puesto'];
    $salario = $_POST['salario'];
    $fecha_contratacion = $_POST['fecha_contratacion'];
    $departamento = $_POST['departamento'];
    $id = $_POST['id'];
```
###  Y luego metemos esa información en la base de datos
```
$host = "localhost";
$user = "empleados";
$pass = "Empleados123$";
$db   = "empleados";
$conexion = new mysqli($host, $user, $pass, $db);
```
###  Metemos los datos en la base de datos
```
 $sql = "
  	 UPDATE empleados SET
     	nombre = '".$nombre."',
      puesto = '".$puesto."',
      salario = '".$salario."',
      fecha_contratacion = '".$fecha_contratacion."',
      departamento = '".$departamento."' 
      WHERE id = ".$id."
    ;
  ";
```


# Codigo Completo
Project\  
├─ explicacion.md  
├─ 004-UPDATE
|    ├─ 001-Miniformulario.html 
|    └─ 002-procesamodificar.php  
└─ 001-Creamos base de datos de clientes.sql  
## 001-Creamos base de datos de clientes.sql
```

CREATE DATABASE IF NOT EXISTS empleados
    DEFAULT CHARACTER SET utf8mb4
    COLLATE utf8mb4_spanish_ci;

USE empleados;

DROP TABLE IF EXISTS empleados;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento VARCHAR(100)
);

-- 4. Insert sample data
INSERT INTO empleados (nombre, puesto, salario, fecha_contratacion, departamento) VALUES
('Ana Torres', 'Administrativa', 21000.00, '2021-03-15', 'Administración'),
('Luis Martínez', 'Desarrollador Backend', 32000.00, '2020-11-02', 'IT'),
('Marta López', 'Desarrolladora Frontend', 30000.00, '2022-01-10', 'IT'),
('Carlos Pérez', 'Comercial', 25000.00, '2019-07-08', 'Ventas'),
('Elena García', 'Marketing Specialist', 27000.00, '2021-09-23', 'Marketing'),
('Javier Ruiz', 'Técnico de Soporte', 24000.00, '2020-02-14', 'Soporte'),
('Patricia Sánchez', 'Recursos Humanos', 26000.00, '2018-06-20', 'RRHH'),
('Sergio Gómez', 'Data Analyst', 35000.00, '2022-05-01', 'Datos'),
('Raquel Navarro', 'Diseñadora UX/UI', 29000.00, '2021-12-01', 'IT'),
('David Fernández', 'Contable', 23000.00, '2019-10-30', 'Finanzas');


CREATE USER 
'empleados'@'localhost' 
IDENTIFIED  BY 'Empleados123$';

GRANT USAGE ON *.* TO 'empleados'@'localhost';

ALTER USER 'empleados'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON empleados.* 
TO 'empleados'@'localhost';

FLUSH PRIVILEGES;
```
## 001-Miniformulario.html 
```
<!doctype html>
<html lang="es">
  <head>
    <title>Jose Vicente Carratala</title>
    <meta charset="utf-8">
  </head>
  <body>
    <form action="002-procesamodificar.php" method="POST">
      <p>Introduce el ID del elemento que quieres modificar</p>
      <input type="number" name="id" placeholder="id">
      <input type="submit">
    </form>
  </body>
</html>
```
## 002-procesamodificar.php
```
<?php
  
  $nombre = $_POST['nombre'];
  $puesto = $_POST['puesto'];
  $salario = $_POST['salario'];
  $fecha_contratacion = $_POST['fecha_contratacion'];
  $departamento = $_POST['departamento'];
  
  $id = $_POST['id'];

	 
  $host = "localhost";
  $user = "empleados";
  $pass = "Empleados123$";
  $db   = "empleados";

  $conexion = new mysqli($host, $user, $pass, $db);

  $sql = "
  	 UPDATE empleados SET
     	nombre = '".$nombre."',
      puesto = '".$puesto."',
      salario = '".$salario."',
      fecha_contratacion = '".$fecha_contratacion."',
      departamento = '".$departamento."' 
      WHERE id = ".$id."
    ;
  ";
  $conexion->query($sql);
	
  $conexion->close();
  
?
```


# 4.-Cierre/Conclusión enlazando con la unidad



El ejercicio demuestra la importancia de la llave primaria (ID) para garantizar modificaciones precisas mediante la cláusula WHERE. Concluimos que la integración efectiva entre SQL, HTML y PHP es esencial para desarrollar aplicaciones web funcionales donde la información no solo se almacena, sino que se gestiona y actualiza de forma segura y persistent
