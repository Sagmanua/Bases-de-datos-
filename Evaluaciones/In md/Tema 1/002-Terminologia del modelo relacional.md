# Introduce de la practica 
En este ejercicio vamos instllar Mysql y crear una base de datos en que vamos crear una tabla y en que vamos Añade registros a las tabla correspondiente, por ejemplo, inserta algunos clientes con sus respectivos atributos.Y todo eso para practicar en los conceptos de terminología del modelo relacional en MySQL






#  Aplicación Práctica: Creación de la Base de Datos

El primero que voy a hacer es abrir terminal y  descargar MySQL 
```
sudo apt install mysql-server
```


Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

Cuando abre My sql voy a crear bases de daros para trabajar en ella 
```
Create DATABASE empresadam ;
```

Abre este bases de datos que luego puedo trabajar en este bases de datos 
```
USE empresadam  ;
```

Create tabla de Cliente dni es primary key , id_empresa es Foreign key de tabla Empresa

#### Resultado en tabla 

| Field      | Type         | Null | Key | Default | Extra |
|:------------:|:--------------:|:------:|:-----:|:---------:|:-------:|
| dni        | varchar(10)  | NO   | PRI | NULL    |       |
| nombre     | varchar(50)  | NO   |     | NULL    |       |
| apellidos  | varchar(50)  | NO   |     | NULL    |       |
| email      | varchar(100) | YES  |     | NULL    |       |
| id_empresa | int          | YES  | MUL | NULL    |       |

#### EL codigo de tabla cliente

```
CREATE TABLE Cliente (
    dni VARCHAR(10) PRIMARY KEY ,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    id_empresa INT,
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);
```
### 6. Insertar values en la tabla Clientesç

#### El codigo
```
INSERT INTO Cliente VALUES 
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com', 1),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com', 2),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com', 1);

```
#### Resultado 

| dni       | nombre | apellidos | email                   |
|:-----------:|:--------:|:-----------:|:-------------------------:|
| 11223344C | Luis   | Martínez  | luis.martinez@email.com |
| 12345678A | Juan   | Pérez     | juan.perez@email.com    | 
| 87654321B | Ana    | Gómez     | ana.gomez@email.com     |


# Codigo completa 
```
sudo apt install mysql-server
Create DATABASE empresadam;
USE empresadam;
CREATE TABLE Cliente (
    dni VARCHAR(10) PRIMARY KEY ,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    email VARCHAR(100),
);
INSERT INTO Cliente VALUES 
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com',),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com',),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com',);
```

# Conclusión enlazando con la actividad 

En este ejercicio me ha hecho bases de datos completa con una tabla de cliente y inserta valores en este tabla  tam bien añade clave primaria y valor que no esta NUll. No creamos segunda tabla por eso no usamos claves foreneas.Este practica es fundamental para luegos trabajos y mis descansa para gurdar informacion ordenado 
