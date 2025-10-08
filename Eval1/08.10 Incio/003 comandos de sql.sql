--- CRETE

INSERT INTO clientes VALUES(
    '123456789',
    'Bohdan',
    'Sydorenko',
    'info@gmail.com'
);
Query OK, 1 row affected (0,01 sec)

--- Read 

SElECT * FROM clientes;

+-----------+--------+------------+----------------+
| dni       | nombre | apeillidos | email          |
+-----------+--------+------------+----------------+
| 123456789 | Bohdan | Sydorenko  | info@gmail.com |
+-----------+--------+------------+----------------+



--- Update

UPDATE clientes
SET dni = '11111111A'
WHERE nombre = 'Bohdan';

SELECT * FROM clientes;

UPDATE clientes
SET apellidos = 'Garcia Lopez'
WHERE nombre = 'Bohdan';

+-----------+--------+------------+----------------+
| dni       | nombre | apeillidos | email          |
+-----------+--------+------------+----------------+
| 11111111A | Bohdan | Sydorenko  | info@gmail.com |
+-----------+--------+------------+----------------+


--- DELETE 

DELETE FROM clientes 
WHERE dni = '11111111A';
Query OK, 1 row affected (0,00 sec)

