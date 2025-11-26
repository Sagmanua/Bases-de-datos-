sudo mysql -u root -p



sudo mysql -u root -p

CREATE DATABASE clientes1;


USE clientes1;

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
    nombre VARCHAR(100),
    id_alumno INT
);