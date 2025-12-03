DESCRIBE clientes

ALTER TABLE clientes
MODIFY COLUMN id VARCHAR(9);

ALTER TABLE clientes
ADD COLUMN direccion VARCHAR(255);

ALTER TABLE clientes
DROP COLUMN direccion;

ALTER TABLE clientes
RENAME COLUMN id TO dninie ;

ALTER TABLE clientes
DROP CONSTRAINT comprobar_dni_nie_letra;
