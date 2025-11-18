sudo mysql -u root -p

SHOW TABLE;
CREATE DATABASE practica;



CREATE TABLE productos ( 
	id INT, 
	nombre VARCHAR(255) NOT NULL, 
	descripcion TEXT, 
	precio DECIMAL(7,2) NOT NULL, 
	stock INT NOT NULL );
	
ALTER TABLE productos MODIFY id INT NOT NULL, ADD PRIMARY KEY (id);

ALTER TABLE productos MODIFY id INT NOT NULL AUTO_INCREMENT;

ALTER TABLE productos ADD CONSTRAINT chk_stock_no_negativo CHECK (stock >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_no_negativo CHECK (precio >= 0);

ALTER TABLE productos ADD CONSTRAINT chk_precio_max_5000 CHECK (precio <= 5000);

ALTER TABLE productos ADD CONSTRAINT chk_nombre_min_5 CHECK (CHAR_LENGTH(nombre) >= 5);
