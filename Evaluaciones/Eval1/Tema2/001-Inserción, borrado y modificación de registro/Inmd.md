# Introducción de la práctica

En esta práctica de bases de datos vamos a trabajar el concepto de copia de seguridad y las operaciones CRUD (Create, Read, Update, Delete) en MySQL.
Realizar copias de seguridad es importante para proteger la información ante fallos o errores, y las operaciones CRUD nos permiten gestionar los datos almacenados en la base de datos.

# Aplicación Práctica

Si MySQL está instalado, iniciamos sesión con `sudo mysql -u root -p` para probar si esata esta bases de datos 

Seleccionar la Base de Datos

Usamos la base de datos donde queremos trabajar, en este caso empresarial:

USE empresarial;

# Código Completo
USE empresarial;
INSERT INTO clientes VALUES 
(NULL, 'Nombre del nuevo cliente', 'Apellidos del nuevo cliente', '620891718', 'info@jocarsa.com', 'Localidad del nuevo cliente');
SELECT * FROM clientes;
UPDATE clientes 
SET nombre = "Jose Vicente"
WHERE telefono = 620891718;
DELETE FROM clientes
WHERE telefono = '620891718';
# Conclusión enlazando con la actividad

En esta actividad aprendimos a realizar una copia de seguridad de una base de datos usando mysqldump, lo cual es fundamental para proteger la información.
También practicamos las operaciones CRUD, que son esenciales para gestionar cualquier base de datos:Crear nuevos registro,Consultar datos existentes,Actualizar información,Eliminar datos de manera controlada .Estos pasos nos permiten administrar la información de forma segura y eficiente.