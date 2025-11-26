mysql> SELECT 
    -> *
    -> FROM matriculas
    -> LEFT JOIN asignaturas
    -> ON matriculas.id_asignatura = asignaturas.Identificador;
+---------------+---------------+-----------+---------------+--------------------+-------------+
| Identificador | id_asignatura | id_alumno | Identificador | nombre             | id_profesor |
+---------------+---------------+-----------+---------------+--------------------+-------------+
|             1 |             1 |         1 |             1 | Matemáticas        |           1 |
|             2 |             1 |         2 |             1 | Matemáticas        |           1 |
|             3 |             1 |         3 |             1 | Matemáticas        |           1 |
|             4 |             2 |         1 |             2 | Lengua Española    |           2 |
|             5 |             2 |         4 |             2 | Lengua Española    |           2 |
|             6 |             2 |         5 |             2 | Lengua Española    |           2 |
|             7 |             3 |         6 |             3 | Historia           |           3 |
|             8 |             3 |         7 |             3 | Historia           |           3 |
|             9 |             3 |         8 |             3 | Historia           |           3 |
|            10 |             4 |         9 |             4 | Geografía          |           4 |
|            11 |             4 |        10 |             4 | Geografía          |           4 |
|            12 |             5 |        11 |             5 | Física             |           5 |
|            13 |             5 |        12 |             5 | Física             |           5 |
|            14 |             6 |        13 |             6 | Química            |           6 |
|            15 |             6 |        14 |             6 | Química            |           6 |
|            16 |             7 |        15 |             7 | Biología           |           7 |
|            17 |             7 |         3 |             7 | Biología           |           7 |
|            18 |             8 |         4 |             8 | Inglés             |           2 |
|            19 |             8 |         5 |             8 | Inglés             |           2 |
|            20 |             9 |         6 |             9 | Tecnología         |           5 |
|            21 |            10 |         7 |            10 | Educación Física   |           3 |
|            22 |            11 |         8 |            11 | Música             |           4 |
|            23 |            12 |         9 |            12 | Arte               |           1 |
|            24 |            12 |        10 |            12 | Arte               |           1 |
|            25 |             9 |        11 |             9 | Tecnología         |           5 |
|            26 |             5 |        12 |             5 | Física             |           5 |
|            27 |             4 |        13 |             4 | Geografía          |           4 |
|            28 |             3 |        14 |             3 | Historia           |           3 |
|            29 |             2 |        15 |             2 | Lengua Española    |           2 |
|            30 |             1 |         4 |             1 | Matemáticas        |           1 |
+---------------+---------------+-----------+---------------+--------------------+-------------+
30 rows in set (0,01 sec)
