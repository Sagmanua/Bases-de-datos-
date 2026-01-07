Create DATABASE 007_valor_null;
USE 007_valor_null;


## Indroduccion brece y contexalizacion

En las bases de datos relacionales, las tablas organizan la información en filas y columnas. Un concepto clave es el valor NULL, que indica la ausencia o desconocimiento de un dato.

En esta práctica, se trabajará con la base de datos empresadam en MySQL para crear y consultar la tabla pedidos, insertando valores NULL para observar cómo se manejan dentro de una tabla.



## 2 Desarrollo técnico correcto y preciso

### Abre este bases de datos que luego puedo trabajar en este bases de datos 
```
USE empresadam;
```

### voy a ver que tablas tiene y su nombre 
```
SHOW TABLES;
```


| Tables_in_empresadam |
|:----------------------:|
| Cliente              |
| clientes             |


### crear tabla pedeidos
```
CREATE TABLE pedidos (
  numerodepedido VARCHAR(20) NOT NULL,
  cliente VARCHAR(50) NOT NULL,
  producto VARCHAR(255) NOT NULL
);
       
```
###
```
DESRIBE pedidos;
```

| Field          | Type         | Null | Key | Default | Extra |
|:----------------:|:--------------:|:------:|:-----:|:---------:|:-------:|
| numerodepedido | varchar(20)  | NO   |     | NULL    |       |
| cliente        | varchar(50)  | NO   |     | NULL    |       |
| producto       | varchar(255) | NO   |     | NULL    |       |





### Inserta values en la tabla pedidos
```
INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES ('P001', 'Cliente A', NULL);

```
### Resultado dame a error porque tabla de productos deben tener algo no esta null
Column 'producto' cannot be null

## Codigo Completo

```
USE empresadam;
SHOW TABLES;
CREATE TABLE pedidos (
  numerodepedido VARCHAR(20) NOT NULL,
  cliente VARCHAR(50) NOT NULL,
  producto VARCHAR(255) NOT NULL
);
DESRIBE pedidos;
INSERT INTO pedidos (numerodepedido, cliente, producto) VALUES ('P001', 'Cliente A', NULL);

```

## Cierre/Conclusión enlazando con la unidad


Este ejercicio permitió aplicar los conceptos de la unidad sobre estructuras de tablas y gestión de datos en bases de datos relacionales, comprendiendo el papel del valor NULL en la representación de información faltante. Al crear, insertar y consultar registros, se reforzó la importancia de definir correctamente los campos y entender cómo los valores NULL afectan las consultas y la integridad de los datos.