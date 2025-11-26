-- Seleccionamos los datos que nos interesan
-- Cruzamos matriculas con alumnos y asignaturas

SELECT 
*
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;



+---------------+---------------+-----------+---------------+--------------------+-------------+---------------+---------+-------------------+
| Identificador | id_asignatura | id_alumno | Identificador | nombre             | id_profesor | Identificador | nombre  | apellidos         |
+---------------+---------------+-----------+---------------+--------------------+-------------+---------------+---------+-------------------+
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
+---------------+---------------+-----------+---------------+--------------------+-------------+---------------+---------+-------------------+
30 rows in set (0,00 sec)
