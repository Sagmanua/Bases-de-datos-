# 1.-Indroduccion brece y contexalizacion

Este proyecto demuestra la creación de una aplicación web dinámica mediante la integración de una base de datos SQL y el framework Flask.

El objetivo es automatizar la visualización de matrículas escolares, conectando un almacenamiento relacional con una interfaz de usuario. Se cubre el ciclo completo de datos: Almacenamiento (MySQL/SQLite), Lógica (Python) y Presentación (HTML).



# 2.-Desarrollo técnico correcto y preciso
## 001-creamos una base de datos.sql 
### crear bases de datos
```
sudo mysql -u root -p

CREATE DATABASE composiciones;

USE composiciones;
```
### denteo de bases de datos `composiciones` hago tablas
* alumnos
* profesores
* asignaturas
* matriculas
```
CREATE TABLE alumnos(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE profesores(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE asignaturas(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  id_profesor INT
);

CREATE TABLE matriculas(
	Identificador INT PRIMARY KEY,
  id_asignatura INT,
  id_alumno INT
);
```
## 002-datos de muestra.sql
### hago una insert in todos los tablas
```
INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1,'Ana','García López'),
(2,'Luis','Martínez Pérez'),
(3,'María','Sánchez Ruiz'),
(4,'Javier','Fernández Gómez'),
(5,'Laura','Díaz Ortega'),
(6,'Carlos','Romero Torres'),
(7,'Elena','Navarro Martínez'),
(8,'Pablo','Hernández Soto'),
(9,'Sofía','Iglesias Navarro'),
(10,'Miguel','Castro León'),
(11,'Clara','Vidal Serrano'),
(12,'Diego','Morales Rivas'),
(13,'Lucía','Cano Torres'),
(14,'Adrián','Herrero Gil'),
(15,'Nuria','Requena Soler');

INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(1,'Juan','López García'),
(2,'Isabel','Martín Torres'),
(3,'Pedro','Hernández Rojas'),
(4,'Raquel','Santos Pérez'),
(5,'Alberto','Gómez Ortiz'),
(6,'Carmen','Fuentes Beltrán'),
(7,'Roberto','Pascual Torres');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1,'Matemáticas',1),
(2,'Lengua Española',2),
(3,'Historia',3),
(4,'Geografía',4),
(5,'Física',5),
(6,'Química',6),
(7,'Biología',7),
(8,'Inglés',2),
(9,'Tecnología',5),
(10,'Educación Física',3),
(11,'Música',4),
(12,'Arte',1);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1,1,1),
(2,1,2),
(3,1,3),
(4,2,1),
(5,2,4),
(6,2,5),
(7,3,6),
(8,3,7),
(9,3,8),
(10,4,9),
(11,4,10),
(12,5,11),
(13,5,12),
(14,6,13),
(15,6,14),
(16,7,15),
(17,7,3),
(18,8,4),
(19,8,5),
(20,9,6),
(21,10,7),
(22,11,8),
(23,12,9),
(24,12,10),
(25,9,11),
(26,5,12),
(27,4,13),
(28,3,14),
(29,2,15),
(30,1,4);
```
## 005-mas composiciones.sql
### hado un selct left join
```
SELECT 
*
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;
```
| Identificador | id_asignatura | id_alumno | Identificador | nombre             | id_profesor | Identificador | nombre  | apellidos         |
|---------------|---------------|-----------|---------------|--------------------|-------------|---------------|---------|-------------------|
|             1 |             1 |         1 |             1 | Matemáticas        |           1 |             1 | Ana     | García López      |
|             2 |             1 |         2 |             1 | Matemáticas        |           1 |             2 | Luis    | Martínez Pérez    |
|             3 |             1 |         3 |             1 | Matemáticas        |           1 |             3 | María   | Sánchez Ruiz      |
|             4 |             2 |         1 |             2 | Lengua Española    |           2 |             1 | Ana     | García López      |
|             5 |             2 |         4 |             2 | Lengua Española    |           2 |             4 | Javier  | Fernández Gómez   |
|             6 |             2 |         5 |             2 | Lengua Española    |           2 |             5 | Laura   | Díaz Ortega       |
|             7 |             3 |         6 |             3 | Historia           |           3 |             6 | Carlos  | Romero Torres     |
|             8 |             3 |         7 |             3 | Historia           |           3 |             7 | Elena   | Navarro Martínez  |
|             9 |             3 |         8 |             3 | Historia           |           3 |             8 | Pablo   | Hernández Soto    |
|            10 |             4 |         9 |             4 | Geografía          |           4 |             9 | Sofía   | Iglesias Navarro  |
|            11 |             4 |        10 |             4 | Geografía          |           4 |            10 | Miguel  | Castro León       |
|            12 |             5 |        11 |             5 | Física             |           5 |            11 | Clara   | Vidal Serrano     |
|            13 |             5 |        12 |             5 | Física             |           5 |            12 | Diego   | Morales Rivas     |
|            14 |             6 |        13 |             6 | Química            |           6 |            13 | Lucía   | Cano Torres       |
|            15 |             6 |        14 |             6 | Química            |           6 |            14 | Adrián  | Herrero Gil       |
|            16 |             7 |        15 |             7 | Biología           |           7 |            15 | Nuria   | Requena Soler     |
|            17 |             7 |         3 |             7 | Biología           |           7 |             3 | María   | Sánchez Ruiz      |
|            18 |             8 |         4 |             8 | Inglés             |           2 |             4 | Javier  | Fernández Gómez   |
|            19 |             8 |         5 |             8 | Inglés             |           2 |             5 | Laura   | Díaz Ortega       |
|            20 |             9 |         6 |             9 | Tecnología         |           5 |             6 | Carlos  | Romero Torres     |
|            21 |            10 |         7 |            10 | Educación Física   |           3 |             7 | Elena   | Navarro Martínez  |
|            22 |            11 |         8 |            11 | Música             |           4 |             8 | Pablo   | Hernández Soto    |
|            23 |            12 |         9 |            12 | Arte               |           1 |             9 | Sofía   | Iglesias Navarro  |
|            24 |            12 |        10 |            12 | Arte               |           1 |            10 | Miguel  | Castro León       |
|            25 |             9 |        11 |             9 | Tecnología         |           5 |            11 | Clara   | Vidal Serrano     |
|            26 |             5 |        12 |             5 | Física             |           5 |            12 | Diego   | Morales Rivas     |
|            27 |             4 |        13 |             4 | Geografía          |           4 |            13 | Lucía   | Cano Torres       |
|            28 |             3 |        14 |             3 | Historia           |           3 |            14 | Adrián  | Herrero Gil       |
|            29 |             2 |        15 |             2 | Lengua Española    |           2 |            15 | Nuria   | Requena Soler     |
|            30 |             1 |         4 |             1 | Matemáticas        |           1 |             4 | Javier  | Fernández Gómez   |

## 008-creamos vista.sql
### creo una vista `matriculas_join`
```
CREATE VIEW matriculas_join AS 
SELECT 
asignaturas.nombre AS 'Nombre de la asignatura',
alumnos.nombre AS 'Nombre del alumno',
alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;
```
### hago una SELECT de la VIEW `matriculas_join`
```
SELECT * from  matriculas_join;
```
| Nombre de la asignatura | Nombre del alumno | Apellidos del alumno |
|-------------------------|-------------------|----------------------|
| Matemáticas             | Ana               | García López         |
| Matemáticas             | Luis              | Martínez Pérez       |
| Matemáticas             | María             | Sánchez Ruiz         |
| Lengua Española         | Ana               | García López         |
| Lengua Española         | Javier            | Fernández Gómez      |
| Lengua Española         | Laura             | Díaz Ortega          |
| Historia                | Carlos            | Romero Torres        |
| Historia                | Elena             | Navarro Martínez     |
| Historia                | Pablo             | Hernández Soto       |
| Geografía               | Sofía             | Iglesias Navarro     |
| Geografía               | Miguel            | Castro León          |
| Física                  | Clara             | Vidal Serrano        |
| Física                  | Diego             | Morales Rivas        |
| Química                 | Lucía             | Cano Torres          |
| Química                 | Adrián            | Herrero Gil          |
| Biología                | Nuria             | Requena Soler        |
| Biología                | María             | Sánchez Ruiz         |
| Inglés                  | Javier            | Fernández Gómez      |
| Inglés                  | Laura             | Díaz Ortega          |
| Tecnología              | Carlos            | Romero Torres        |
| Educación Física        | Elena             | Navarro Martínez     |
| Música                  | Pablo             | Hernández Soto       |
| Arte                    | Sofía             | Iglesias Navarro     |
| Arte                    | Miguel            | Castro León          |
| Tecnología              | Clara             | Vidal Serrano        |
| Física                  | Diego             | Morales Rivas        |
| Geografía               | Lucía             | Cano Torres          |
| Historia                | Adrián            | Herrero Gil          |
| Lengua Española         | Nuria             | Requena Soler        |
| Matemáticas             | Javier            | Fernández Gómez      |
## 010-creamos un usuario.sql 
### creo una usario para conectar PY y Mysql
```
CREATE USER 
'composiciones'@'localhost' 
IDENTIFIED  BY 'composiciones';

GRANT USAGE ON *.* TO 'composiciones'@'localhost';


ALTER USER 'composiciones'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON composiciones.* 
TO 'composiciones'@'localhost';

FLUSH PRIVILEGES
```
## 014 uso de plantilla.py
### hago import de `flack` y `mysql.connector`
```
import mysql.connector 
from flask import Flask,render_template
```
### hago una conexion de la Mysql 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones",
  password="composiciones",
  database="composiciones"
)   
```
### creao una conexion de la flack 
```
app = Flask(__name__)
@app.route("/")
```
### creo un endpoint 
```
@app.route("/")
def inicio():
```
### creo una SELECT de vista
```
  cursor = conexion.cursor(dictionary=True) 
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html",datos=filsa)
```
### empezo de flack 
```
if __name__ == "__main__":
  app.run(debug=True)
```
## index.html
### creo una structura bacica de la HTML
```
<!doctype html>
<html lang="es">
  <head>
    <title>Backoffice</title>
    <meta charset="utf-8">
    <style>

    </style>
  </head>
  <body>
    <header><h1>Gestión de escuela</h1></header>
    <main>  
    </main>
  </body>
</html>
```
### dentro de main muestra informacion de la bases de datos
```
    <section>
        {% for linea in datos:%}
        	<article>
            <div class="imagen">
            	<img src="static/josevicente.jpg">
            </div>
            <div class="texto">
              <p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
              <p>Nombre: {{linea['Nombre del alumno']}}</p>
              <p>Apellidos: {{linea['Apellidos del alumno']}}</p>
            </div>
          </article>
        {% endfor %}
      </section>    
```
#### uso for para demuetra informacion `for`
```
{% for linea in datos:%}
{% endfor %}
```
#### mustra imagen
```
<article>
<div class="imagen">
    <img src="static/josevicente.jpg">
</div>
```
#### creo demuetra de informacion
```
            <div class="texto">
              <p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
              <p>Nombre: {{linea['Nombre del alumno']}}</p>
              <p>Apellidos: {{linea['Apellidos del alumno']}}</p>
            </div>
```
# Codigo Completo
Project\
├─ templates
|   └─ index.html
├─ explicacion.md 
├─ 001-creamos una base de datos.sql  
├─ 002-datos de muestra.sql    
├─ 005-mas composiciones.sql 
├─ 008-creamos vista.sql  
├─ 010-creamos un usuario.sql  
└─ 014 uso de plantilla.py  
## 001-creamos una base de datos.sql 
```
sudo mysql -u root -p

CREATE DATABASE composiciones;

USE composiciones;

CREATE TABLE alumnos(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE profesores(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE asignaturas(
	Identificador INT PRIMARY KEY,
  nombre VARCHAR(100),
  id_profesor INT
);

CREATE TABLE matriculas(
	Identificador INT PRIMARY KEY,
  id_asignatura INT,
  id_alumno INT
);


```
## 002-datos de muestra.sql
```
INSERT INTO alumnos (Identificador, nombre, apellidos) VALUES
(1,'Ana','García López'),
(2,'Luis','Martínez Pérez'),
(3,'María','Sánchez Ruiz'),
(4,'Javier','Fernández Gómez'),
(5,'Laura','Díaz Ortega'),
(6,'Carlos','Romero Torres'),
(7,'Elena','Navarro Martínez'),
(8,'Pablo','Hernández Soto'),
(9,'Sofía','Iglesias Navarro'),
(10,'Miguel','Castro León'),
(11,'Clara','Vidal Serrano'),
(12,'Diego','Morales Rivas'),
(13,'Lucía','Cano Torres'),
(14,'Adrián','Herrero Gil'),
(15,'Nuria','Requena Soler');

INSERT INTO profesores (Identificador, nombre, apellidos) VALUES
(1,'Juan','López García'),
(2,'Isabel','Martín Torres'),
(3,'Pedro','Hernández Rojas'),
(4,'Raquel','Santos Pérez'),
(5,'Alberto','Gómez Ortiz'),
(6,'Carmen','Fuentes Beltrán'),
(7,'Roberto','Pascual Torres');

INSERT INTO asignaturas (Identificador, nombre, id_profesor) VALUES
(1,'Matemáticas',1),
(2,'Lengua Española',2),
(3,'Historia',3),
(4,'Geografía',4),
(5,'Física',5),
(6,'Química',6),
(7,'Biología',7),
(8,'Inglés',2),
(9,'Tecnología',5),
(10,'Educación Física',3),
(11,'Música',4),
(12,'Arte',1);

INSERT INTO matriculas (Identificador, id_asignatura, id_alumno) VALUES
(1,1,1),
(2,1,2),
(3,1,3),
(4,2,1),
(5,2,4),
(6,2,5),
(7,3,6),
(8,3,7),
(9,3,8),
(10,4,9),
(11,4,10),
(12,5,11),
(13,5,12),
(14,6,13),
(15,6,14),
(16,7,15),
(17,7,3),
(18,8,4),
(19,8,5),
(20,9,6),
(21,10,7),
(22,11,8),
(23,12,9),
(24,12,10),
(25,9,11),
(26,5,12),
(27,4,13),
(28,3,14),
(29,2,15),
(30,1,4);
```

## 005-mas composiciones.sql
```
SELECT 
*
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;
```
## 008-creamos vista.sql
```
CREATE VIEW matriculas_join AS 
SELECT 
asignaturas.nombre AS 'Nombre de la asignatura',
alumnos.nombre AS 'Nombre del alumno',
alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;

SELECT * from  matriculas_join;

```
## 010-creamos un usuario.sql 
```
CREATE USER 
'composiciones'@'localhost' 
IDENTIFIED  BY 'composiciones';

GRANT USAGE ON *.* TO 'composiciones'@'localhost';


ALTER USER 'composiciones'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON composiciones.* 
TO 'composiciones'@'localhost';

FLUSH PRIVILEGES;
```
## 014 uso de plantilla.py 
```
import mysql.connector 
from flask import Flask,render_template

conexion = mysql.connector.connect(
  host="localhost",
  user="composiciones",
  password="composiciones",
  database="composiciones"
)                                      

app = Flask(__name__)
@app.route("/")
def inicio():
  cursor = conexion.cursor(dictionary=True) 
  cursor.execute("SELECT * FROM matriculas_join;")  
  filas = cursor.fetchall()
  return render_template("index.html",datos=filas)

if __name__ == "__main__":
  app.run(debug=True)
```
## index.html
```
<!doctype html>
<html lang="es">
  <head>
    <title>Backoffice</title>
    <meta charset="utf-8">
    <style>

    </style>
  </head>
  <body>
    <header><h1>Gestión de escuela</h1></header>
    <main>
      <section>
        {% for linea in datos:%}
        	<article>
            <div class="imagen">
            	<img src="static/josevicente.jpg">
            </div>
            <div class="texto">
              <p>Asignatura: {{linea['Nombre de la asignatura']}}</p>
              <p>Nombre: {{linea['Nombre del alumno']}}</p>
              <p>Apellidos: {{linea['Apellidos del alumno']}}</p>
            </div>
          </article>
        {% endfor %}
      </section>    
    </main>
  </body>
</html>
```

# 4.-Cierre/Conclusión enlazando con la unidad


Este proyecto integra de forma práctica los pilares de la unidad: diseño de bases de datos, lógica de servidor y visualización web.

Al conectar SQL con Flask, hemos transformado datos estáticos en información dinámica y accesible. El uso de vistas para alimentar la interfaz demuestra cómo la correcta estructuración de los datos facilita el desarrollo de aplicaciones reales y escalables.

