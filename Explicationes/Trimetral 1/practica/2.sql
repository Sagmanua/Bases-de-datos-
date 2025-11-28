sudo mysql -u root -p

SHOW TABLE;
CREATE DATABASE practica;



CREATE TABLE productos ( 
	id INT, 
	nombre VARCHAR(255) NOT NULL, 
	descripcion TEXT, 
	precio DECIMAL(7,2) NOT NULL, 
	stock INT NOT NULL );
	

ALTER TABLE productos MODIFY id NOT NULL,
ADD PRIMERY KEY(id);

ALTER TABLE productos MODIFY id NOT NULL,
ADD AUTO_INCEMENT;

ALTER TABLE productos 
ADD CONSTRAINT chk_stock CHECK(stock>=0)

