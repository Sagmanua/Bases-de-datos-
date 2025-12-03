CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  emial VARCHAR(255)
);

CREATE TABLE pedido (
  id INT PRIMARY KEY,
  fecha VARCHAR(255),
  cliente_id INT,
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE listapedido (
  id INT PRIMARY KEY,
  pedido_id INT,
  productos_id INT,
  CONSTRAINT fk_listapedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_listapedido_2 FOREIGN KEY (productos_id) REFERENCES productos(id)
);

CREATE TABLE productos (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  precio VARCHAR(255)
);