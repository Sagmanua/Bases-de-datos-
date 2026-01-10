# 1.-Indroduccion brece y contexalizacion
SQL permite manipular y consultar datos en bases de datos. Los operadores aritméticos, como suma, resta, multiplicación y división, facilitan trabajar con valores numéricos. En esta práctica se aplicarán sobre la columna edad de la tabla clientes para comprender cómo transformar y analizar información de manera sencilla.




# 2.-Desarrollo técnico correcto y preciso
## Conéctate a tu base de datos clientes usando el comando:
```
-- sudo mysql -u root -p

USE clientes;

```
## hago un `SELECT` de toda tabla `clientes` 
```
  SELECT * FROM clientes;
```
| nombre | apellidos | edad |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |   30 |
| Ana    | López     |   25 |
| Pedro  | Martínez  |   40 |
## hago un `SELECT` pero Agregaré 500 con `edad`


```
SELECT nombre, apellidos, edad + 500 FROM clientes;
```
| nombre | apellidos | edad + 500 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |        530 |
| Ana    | López     |        525 |
| Pedro  | Martínez  |        540 |
## hago un `SELECT` pero disminue 500 con `edad`

```
SELECT nombre, apellidos, edad - 500 FROM clientes;
```

| nombre | apellidos | edad - 500 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |       -470 |
| Ana    | López     |       -475 |
| Pedro  | Martínez  |       -460 |
## hago un `SELECT` pero multiplica 500 con `edad`

```
SELECT nombre, apellidos, edad * 500 FROM clientes;
```


| nombre | apellidos | edad * 500 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |      15000 |
| Ana    | López     |      12500 |
| Pedro  | Martínez  |      20000 |
## hago un `SELECT` pero Divide 500 con `edad`

```
SELECT nombre, apellidos, edad / 500 FROM clientes;
```
| nombre | apellidos | edad / 500 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |     0.0600 |
| Ana    | López     |     0.0500 |
| Pedro  | Martínez  |     0.0800 |

## hago un `SELECT` pero Agregaré 288 con `edad`
```
 SELECT nombre, apellidos, edad + 288 FROM clientes;
```
| nombre | apellidos | edad + 288 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |        318 |
| Ana    | López     |        313 |
| Pedro  | Martínez  |        328 |
## hago un `SELECT` pero disminue 228 con `edad`
```
SELECT nombre, apellidos, edad - 228 FROM clientes;
```
| nombre | apellidos | edad - 228 |
|--------------------|-----------------------|------------------|
| Juan   | Pérez     |       -198 |
| Ana    | López     |       -203 |
| Pedro  | Martínez  |       -188 |

# Codigo Completo


-- sudo mysql -u root -p

USE clientes;

SELECT * FROM clientes;
SELECT nombre, apellidos, edad + 500 FROM clientes;
SELECT nombre, apellidos, edad - 500 FROM clientes;
SELECT nombre, apellidos, edad * 500 FROM clientes;
SELECT nombre, apellidos, edad / 500 FROM clientes;
SELECT nombre, apellidos, edad + 288 FROM clientes;
SELECT nombre, apellidos, edad - 228 FROM clientes;
# 4.-Cierre/Conclusión enlazando con la unidad
Recuerda que el objetivo es entender cómo aplicar estos operadores para manipular y consultar datos numéricos en tus tablas. ¡Buena práctica!




