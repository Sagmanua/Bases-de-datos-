ALTER TABLE clientes
	ADD CONSTRAINT comprobar_email
	CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$');

DELETE FROM clientes WHERE inditificador = 4
DELETE FROM clientes WHERE inditificador = (que tienene falla)

ALTER TABLE clientes
ADD CONSTRAINT comprobar_dni_nie
CHECK (
    dni REGEXP '^[0-9]{8}[A-Za-z]$'  -- DNI: 8 digits + letter
    OR
    dni REGEXP '^[XYZ][0-9]{7}[A-Za-z]$'  -- NIE: X, Y, or Z + 7 digits + letter
);

