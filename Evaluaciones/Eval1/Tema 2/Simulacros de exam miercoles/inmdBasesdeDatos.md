
# 1.-Indroduccion brece y contexalizacion
En este simulacro de examen vamos a abordar un problema común: diseñar un portafolio que cuente con una parte visible al público general (sitio web) y un panel de administración interna. El objetivo de esta práctica es prepararnos para el próximo examen de Bases de Datos, enfocándonos en cómo crear y relacionar tablas, así como en la construcción de vistas (views) para consultas más eficientes.Durante la practica apredemos
Crear dos tablas relacionadas, donde una contendrá una clave foránea (Foreign Key) que establece la relación entre ellas.

Realizar un LEFT JOIN para combinar los datos de ambas tablas y obtener información completa de cada pieza junto con su categoría.

Crear una vista (view) basada en ese JOIN, facilitando la consulta y presentación de los datos de manera organizada.



# 2.-Desarrollo técnico correcto y preciso
## Crear bases de datos en Mysql
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### ahora veo que bases de datos tiene 
```
SHOW DATABASES;
```
| Database           |
|:--------------------:|
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| practica           |
| sys                |

### Creo bases de datos con nombre de portafolio
```
CREATE DATABASE portafolio;    
```
### Abrir bases de dattos para trabajar en ella 
```
USE portafolio;
```
### crear tabla de Categoria
#### codigo
```
CREATE TABLE Categoria(
    Id_cat INT Primary Key,
    titulo_c VARCHAR(255),
    descripcion_c VARCHAR(255)
);
```
### pronar si todo pasar bien
```
DESCRIBE Categoria;
```

| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Id_cat        | int          | NO   | PRI | NULL    |       |
| titulo_c      | varchar(255) | YES  |     | NULL    |       |
| descripcion_c | varchar(255) | YES  |     | NULL    |       |


### Ahora crear Pieza con `FOREIGN KEY`de tabla `Categoria`
```
CREATE TABLE Pieza(
    id_pieza INT Primary Key,
    titulo_p VARCHAR(255),
    descripcion_p VARCHAR(255),
    imagen VARCHAR(255),
    url VARCHAR(255),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES Categoria(Id_cat)
);
```
### pronar si todo pasar bien
```
DESCRIBE Pieza;
```

| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| id_pieza      | int          | NO   | PRI | NULL    |       |
| titulo_p      | varchar(255) | YES  |     | NULL    |       |
| descripcion_p | varchar(255) | YES  |     | NULL    |       |
| imagen        | varchar(255) | YES  |     | NULL    |       |
| url           | varchar(255) | YES  |     | NULL    |       |
| id_categoria  | int          | YES  | MUL | NULL    |       |




### Para probar Lrft join voy crear alqunas insertas en tabla   
```
INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera');

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (2, 'Pintura', 'Cuadros en óleo o acrílico');
```

```
INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (1, 'El Pensador', 'Escultura de Rodin', 'pensador.jpg', 'http://ejemplo.com/pensador', 1);

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (2, 'La Noche Estrellada', 'Pintura de Van Gogh', 'noche.jpg', 'http://ejemplo.com/noche', 2);
```
### despues de inserto valores en tablas voy a hacer Left join
```
SELECT p.*, c.titulo_c, c.descripcion_c
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
```
#### Resultado 
| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | id_categoria | titulo_c  | descripcion_c                          |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:--------------:|:-----------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador |            1 | Escultura | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    |            2 | Pintura   | Cuadros en óleo o acrílico             |


### Ahora voy a crear view de 2 tablas Lrft join
```
CREATE VIEW CatPIEz AS 
SELECT
p.id_pieza,
p.titulo_p,
p.descripcion_p,
p.imagen,
p.url,
c.titulo_C AS titilo_categoria ,
c.descripcion_c as descripcion_categoria
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
```
### Despues de crear view `CatPIEz` voy var si todo funciona
```
SHOW * FROM CatPIEz;
```

| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | titilo_categoria | descripcion_categoria                  |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador | Escultura        | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    | Pintura          | Cuadros en óleo o acrílico             |

# Codigo Completo
## MYSQL
```
SHOW DATABASES;
CREATE DATABASE portafolio;
USE portafolio;
CREATE TABLE Categoria(
    Id_cat INT Primary Key,
    titulo_c VARCHAR(255),
    descripcion_c VARCHAR(255)
);
CREATE TABLE Pieza(
    id_pieza INT Primary Key,
    titulo_p VARCHAR(255),
    descripcion_p VARCHAR(255),
    imagen VARCHAR(255),
    url VARCHAR(255),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES Categoria(Id_cat)
);
DESCRIBE Categoria;
DESCRIBE Pieza;

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera');

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (2, 'Pintura', 'Cuadros en óleo o acrílico');

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (1, 'El Pensador', 'Escultura de Rodin', 'pensador.jpg', 'http://ejemplo.com/pensador', 1);

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (2, 'La Noche Estrellada', 'Pintura de Van Gogh', 'noche.jpg', 'http://ejemplo.com/noche', 2);
SELECT p.*, c.titulo_c, c.descripcion_c
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
CREATE VIEW CatPIEz AS 
SELECT
p.id_pieza,
p.titulo_p,
p.descripcion_p,
p.imagen,
p.url,
c.titulo_C AS titilo_categoria ,
c.descripcion_c as descripcion_categoria
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
SHOW * FROM CatPIEz;
```
# 4.-Cierre/Conclusión enlazando con la unidad
En conclusión, la práctica realizada permite consolidar los conceptos fundamentales de la unidad de Bases de Datos Relacionales. Crear tablas y definir claves primary y foraneas. Como crear Left join y Vistas de los tabla para obtner informcaion de 2 tablas en par ver mejor relacion detro este 2 tablas.Al implementar un portafolio con una parte pública y un panel administrativo interno, se evidencia la importancia de un diseño de base de datos eficiente y bien estructurado, que garantice la integridad de los datos y facilite su consulta.