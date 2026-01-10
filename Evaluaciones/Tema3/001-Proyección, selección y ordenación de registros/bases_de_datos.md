
# 1.-Indroduccion brece y contexalizacion
SQL  es el lenguaje estándar para gestionar bases de datos relacionales. Permite almacenar, consultar y organizar información de manera eficiente. Esta práctica se centra en los conceptos de proyección, selección y ordenación de registros, aplicándolos a una tabla de clientes para extraer y presentar datos de forma clara y útil.



# 2.-Desarrollo técnico correcto y preciso
## Primero pasos crear base de datos y Use ella 
```
CREATE DATABASE clientes;
USE clientes;
```
## creo yna tabla de cliente con columnas `nombre` `apellidos` y `edad`
CREATE TABLE clientes(
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  edad INT
);

## hago un insert in bases de datos
```
INSERT INTO clientes VALUES('Juan', 'Pérez', 30), ('Ana', 'López', 25), ('Pedro', 'Martínez', 40);
```
### hago un  `select` donde cambio 
* `nombre` a `Nombre del cliente` 
* `apellidos` a `Apellidos del cliente`
* `edad` a `Edad del cliente`
```

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;
```


| Nombre del cliente | Apellidos del cliente | Edad del cliente |
|--------------------|-----------------------|------------------|
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |


## hago un `SELECT` de toda tabla `clientes` 
```

  SELECT * FROM clientes;
```

| nombre | apellidos | edad |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |   30 |
| Ana    | López     |   25 |
| Pedro  | Martínez  |   40 |

### hago un  `select` donde cambio + ORDEN POR `apellidos`

* `nombre` a `Nombre del cliente` 
* `apellidos` a `Apellidos del cliente`
* `edad` a `Edad del cliente`

```

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos;
```

| Nombre del cliente | Apellidos del cliente | Edad del cliente |
|--------------------|-----------------------|------------------|
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |

### hago un  `select` donde cambio + ORDEN POR `edad` descendiendo a despues si tienes edad simular por  `apellidos` a (A → Z)

* `nombre` a `Nombre del cliente` 
* `apellidos` a `Apellidos del cliente`
* `edad` a `Edad del cliente`

```

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC, apellidos ASC;
```

| Nombre del cliente | Apellidos del cliente | Edad del cliente |
|--------------------|-----------------------|------------------|
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
### hago un  `select` donde cambio + ORDEN POR `edad` descendiendo 

* `nombre` a `Nombre del cliente` 
* `apellidos` a `Apellidos del cliente`
* `edad` a `Edad del cliente`
```

SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC;
```

| Nombre del cliente | Apellidos del cliente | Edad del cliente |
|--------------------|-----------------------|------------------|
| Pedro              | Martínez              |               40 |
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |

### ### hago un  `select` donde selectiona solo `nombre` y `apellidos`
```
SELECT 
  nombre,
  apellidos
FROM 
  clientes;
```

| nombre | apellidos |
|--------------------|-----------------------|
| Juan   | Pérez     |
| Ana    | López     |
| Pedro  | Martínez  |


SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;

### hago un  `select` donde cambio 
* `nombre` a `Nombre del cliente` 
* `apellidos` a `Apellidos del cliente`
* `edad` a `Edad del cliente`
| Nombre del cliente | Apellidos del cliente | Edad del cliente |
|--------------------|-----------------------|------------------|
| Juan               | Pérez                 |               30 |
| Ana                | López                 |               25 |
| Pedro              | Martínez              |               40 |




# Codigo Completo

```
CREATE DATABASE clientes;
USE clientes;

CREATE TABLE clientes(
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  edad INT
);
INSERT INTO clientes VALUES('Juan', 'Pérez', 30), ('Ana', 'López', 25), ('Pedro', 'Martínez', 40);
SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;
  SELECT * FROM clientes;
SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos;
  SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC, apellidos ASC;
  SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  apellidos ASC;
  SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes
ORDER BY
  edad DESC;
  SELECT 
  nombre,
  apellidos
FROM 
  clientes;
SELECT 
  nombre AS 'Nombre del cliente',
  apellidos AS 'Apellidos del cliente',
  edad AS 'Edad del cliente'
FROM 
  clientes;
```

# 4.-Cierre/Conclusión enlazando con la unidad

Los ejercicios realizados permiten comprender cómo seleccionar columnas específicas (proyección), filtrar registros (selección) y ordenar datos (ordenación). Estos fundamentos de SQL son esenciales para manejar bases de datos de forma efectiva y constituyen la base para consultas más complejas, reforzando los objetivos de la unidad.