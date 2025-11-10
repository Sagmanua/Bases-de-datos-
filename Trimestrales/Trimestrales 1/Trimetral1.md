# 1.-Indroduccion brece y contexalizacion
En el presente trabajo se desarrollará un ejemplo práctico relacionado con el diseño y gestión de bases de datos. Para ello, se crearán dos tablas: `categoriasportafolio` y `piezasportafolio`, donde la tabla entradas contendrá una clave foránea `(Foreign Key)` que relacionará cada entrada con su `categoriasportafolio` correspondiente. Posteriormente, se insertarán datos en ambas tablas y se realizará una consulta utilizando `LEFT JOIN` para observar la relación entre ellas. Finalmente, se creará una vista `(VIEW)` que permitirá visualizar de manera más clara y estructurada la información combinada


# 2.-Desarrollo técnico correcto y preciso
## Mysql
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

### Creo bases de datos con nombre de portafolioexamen
```
Create DATABASE portafolioexamen;
```
### Abro este bases de datos para trabajar en ella
```
USE portafolioexamen;
```
### Creo tabla de  `categoriasportafolio` con `PRIMARY KEY` 
```
CREATE TABLE categoriasportafolio (
    Identificador_categoria INT PRIMARY KEY ,
    nombre VARCHAR(50)
);
```
### Usa `DESCRIBE` para ver si gurda tofo vien o tiene errores
#### Codigo 
```
DESCRIBE categoriasportafolio;
```
#### Resultado
| Field                   | Type        | Null | Key | Default | Extra |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|
| Identificador_categoria | int         | NO   | PRI | NULL    |       |
| nombre                  | varchar(50) | YES  |     | NULL    |       |



### Creo tabla de  `piezasportafolio` con `PRIMARY KEY` y `FOREIGN KEY` que tiene referencia a tabla `categoriasportafolio`
```
CREATE TABLE piezasportafolio (
    Identificador_portfolio INT PRIMARY KEY ,
    titulo VARCHAR(50),
    descripcion VARCHAR(255),
    fecha VARCHAR(100),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador_categoria)
);
```
### Usa `DESCRIBE` para ver si gurda tofo vien o tiene errores
#### Codigo 
```
DESCRIBE piezasportafolio;
```
#### Resultado
| Field                   | Type         | Null | Key | Default | Extra |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|
| Identificador_portfolio | int          | NO   | PRI | NULL    |       |
| titulo                  | varchar(50)  | YES  |     | NULL    |       |
| descripcion             | varchar(255) | YES  |     | NULL    |       |
| fecha                   | varchar(100) | YES  |     | NULL    |       |
| id_categoria            | int          | YES  | MUL | NULL    |       |



### Insetartas valores en la tabla `piezasportafolio`
```
INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion,fecha,id_categoria)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera',' 2025/10/11', 1 );

INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion, fecha, id_categoria)
VALUES (2, 'Pintura al óleo', 'Retratos y paisajes pintados con óleo sobre lienzo', '2025/08/05', 2);

INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion, fecha, id_categoria)
VALUES (3, 'Diseño digital', 'Ilustraciones digitales y composiciones gráficas', '2025/12/21', 3);
```
### Leer datos de la tabla `piezasportafolio` va ver si guarda todo vien 
#### Codigo 
```
SELECT * FROM piezasportafolio ;
```
#### Resultado
| Identificador_portfolio | titulo           | descripcion                                         | fecha       | id_categoria |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|
|                       1 | Escultura        | Obras hechas en piedra, metal o madera              |  2025/10/11 |            1 |
|                       2 | Pintura al óleo  | Retratos y paisajes pintados con óleo sobre lienzo  | 2025/08/05  |            2 |
|                       3 | Diseño digital   | Ilustraciones digitales y composiciones gráficas    | 2025/12/21  |            3 |

###  Insetartas valores en la tabla `piezasportafolio`

```
INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (1, 'Bohdan');

INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (2, 'Marketing');

INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (3, 'Desarrollo');
```
### Leer datos de la tabla `categoriasportafolio` va ver si guarda todo vien 
#### Codigo
```
SELECT * FROM categoriasportafolio;
```
#### Resultado 
| Identificador_categoria | nombre     |
|:----------:|:---------------------:|
| Bohdan     |
|                       2 | Marketing  |
|                       3 | Desarrollo |


### LEft join para ver 2 tablas en el mismo tiempo 
#### Codigo
```
SELECT p.*, p.titulo, p.descripcion
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c ON p.id_categoria = c.Identificador_categoria;
```
#### Resultado
| Identificador_portfolio | titulo           | descripcion                                         | fecha       | id_categoria | titulo           | descripcion                                         |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|:----------:|
|                       1 | Escultura        | Obras hechas en piedra, metal o madera              |  2025/10/11 |            1 | Escultura        | Obras hechas en piedra, metal o madera              |
|                       2 | Pintura al óleo  | Retratos y paisajes pintados con óleo sobre lienzo  | 2025/08/05  |            2 | Pintura al óleo  | Retratos y paisajes pintados con óleo sobre lienzo  |
|                       3 | Diseño digital   | Ilustraciones digitales y composiciones gráficas    | 2025/12/21  |            3 | Diseño digital   | Ilustraciones digitales y composiciones gráficas    |


### VISTA usa para ver 2 tablas pero es gurda como tabla y puedo llamar cuando quiero
```
CREATE VIEW CatPIEz AS 
SELECT
    p.Identificador_portfolio,
    p.titulo,
    p.descripcion,
    p.fecha,
    p.id_categoria,
    c.nombre
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c 
    ON p.id_categoria = c.Identificador_categoria;
```
### Ahora voy a llamar VISTA `CatPIEz` que es left join para ver 2 tablas en mismo tiempo
#### Codigo
```
SELECT * FROM CatPIEz;
```
#### Resultado
| Identificador_portfolio | titulo           | descripcion                                         | fecha       | id_categoria | nombre     |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|
|                       1 | Escultura        | Obras hechas en piedra, metal o madera              |  2025/10/11 |            1 | Bohdan     |
|                       2 | Pintura al óleo  | Retratos y paisajes pintados con óleo sobre lienzo  | 2025/08/05  |            2 | Marketing  |
|                       3 | Diseño digital   | Ilustraciones digitales y composiciones gráficas    | 2025/12/21  |            3 | Desarrollo |

### Actilizar los datos de la tabla `piezasportafolio`
```
UPDATE piezasportafolio
SET titulo = 'Es es nuevo titilo'
WHERE Identificador_portfolio = 1 ;
```

Rows matched: 1  Changed: 1  Warnings: 0
### voy a ver cambias en la tabla 
```
SELECT * FROM piezasportafolio;
```

| Identificador_portfolio | titulo             | descripcion                                         | fecha       | id_categoria |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|
|                       1 | Es es nuevo titilo | Obras hechas en piedra, metal o madera              |  2025/10/11 |            1 |
|                       2 | Pintura al óleo    | Retratos y paisajes pintados con óleo sobre lienzo  | 2025/08/05  |            2 |
|                       3 | Diseño digital     | Ilustraciones digitales y composiciones gráficas    | 2025/12/21  |            3 |


### Delete  borar datos en la tabla `piezasportafolio`
```
DELETE FROM piezasportafolio 
WHERE Identificador_portfolio =2;
```
### voy a ver cambias en la tabla 
#### Codigo
```
SELECT * FROM piezasportafolio;
```
#### Resultado
| Identificador_portfolio | titulo             | descripcion                                       | fecha       | id_categoria |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|
|                       1 | Es es nuevo titilo | Obras hechas en piedra, metal o madera            |  2025/10/11 |            1 |
|                       3 | Diseño digital     | Ilustraciones digitales y composiciones gráficas  | 2025/12/21  |            3 |

### voy a ver que usario tiene mysql

```
SELECT User, Host FROM mysql.user;
```
### Resultado
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+

### despues de veo usario crear nuevo user 
```
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'password123';
```
#### en resultado tiene problema de contrsena no tiene contresaña bien
```
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```
### voy a ver reqesitos de contraseña 
```
SHOW VARIABLES LIKE 'validate_password%';
```
| Variable_name                                   | Value  |
|:-------------------------------------------------:|:--------:|
| validate_password.changed_characters_percentage | 0      |
| validate_password.check_user_name               | ON     |
| validate_password.dictionary_file               |        |
| validate_password.length                        | 8      |
| validate_password.mixed_case_count              | 1      |
| validate_password.number_count                  | 1      |
| validate_password.policy                        | MEDIUM |
| validate_password.special_char_count            | 1      |

### vale ahora voy esribir contaraseña correcta
```
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'Qwerty123!';
```
### da a usario priveges de administrador
```
GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'someone'@'localhost';
```
### guardar usario
```
FLUSH PRIVILEGES;
```

### voe que priveges tiene este usario
```
SHOW GRANTS FOR 'someone'@'localhost';
```

# Codigo Completo

```
Create DATABASE portafolioexamen;
USE portafolioexamen;
CREATE TABLE categoriasportafolio (
    Identificador_categoria INT PRIMARY KEY ,
    nombre VARCHAR(50)
);
DESCRIBE categoriasportafolio;
CREATE TABLE piezasportafolio (
    Identificador_portfolio INT PRIMARY KEY ,
    titulo VARCHAR(50),
    descripcion VARCHAR(255),
    fecha VARCHAR(100),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES categoriasportafolio(Identificador_categoria)
);
DESCRIBE piezasportafolio;
INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion,fecha,id_categoria)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera',' 2025/10/11', 1 );

INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion, fecha, id_categoria)
VALUES (2, 'Pintura al óleo', 'Retratos y paisajes pintados con óleo sobre lienzo', '2025/08/05', 2);

INSERT INTO piezasportafolio (Identificador_portfolio, titulo, descripcion, fecha, id_categoria)
VALUES (3, 'Diseño digital', 'Ilustraciones digitales y composiciones gráficas', '2025/12/21', 3);

SELECT * FROM piezasportafolio ;
INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (1, 'Bohdan');

INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (2, 'Marketing');

INSERT INTO categoriasportafolio (Identificador_categoria, nombre)
VALUES (3, 'Desarrollo');

SELECT * FROM categoriasportafolio;

SELECT p.*, p.titulo, p.descripcion
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c ON p.id_categoria = c.Identificador_categoria;

CREATE VIEW CatPIEz AS 
SELECT
    p.Identificador_portfolio,
    p.titulo,
    p.descripcion,
    p.fecha,
    p.id_categoria,
    c.nombre
FROM piezasportafolio p
LEFT JOIN categoriasportafolio c 
    ON p.id_categoria = c.Identificador_categoria;
SELECT * FROM CatPIEz;
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'password123';
SHOW VARIABLES LIKE 'validate_password%';
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'Qwerty123!';
GRANT ALL PRIVILEGES ON portafolioexamen.* TO 'someone'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'someone'@'localhost';
UPDATE piezasportafolio
SET titulo = 'Es es nuevo titilo'
WHERE Identificador_portfolio = 1 ;
SELECT * FROM piezasportafolio;
DELETE FROM piezasportafolio 
WHERE Identificador_portfolio =2;
SELECT * FROM piezasportafolio;
```

# 4.-Cierre/Conclusión enlazando con la unidad
La construcción y gestión de las tablas `categoriasportafolio` y `piezasportafolio`, junto con la definición de una clave foránea para relacionarlas, ha permitido comprender de forma práctica cómo se establecen y mantienen las relaciones dentro de una base de datos relacional. Además, el uso de consultas LEFT JOIN y la creación de una vista (VIEW) han facilitado la visualización integrada de los datos, mostrando cómo las relaciones permiten obtener información más completa y significativa. Este trabajo refuerza los contenidos de la unidad, especialmente en lo referente al diseño lógico, integridad referencial y consultas avanzadas en SQL, aspectos fundamentales para la administración eficiente de bases de datos.



