# Introduce de la practica 
En esta práctica aprenderás a crear, gestionar y verificar claves primarias dentro de una base de datos relacional utilizando MySQL. Las claves primarias son un concepto fundamental en el diseño de bases de datos, ya que permiten identificar de forma única cada registro dentro de una tabla, evitando duplicidades y asegurando la integridad de los datos.


#  Aplicación Práctica
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 



Abre este bases de datos que luego puedo trabajar en este bases de datos 
```
USE empresadam;
```


Usamos este codigo para ve todos los tablas de basesa de datos empresadam
```
SHOW TABLES;
```

#### Que ver de tablas 
   

|empresadam  |
|:--------------------------------:|
| Clientes                       |
| clientes                       |




### Insertar values en la tabla Clientes
```
INSERT INTO clientes 
VALUES(
  NULL,
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);

```
### Voy a ver como yo inserta values en la tabla Clientes  
```
SELECT * FROM Clientes;
```
| id   | dni       | nombre | apellidos    | email            |
|:------:|:-----------:|:--------:|:--------------:|:------------------:|
| 2    | 12345679A | Juan   | Garcia Lopez | juan@jocarsa.com |




### Ahora voy Intentar insertar un registro con una clave primaria duplicada
#### Codigo

```
INSERT INTO clientes 
VALUES(
  2,
  '12345679A',
  'Juan',
  'Garcia Lopez',
  'juan@jocarsa.com'
);
```
### Resultado 
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'


# Codigo completa 
```
USE empresadam;
INSERT INTO clientes 
VALUES(
  1,
  '12345678A',
  'Jose Vicente',
  'Carratala Sanchis',
  'info@jocarsa.com'
);
INSERT INTO clientes 
VALUES(
  2,
  '12345679A',
  'Juan',
  'Garcia Lopez',
  'juan@jocarsa.com'
);

```
# Conclusión enlazando con la actividad 


A lo largo de esta práctica hemos podido comprobar la importancia de las claves primarias en el diseño y funcionamiento de una base de datos relacional. Al crear una columna autoincremental como clave primaria en la tabla clientes, se ha asegurado que cada registro quede identificado de manera única, evitando duplicidades y posibles inconsistencias en los datos.