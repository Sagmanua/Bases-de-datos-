# Introducción de la práctica

En esta práctica de bases de datos vamos a trabajar el concepto de copia de seguridad y las operaciones CRUD (Create, Read, Update, Delete) en MySQL.
Realizar copias de seguridad es importante para proteger la información ante fallos o errores, y las operaciones CRUD nos permiten gestionar los datos almacenados en la base de datos.

# Aplicación Práctica

Si MySQL está instalado, iniciamos sesión con:

sudo mysql -u root -p

Seleccionar la Base de Datos

Usamos la base de datos donde queremos trabajar, en este caso empresarial:

USE empresarial;

1. Copia de Seguridad

Primero creamos un directorio para guardar nuestra copia de seguridad:

mkdir micopiadeseguridad
cd micopiadeseguridad


Luego ejecutamos el siguiente comando para generar la copia:

mysqldump -u usuarioempresarial -p empresarial > copia_de_seguridad_empresarial.sql


⚠ Se pedirá la contraseña. Escríbela y presiona Enter.

2. Operaciones CRUD en la tabla clientes
Comprobar la tabla antes de modificarla
DESCRIBE clientes;

Campo	Tipo	Null	Clave	Extra
id	int	NO	PRI	auto_increment
nombre	varchar(50)	YES		
apellidos	varchar(255)	YES		
telefono	varchar(20)	YES		
email	varchar(50)	YES		
localidad	varchar(100)	YES		
A. Crear (INSERT)
INSERT INTO clientes VALUES 
(NULL, 'Nombre del nuevo cliente', 'Apellidos del nuevo cliente', '620891718', 'info@jocarsa.com', 'Localidad del nuevo cliente');

B. Leer (SELECT)

Para comprobar que se insertó correctamente:

SELECT * FROM clientes;

C. Actualizar (UPDATE)
UPDATE clientes 
SET nombre = "Jose Vicente"
WHERE telefono = 620891718;


⚠ Siempre usar WHERE, de lo contrario se modificarán todos los registros.

D. Eliminar (DELETE)
DELETE FROM clientes
WHERE telefono = '620891718';


⚠ Este comando puede borrar muchos datos si no se usa correctamente.

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