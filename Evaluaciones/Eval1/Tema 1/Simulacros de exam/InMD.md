
## 1.-Indroduccion brece y contexalizacion





## 2.-Desarrollo técnico correcto y preciso




```
mysql> SHOW DATABASES;
```
+--------------------+
| Database           |
+--------------------+
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| practica           |
| sys                |
+--------------------+

```
mysql> CREATE DATABASE portafolio;    
```

mysql> USE portafolio;


```
CREATE TABLE Categoria(
    Id_cat INT Primary Key,
    titulo_c VARCHAR(255),
    descripcion_c VARCHAR(255)
);

```
DESCRIBE Pieza;



| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Id_cat        | int          | NO   | PRI | NULL    |       |
| titulo_c      | varchar(255) | YES  |     | NULL    |       |
| descripcion_c | varchar(255) | YES  |     | NULL    |       |



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
mysql> DESCRIBE Pieza;

| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| id_pieza      | int          | NO   | PRI | NULL    |       |
| titulo_p      | varchar(255) | YES  |     | NULL    |       |
| descripcion_p | varchar(255) | YES  |     | NULL    |       |
| imagen        | varchar(255) | YES  |     | NULL    |       |
| url           | varchar(255) | YES  |     | NULL    |       |
| id_categoria  | int          | YES  | MUL | NULL    |       |



```
SELECT p.*, c.titulo_c, c.descripcion_c
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;

```


| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | id_categoria | titulo_c  | descripcion_c                          |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:--------------:|:-----------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador |            1 | Escultura | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    |            2 | Pintura   | Cuadros en óleo o acrílico             |



insertar valores
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

SHOW * FROM CatPIEz;



| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | titilo_categoria | descripcion_categoria                  |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador | Escultura        | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    | Pintura          | Cuadros en óleo o acrílico             |

## Codigo Completo

```

```

## 4.-Cierre/Conclusión enlazando con la unidad