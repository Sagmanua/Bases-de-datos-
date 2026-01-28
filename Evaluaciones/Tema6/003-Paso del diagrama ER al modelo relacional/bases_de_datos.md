-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS clientes_Tema6_ej003;

-- Usarla
USE clientes_Tema6_ej003;

CREATE TABLE Cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE Telefono (
  id INT PRIMARY KEY,
  id_cliente INT,
  tipo VARCHAR(50),
  numero VARCHAR(20),
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id)
);

CREATE TABLE Persona (
  id INT PRIMARY KEY,
  nombre VARCHAR(100),
  apellidos VARCHAR(100)
);

CREATE TABLE Alumno (
  id INT PRIMARY KEY,
  NIA VARCHAR(20),
  FOREIGN KEY (id) REFERENCES Persona(id)
);

CREATE TABLE Profesor (
  id INT PRIMARY KEY,
  asignaturas TEXT,
  FOREIGN KEY (id) REFERENCES Persona(id)
);