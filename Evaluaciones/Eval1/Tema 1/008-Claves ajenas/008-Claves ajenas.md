# Introduce de la practica 
En esta práctica se trabaja el concepto de claves ajenas en bases de datos relacionales. Se crean dos tablas: personas y emails, donde cada correo está vinculado a una persona.La clave ajena garantiza la integridad referencial entre ambas tablas.Se insertan datos en cada tabla respetando esta relación.Luego, se realiza una consulta con LEFT JOIN para combinar información de ambas tablas.Esto permite visualizar todos los correos asociados a cada persona, incluso si no tienen correo.El objetivo es comprender cómo las claves ajenas facilitan la relación y consistencia de los datos.
#  Aplicación Práctica
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### Abre este bases de datos que luego puedo trabajar en este bases de datos 

```
USE ejemploclaves;
```


### voy a crear tabla personas 

```
CREATE TABLE personas (
  nombre VARCHAR(50),
  apellidos VARCHAR(255)
);
```

### añado identificador
```
ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

### voy a ver si todo creado bien

```
DESCRIBE personas;
```

| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(50)  | YES  |     | NULL    |                |
| apellidos     | varchar(255) | YES  |     | NULL    |                |



### voy a crear tabla emails
```
CREATE TABLE emails (
  direccion VARCHAR(50),
  persona VARCHAR(255)
);
```

### añado identificador
```
ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```
### voy a ver si todo creado bien

```
DESCRIBE emails;
```

| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| direccion     | varchar(50)  | YES  |     | NULL    |                |
| persona       | varchar(255) | YES  |     | NULL    |                |


### inserta un persona 
```
INSERT INTO personas VALUES(
  NULL,
  'Jose Vicente',
  'Carratalá Sanchis'
);
``` 
### insert emails 
INSERT INTO emails VALUES(
  NULL,
  'info@jocarsa.com',
  1
);


INSERT INTO emails VALUES(
  NULL,
  'info@josevicentecarratala.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'jocarsa2@gmail.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'inventado',
  2
);


### usamos leftjoin para ver 2 tablas en mismo tiempo 

SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;


| identificador | direccion                     | persona | identificador | nombre       | apellidos          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
|             1 | info@jocarsa.com              | 1       |             1 | Jose Vicente | Carratalá Sanchis  |
|             2 | info@josevicentecarratala.com | 1       |             1 | Jose Vicente | Carratalá Sanchis  |
|             3 | jocarsa2@gmail.com            | 1       |             1 | Jose Vicente | Carratalá Sanchis  |
|             4 | inventado                     | 2       |          NULL | NULL         | NULL               |


# Codigo completa 
```
USE ejemploclaves;
CREATE TABLE personas (
  nombre VARCHAR(50),
  apellidos VARCHAR(255)
);
ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
DESCRIBE personas;
CREATE TABLE emails (
  direccion VARCHAR(50),
  persona VARCHAR(255)
);
ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
DESCRIBE emails;
INSERT INTO personas VALUES(
  NULL,
  'Jose Vicente',
  'Carratalá Sanchis'
);
INSERT INTO emails VALUES(
  NULL,
  'info@jocarsa.com',
  1
);
INSERT INTO emails VALUES(
  NULL,
  'info@josevicentecarratala.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'jocarsa2@gmail.com',
  1
);

INSERT INTO emails VALUES(
  NULL,
  'inventado',
  2
);
SELECT * FROM emails
LEFT JOIN personas
ON emails.persona = personas.Identificador;
```
# Conclusión enlazando con la actividad 
La práctica permitió comprender cómo las claves ajenas establecen relaciones entre tablas, garantizando la integridad de los datos.
Al crear las tablas personas y emails y vincularlas correctamente, se pudo observar cómo se mantiene la relación entre registros.
La inserción de datos y la consulta con LEFT JOIN demostraron cómo se pueden combinar datos de tablas relacionadas.
Se evidenció que incluso si una persona no tiene correo, la relación sigue siendo consistente.
En general, la actividad reforzó la importancia de las claves ajenas para organizar, relacionar y consultar información de manera eficiente en bases de datos relacionales
