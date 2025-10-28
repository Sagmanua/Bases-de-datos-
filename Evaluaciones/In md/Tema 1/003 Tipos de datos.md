# Introduce de la practica 
En esta clase, aprenderás a definir tipos de datos como INT, VARCHAR y TEXT. También te enseñaremos cómo crear tablas en la base de datos y realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Vamos a trabajar con una tabla llamada clientes que incluye campos para el DNI, nombre, apellidos y email.

#  Aplicación Práctica: Creación de la Base de Datos
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

Cuando abre My sql voy a crear bases de daros para trabajar en ella 
```
Create DATABASE 003_Tipos_de_datos;
```

Abre este bases de datos que luego puedo trabajar en este bases de datos 
```
USE 003_Tipos_de_datos  ;
```

Create tabla de Clientes dni es primary key , id_empresa es Foreign key de tabla Empresa

#### Resultado en tabla 
   

#### EL codigo de tabla cliente

```
CREATE TABLE Clientes (
    dni VARCHAR(9) PRIMARY KEY ,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);
```
### Insertar values en la tabla Clientesç
```
INSERT INTO Clientes (dni, nombre, apellidos, email) VALUES
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com'),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com'),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com');

```
### Voy a ver como yo inserta values en la tabla Clientes  
```
SELECT * FROM Clientes;
```
| dni       | nombre | apellidos | email                   |
|:-----------:|:--------:|:-----------:|:-------------------------:|
| 11223344C | Luis   | Martínez  | luis.martinez@email.com |
| 12345678A | Juan   | Pérez     | juan.perez@email.com    | 
| 87654321B | Ana    | Gómez     | ana.gomez@email.com     |


### Ahora voy a  modificar esta tabla con UPDATE y DELETE
#### UPDATE 

UPDATE Clientes
SET dni = '87654321A',
    apellidos = 'López Martínez'
WHERE nombre = 'Juan


#### Delete  

DELETE FROM Clientes 
WHERE dni ='11223344C';


### Resultado 

| dni       | nombre | apellidos        | email                |
|:-----------:|:--------:|:------------------:|:----------------------:|
| 87654321A | Juan   | López Martínez   | juan.perez@email.com |
| 87654321B | Ana    | Gómez            | ana.gomez@email.com  |


# Codigo completa 
```

Create DATABASE 003_Tipos_de_datos;
USE 003_Tipos_de_datos;
CREATE TABLE Clientes (
    dni VARCHAR(9) PRIMARY KEY ,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);
INSERT INTO Clientes (dni, nombre, apellidos, email) VALUES
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com'),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com'),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com');

SELECT * FROM Clientes;
UPDATE Clientes
SET dni = '87654321A',
    apellidos = 'López Martínez'
WHERE nombre = 'Juan';
DELETE FROM Clientes 
WHERE dni ='11223344C';

```
# Conclusión enlazando con la actividad 

En este actividad he hecho una tarea tipo CRUD (Crear, LEER,  Actulizar y Eliminar). Este conocimintos es fundamental en MySql que deben tener todos que quire trabar con base de datos Dominar estas operaciones básicas te permitirá avanzar hacia el diseño de bases de datos más complejas, el uso de consultas avanzadas y la optimización de datos.
