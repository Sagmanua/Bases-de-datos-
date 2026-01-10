
# 1.-Indroduccion brece y contexalizacion

Para practicar los conceptos de redondeos y consultas en una base de datos utilizando SQL y Python, sigue estos pasos:


# 2.-Desarrollo técnico correcto y preciso
## 003-entramos y pedimos.sql
### abro mysql y abro base de datos `clientes`

```
-- sudo mysql -u root -p
USE clientes;
```

### hago una `SELECT` a todos los datos de clientes
```
mysql> SELECT
    -> *
    -> FROM clientes;
```
+--------+-----------+------+
| nombre | apellidos | edad |
+--------+-----------+------+
| Juan   | Pérez     |   30 |
| Ana    | López     |   25 |
| Pedro  | Martínez  |   40 |
+--------+-----------+------+

### creo una user de mysql para 008-conecto a bases de datos.py
```
mysql> CREATE USER 'clientes'@'localhost' IDENTIFIED BY 'Clientes123$';

mysql> GRANT ALL PRIVILEGES ON clientes.* TO 'clientes'@'localhost';

mysql> FLUSH PRIVILEGES;
``` 

## 007-redondeos.sql
### hago un `SELECT` y selcta avd edad de clientes con `ROUND`

```
SELECT
    ROUND(AVG(edad))
FROM clientes;
```



| ROUND(AVG(edad)) |
|------------------|
|               32 |



### hago un `SELECT` y selcta avd edad de clientes con `FLOOR`
```
SELECT
    FLOOR(AVG(edad))
FROM clientes;
```

| FLOOR(AVG(edad)) |
|------------------|
|               31 |


### hago un `SELECT` y selcta avd edad de clientes con `CEIL`
```
SELECT
    CEIL(AVG(edad))
FROM clientes;
```

| CEIL(AVG(edad)) |
|-----------------|
|              32 |


## 008-conecto a bases de datos.py
### import  `mysql.connector` 
```
import mysql.connector 
```
### conecta a bases de datos 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()        
```
### crear codigo para ejectar en base de datos
```
cursor.execute('''
  SELECT 
    FLOOR(AVG(edad))
  FROM clientes;
''')  
```
### crear variable para mostar response de base de datos y imprimir en console
```
filas = cursor.fetchall()

print(filas)
```


# Codigo Completo
Project\
├─ explicacion.md 
├─ 003-entramos y pedimos.sql  
├─ 008-conecto a bases de datos.py
└─ 007-redondeos.sql

## 003-entramos y pedimos.sql
```
-- sudo mysql -u root -p

USE clientes;

SELECT 
* 
FROM clientes;

mysql> CREATE USER 'clientes'@'localhost' IDENTIFIED BY 'Clientes123$';

mysql> GRANT ALL PRIVILEGES ON clientes.* TO 'clientes'@'localhost';

mysql> FLUSH PRIVILEGES;
```
## 007-redondeos.sql
```
-- sudo mysql -u root -p

USE clientes;

SELECT 
    ROUND(AVG(edad))
FROM clientes;

SELECT 
    FLOOR(AVG(edad))
FROM clientes;

SELECT 
    CEIL(AVG(edad))
FROM clientes;
```
## 008-conecto a bases de datos.py
```
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)                                      
  
cursor = conexion.cursor() 
cursor.execute('''
  SELECT 
    FLOOR(AVG(edad))
  FROM clientes;
''')  

filas = cursor.fetchall()

print(filas)
```

# 4.-Cierre/Conclusión enlazando con la unidad


Siguiendo estos pasos, podrás practicar los conceptos de redondeos y consultas en una base de datos utilizando SQL y Python. Recuerda que la práctica es clave para dominar estos temas, así que asegúrate de ejecutar todos los ejercicios con cuidado y entender el resultado de cada consulta.

