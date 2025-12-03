

## 1.-Indroduccion brece y contexalizacion
En el presente trabajo se desarrollará un ejemplo práctico relacionado con el diseño y gestión de bases de datos. Para ello, se crearán dos tablas: `autores` y `entradas`, donde la tabla entradas contendrá una clave foránea `(Foreign Key)` que relacionará cada entrada con su autor correspondiente. Posteriormente, se insertarán datos en ambas tablas y se realizará una consulta utilizando `LEFT JOIN` para observar la relación entre ellas. Finalmente, se creará una vista `(VIEW)` que permitirá visualizar de manera más clara y estructurada la información combinada


## 2.-Desarrollo técnico correcto y preciso
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### Creo bases de datos 
```
CREATE DATABASE blog2;
```

### Abro bases de datos donte esta tablas que nesisito que luego puedo trabajar en este bases de datos  

```
USE blog2;
```

### Creo tabla de autores
```
CREATE TABLE autores (
  Identificador INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);
```

### voy a ver si todo creado bien sin error 
```
DESCRIBE autores;
```
| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
| apellidos     | varchar(100) | YES  |     | NULL    |                |
| email         | varchar(100) | YES  |     | NULL    |                |


### Creo la tabla entradas con los campos Identificador, titulo, fecha, imagen, id_autor y contenido. Asegúrato de que id_autor sea una

```
CREATE TABLE entradas (
  Identificador INT AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha VARCHAR(100),
  imagen VARCHAR(100),
  id_autor INT,
  contenido TEXT,
  PRIMARY KEY (Identificador)
);
```
### voy a ver si todo creado bien sin error 
```
DESCRIBE entradas;
```
| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| titulo        | varchar(100) | YES  |     | NULL    |                |
| fecha         | varchar(100) | YES  |     | NULL    |                |
| imagen        | varchar(100) | YES  |     | NULL    |                |
| id_autor      | int          | YES  |     | NULL    |                |
| contenido     | text         | YES  |     | NULL    |                |


### Añado una clave foránea a la tabla entradas que haga referencia al campo id_autor en la tabla autores.

```
ALTER TABLE entradas  
ADD CONSTRAINT autores_a_entradas  
FOREIGN KEY (id_autor)  
REFERENCES autores(Identificador) 
ON DELETE CASCADE 
ON UPDATE CASCADE;
```
### voy a ver si todo creado bien sin error 
DESCRIBE autores;

| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(100) | YES  |     | NULL    |                |
| apellidos     | varchar(100) | YES  |     | NULL    |                |
| email         | varchar(100) | YES  |     | NULL    |                |

### Inserto un autor de prueba en la tabla autores.

```
INSERT INTO autores VALUES(
  NULL,
  'Jose Vicente',
  'Carratala',
  'info@jocarsa.com'
);
```
### voy a ver si inserto bien 
SELECT * FROM autores;
| Identificador | nombre       | apellidos | email            |
|:---------------:|:--------------:|:------:|:-----:|
|             1 | Jose Vicente | Carratala | info@jocarsa.com |



### Inserto una entrada en la tabla entradas asociada al autor anterior.

```
INSERT INTO entradas VALUES(
  NULL,
  'Titulo de la primera entrada',
  '2025-11-03',
  'imagen.jpg',
  1,
  'Este es el contenido de la primera entrada'
);
```
### voy a ver si inserto bien 
```
SELECT * FROM entradas;
``` 
| Identificador | titulo                       | fecha      | imagen     | id_autor | contenido                                  |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
|             1 | Titulo de la primera entrada | 2025-11-03 | imagen.jpg |        1 | Este es el contenido de la primera entrada |



### Realiza una consulta cruzada entre las tablas entradas y autores para obtener los detalles de las entradas junto con los datos del autor.


```
SELECT 
  entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
  autores.nombre, autores.apellidos 
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
```

### Crea una vista vista_entradas que combine los datos de las tablas entradas y autores.
```
CREATE VIEW vista_entradas AS 
SELECT 
  entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
  autores.nombre, autores.apellidos 
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
```

### Consulta la vista para obtener los datos combinados.
```
SELECT * FROM vista_entradas;
```

| titulo                       | fecha      | imagen     | contenido                                  | nombre       | apellidos |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Titulo de la primera entrada | 2025-11-03 | imagen.jpg | Este es el contenido de la primera entrada | Jose Vicente | Carratala |



## Codigo Completo

```
CREATE DATABASE blog2;
USE blog2;
CREATE TABLE autores (
  Identificador INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100),
  email VARCHAR(100)
);
DESCRIBE autores;
CREATE TABLE entradas (
  Identificador INT AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha VARCHAR(100),
  imagen VARCHAR(100),
  id_autor INT,
  contenido TEXT,
  PRIMARY KEY (Identificador)
);
DESCRIBE entradas;
ALTER TABLE entradas  
ADD CONSTRAINT autores_a_entradas  
FOREIGN KEY (id_autor)  
REFERENCES autores(Identificador) 
ON DELETE CASCADE 
ON UPDATE CASCADE;
DESCRIBE autores;
INSERT INTO autores VALUES(
  NULL,
  'Jose Vicente',
  'Carratala',
  'info@jocarsa.com'
);
SELECT * FROM autores;
INSERT INTO entradas VALUES(
  NULL,
  'Titulo de la primera entrada',
  '2025-11-03',
  'imagen.jpg',
  1,
  'Este es el contenido de la primera entrada'
);
SELECT * FROM entradas;
SELECT 
  entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
  autores.nombre, autores.apellidos 
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
CREATE VIEW vista_entradas AS 
SELECT 
  entradas.titulo, entradas.fecha, entradas.imagen, entradas.contenido,
  autores.nombre, autores.apellidos 
FROM entradas
LEFT JOIN autores
ON entradas.id_autor = autores.Identificador;
SELECT * FROM vista_entradas;
```

## 4.-Cierre/Conclusión enlazando con la unidad

La construcción y gestión de las tablas autores y entradas, junto con la definición de una clave foránea para relacionarlas, ha permitido comprender de forma práctica cómo se establecen y mantienen las relaciones dentro de una base de datos relacional. Además, el uso de consultas LEFT JOIN y la creación de una vista (VIEW) han facilitado la visualización integrada de los datos, mostrando cómo las relaciones permiten obtener información más completa y significativa. Este trabajo refuerza los contenidos de la unidad, especialmente en lo referente al diseño lógico, integridad referencial y consultas avanzadas en SQL, aspectos fundamentales para la administración eficiente de bases de datos.