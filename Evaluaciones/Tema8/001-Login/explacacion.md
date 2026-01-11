# 1.-Indroduccion brece y contexalizacion

Este ejercicio práctico enseña a crear un sistema de autenticación mediante el flujo: Base de Datos $\rightarrow$ Validación $\rightarrow$ Sesión.El objetivo es conectar PHP y MySQL para verificar identidades y proteger páginas privadas. Aprenderás a gestionar credenciales y a utilizar sesiones para restringir el acceso a usuarios no autorizados, garantizando que el flujo de entrada sea seguro y controlado.



# 2.-Desarrollo técnico correcto y preciso
## create_data_bases.sql 
### creo base de datos 
```
CREATE DATABASE IF NOT EXISTS superaplicacion
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE superaplicacion;
```
### creo tabla `usuarios`
```
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nombrecompleto VARCHAR(150) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
### hago insert 
```
INSERT INTO usuarios (usuario, contrasena, nombrecompleto, email) 
VALUES 
('jdoe88', '$2y$10$e0MYzXyjpJS7Pd0RVvHwHe.9Xy2k2r5W.XgM1iW2Y.f9v8g7h6i5j', 'John Doe', 'john.doe@example.com'),
('mgarcia', '$2y$10$K9R.I8L7M6N5O4P3Q2R1S0T9U8V7W6X5Y4Z3A2B1C0D9E8F7G6H5I', 'Maria Garcia', 'm.garcia@email.net'),
('tech_pro', '$2y$10$Z1X2C3V4B5N6M7L8K9J0H1G2F3D4S5A6Q7W8E9R0T1Y2U3I4O5P6Q', 'Alex Smith', 'alex.smith@techcorp.com');
INSERT INTO usuarios (usuario, contrasena, nombrecompleto, email) 
VALUES (
    'jlopez', 
    '$2y$10$S9.f8G7h6J5k4M3n2B1v0uP.O9i8u7y6t5r4e3w2q1aZ.XcVbNm', -- Este es el hash para '1234segura'
    'Juan Lopez', 
    'j.lopez@ejemplo.com'
)
```
### creo una user 
```
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
```

## 003-comprobacion exitosa.sql
### select para comprobacion 
```
SELECT 
*
FROM usuarios
WHERE
usuario = 'jlopez'
AND
contrasena = '1234segura';
```

## procesa.php  
### hago una conexion de la bases de datos
```
<?php
	session_start(); // Arranco una sesion
    $host = "localhost";
    $user = "superaplicacion";
    $pass = "Superaplicacion123$";
    $db   = "superaplicacion";

  $conexion = new mysqli($host, $user, $pass, $db);
```

### hago una Mysql request
```
    $sql = "
  	SELECT 
    *
    FROM usuarios
    WHERE
    usuario = '".$_POST['usuario']."'
    AND
    contrasena = '".$_POST['contrasena']."';
  ";
```
### declara variable de resùesta
```
  $resultado = $conexion->query($sql);
```
### hago HTTP request 
```
  if ($fila = $resultado->fetch_assoc()) {
```
### si tiene usario tiene mueve a `exito.php`
```
if ($fila = $resultado->fetch_assoc()) {
    $_SESSION['usuario'] = 'si';
    header("Location: exito.php");		
```
### en otro caso volver a este pagina
```
}else{															
header("Location: login.html");					
}
```

## exito.php  
### hago una session
```
session_start();
```
### si tiene usarionada paso
```
if(!isset($_SESSION['usuario'])){
```
### si no usa `die` 
```
die("Te has intentado colar, pero no ha colado");
```



# Codigo Completo
Project\  
├─ explicacion.md 
├─ 003-comprobacion exitosa.sql    
├─ create_data_bases.sql  
├─ exito.php  
└─ procesa.php  
## create_data_bases.sql 
```
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

INSERT INTO usuarios (usuario, contrasena, nombrecompleto, email) 
VALUES 
('jdoe88', '$2y$10$e0MYzXyjpJS7Pd0RVvHwHe.9Xy2k2r5W.XgM1iW2Y.f9v8g7h6i5j', 'John Doe', 'john.doe@example.com'),
('mgarcia', '$2y$10$K9R.I8L7M6N5O4P3Q2R1S0T9U8V7W6X5Y4Z3A2B1C0D9E8F7G6H5I', 'Maria Garcia', 'm.garcia@email.net'),
('tech_pro', '$2y$10$Z1X2C3V4B5N6M7L8K9J0H1G2F3D4S5A6Q7W8E9R0T1Y2U3I4O5P6Q', 'Alex Smith', 'alex.smith@techcorp.com');
INSERT INTO usuarios (usuario, contrasena, nombrecompleto, email) 
VALUES (
    'jlopez', 
    '$2y$10$S9.f8G7h6J5k4M3n2B1v0uP.O9i8u7y6t5r4e3w2q1aZ.XcVbNm', -- Este es el hash para '1234segura'
    'Juan Lopez', 
    'j.lopez@ejemplo.com'
)


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
```
## 003-comprobacion exitosa.sql
```
SELECT 
*
FROM usuarios
WHERE
usuario = 'jlopez'
AND
contrasena = '1234segura';
```
## procesa.php  
```
<?php
	session_start(); // Arranco una sesion
    $host = "localhost";
    $user = "superaplicacion";
    $pass = "Superaplicacion123$";
    $db   = "superaplicacion";

  $conexion = new mysqli($host, $user, $pass, $db);
    $sql = "
  	SELECT 
    *
    FROM usuarios
    WHERE
    usuario = '".$_POST['usuario']."'
    AND
    contrasena = '".$_POST['contrasena']."';
  ";
	
  $resultado = $conexion->query($sql);

  if ($fila = $resultado->fetch_assoc()) {
    $_SESSION['usuario'] = 'si';
    header("Location: exito.php");					
  }else{															
  	header("Location: login.html");					
  }

  $conexion->close();
  
?>
```
## exito.php 
```
<?php
	session_start();
  if(!isset($_SESSION['usuario'])){
  	die("Te has intentado colar, pero no ha colado");
  }
?>

Si estas viendo esto es que has entrado correctamente
``` 

# 4.-Cierre/Conclusión enlazando con la unidad
Este ejercicio cierra la unidad integrando PHP, MySQL y Manejo de Sesiones. Hemos transformado una base de datos estática en un sistema dinámico de control de acceso.

Lo más importante de esta práctica es comprender que la seguridad reside en la validación del lado del servidor: sin una sesión activa y verificada, el sistema garantiza la protección de la información, cumpliendo así con los estándares de autenticación web estudiados.



