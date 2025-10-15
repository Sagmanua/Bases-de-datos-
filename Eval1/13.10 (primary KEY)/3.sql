ALTER TABLE clientes
ADD COLUMN iditificador INT AUTO_INCERMENT
PRIMARY KEY FIRST;

ALTER TABLE clientes
ADD COLUMN iditificador INT AUTO_INCREMENT PRIMARY KEY FIRST;

ALTER

INSERT INTO clientes
VALUES(
	NULL,
	'123456789',
	'Bohdan',
	'Sydorenko',
	'info@gmail.com'
	);
SELECT FROM * clientes;

INSERT INTO clientes
VALUES(
	NULL,
	'123456789',
	'Bohdan',
	'Sydorenko',
	'info@gmail.com'
	);
+--------------+-----------+--------+-----------+----------------+
| iditificador | id        | nombre | apellidos | email          |
+--------------+-----------+--------+-----------+----------------+
|            1 | 123456789 | Bohdan | Sydorenko | info@gmail.com |
|            2 | 123456789 | Bohdan | Sydorenko | info@gmail.com |
+--------------+-----------+--------+-----------+----------------+

	
ejemplo 2020600

INSERT INTO clientes
VALUES(
	4,
	'12345678Z',
	'Bohdan1',
	'Sydorenko1',
	'info@gamil.com'
	);
+--------------+-----------+--------+-----------+----------------+
| iditificador | id        | nombre | apellidos | email          |
+--------------+-----------+--------+-----------+----------------+
|            1 | 123456789 | Bohdan | Sydorenko | info@gmail.com |
|            2 | 123456789 | Bohdan | Sydorenko | info@gmail.com |
|            3 | 123456789 | Bohdan | Sydorenko | correincorecto |
+--------------+-----------+--------+-----------+----------------+
