-- Seleccionamos los datos que nos interesan
-- Cruzamos matriculas con alumnos y asignaturas

SELECT 
asignaturas.nombre AS 'Nombre de la asignatura',
alumnos.nombre AS 'Nombre del alumno',
alumnos.apellidos AS 'Apellidos del alumno'
FROM matriculas
LEFT JOIN asignaturas
ON matriculas.id_asignatura = asignaturas.Identificador
LEFT JOIN alumnos
ON matriculas.id_alumno = alumnos.Identificador;







+-------------------------+-------------------+----------------------+
| Nombre de la asignatura | Nombre del alumno | Apellidos del alumno |
+-------------------------+-------------------+----------------------+
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
+-------------------------+-------------------+----------------------+
30 rows in set (0,00 sec)
