-- sudo mysql -u root -p

USE clientes;

SELECT 
* 
FROM clientes;

mysql> CREATE USER 'clientes'@'localhost' IDENTIFIED BY 'Clientes123$';

mysql> GRANT ALL PRIVILEGES ON clientes.* TO 'clientes'@'localhost';

mysql> FLUSH PRIVILEGES;
