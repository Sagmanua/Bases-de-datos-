# Introduce de la practica 







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

| Field      | Type         | Null | Key | Default | 
|:------------:|:--------------:|:------:|:-----:|:-------:|
| dni        | varchar(10)  | NO   | PRI | NULL    |       
| nombre     | varchar(50)  | NO   |     | NULL    |      
| apellidos  | varchar(50)  | NO   |     | NULL    |       
| email      | varchar(100) | YES  |     | NULL    |       
 |       

#### EL codigo de tabla cliente

```
CREATE TABLE Clientes (
    dni VARCHAR(9) PRIMARY KEY ,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);
```
### 6. Insertar values en la tabla Clientesç

#### El codigo
```
INSERT INTO Clientes VALUES 
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com', 1),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com', 2),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com', 1);

```
```
SELECT * FROM Clientes;
```
| dni       | nombre | apellidos | email                   |
|:-----------:|:--------:|:-----------:|:-------------------------:|
| 11223344C | Luis   | Martínez  | luis.martinez@email.com |
| 12345678A | Juan   | Pérez     | juan.perez@email.com    | 
| 87654321B | Ana    | Gómez     | ana.gomez@email.com     |

#### USTLIZAR UPDATE 

UPDATE Clientes
SET dni = '87654321A',
    apellidos = 'López Martínez'
WHERE nombre = 'Juan';


#### Delete  

DELETE FROM Clientes 
WHERE dni ='87654321A';


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

| dni       | nombre | apellidos        | email                |
|:-----------:|:--------:|:------------------:|:----------------------:|
| 87654321A | Juan   | López Martínez   | juan.perez@email.com |
| 87654321B | Ana    | Gómez            | ana.gomez@email.com  |



# Conclusión enlazando con la actividad 

En este ejercicio me ha hecho bases de datos completa con una tabla de cliente y inserta valores en este tabla  tam bien añade clave primaria y valor que no esta NUll. No creamos segunda tabla por eso no usamos claves foreneas.Este practica es fundamental para luegos trabajos y mis descansa para gurdar informacion ordenado 
