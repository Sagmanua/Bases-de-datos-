INSERT INTO clientes VALUES(
    NULL,
    'Bohdan ',
    'Sydorenko',
    'info.gmail.com'
);
-- read
SELECT FROM * clientes;
-- update 
update clientes
SET email ='info@mail.com'
where idificador = 1;
---delete clientes
delete from clientes
where idificador = 1;