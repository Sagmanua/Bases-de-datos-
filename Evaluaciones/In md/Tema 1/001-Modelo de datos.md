##1. Introducción al Modelo de Datos
-

Primero, identificamos las entidades y sus atributos según lo que mencionaste:



## Entidad: Empresa
> - id_empresa (clave primaria)
> - nombre_empresa
> - direccion (opcional)
> - telefono (opcional)

## Entidad: Cliente
> - dni (clave primaria)
> - nombre
> - apellidos
> - email
id_empresa (clave foránea que indica a qué empresa pertenece)



##2. Desarrollo del Modelo: Diagrama Entidad-Relación (ERD)
-

## Empresa

id_empresa (PK)

nombre_empresa

direccion

telefono


## Cliente

|Clientes|
|:-------:|
|dni (PK)|
|nombre|
|apellidos|
|email|
|id_empresa (FK)|

# Diagrama ERD de Escuela

```mermaid
erDiagram
    EMPRESA {
        int id_empresa PK
        string nombre_empresa
        string direccion
        string telefono
    }

    CLIENTE {
        int dni PK
        string nombre
        string apellidos
        string email
        int id_empresa FK
    }

    EMPRESA ||--o{ CLIENTE : "tiene 1:N"

```









Relación:


Empresa 1 --- N Cliente


#3. Aplicación Práctica: Creación de la Base de Datos
-

```
-- Crear Basw de datos y usar ellos 
Create DATABASE 001_modello_de_datos;
USE 001_modello_de_datos;

```
```
-- Crear tabla Empresa
CREATE TABLE Empresa (
    id_empresa INT AUTO_INCREMENT,
    nombre_empresa VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(15),
    PRIMARY KEY (id_empresa)
);
```
| Column 1 | Column 2 | Column 3 |
|:-------- |:--------:| --------:|
| Left     | Center   | Right    |







| Field          | Type         | Null | Key | Default | Extra          |
|:----------------|:--------------:|:------:|:-----:|:---------:|:----------------:|
| id_empresa     | int          | NO   | PRI | NULL    | auto_increment |
| nombre_empresa | varchar(100) | NO   |     | NULL    |                |
| direccion      | varchar(200) | YES  |     | NULL    |                |
| telefono       | varchar(15)  | YES  |     | NULL    |                |


```
-- Crear tabla Cliente
CREATE TABLE Cliente (
    dni VARCHAR(10) PRIMARY KEY NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    id_empresa INT,
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);
```

| Field      | Type         | Null | Key | Default | Extra |
|:------------:|:--------------:|:------:|:-----:|:---------:|:-------:|
| dni        | varchar(10)  | NO   | PRI | NULL    |       |
| nombre     | varchar(50)  | NO   |     | NULL    |       |
| apellidos  | varchar(50)  | NO   |     | NULL    |       |
| email      | varchar(100) | YES  |     | NULL    |       |
| id_empresa | int          | YES  | MUL | NULL    |       |


```

-- Insertar algunos registros de ejemplo
INSERT INTO Empresa VALUES 
    (NULL, 'Tech Solutions', 'Calle Falsa 123', '555-1234'),
    (NULL, 'Innova Corp', 'Avenida Siempre Viva 456', '555-5678');
```

| id_empresa | nombre_empresa | direccion                | telefono |
|:------------:|:----------------:|:--------------------------:|:----------:|
|          1 | Tech Solutions | Calle Falsa 123          | 555-1234 |
|          2 | Innova Corp    | Avenida Siempre Viva 456 | 555-5678 |


```
INSERT INTO Cliente VALUES 
    ('12345678A', 'Juan', 'Pérez', 'juan.perez@email.com', 1),
    ('87654321B', 'Ana', 'Gómez', 'ana.gomez@email.com', 2),
    ('11223344C', 'Luis', 'Martínez', 'luis.martinez@email.com', 1);

```

| dni       | nombre | apellidos | email                   | id_empresa |
|:-----------:|:--------:|:-----------:|:-------------------------:|:------------:|
| 11223344C | Luis   | Martínez  | luis.martinez@email.com |          1 |
| 12345678A | Juan   | Pérez     | juan.perez@email.com    |          1 |
| 87654321B | Ana    | Gómez     | ana.gomez@email.com     |          2 |









