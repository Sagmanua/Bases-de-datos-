-- crea usuario nuevo con contraseña
CREATE USER 'tiendaclase'@'localhost' IDENTIFIED BY 'Tiendaclase123$';

-- permite acceso a ese usuario
GRANT ALL PRIVILEGES ON tiendaclase.* TO 'tiendaclase'@'localhost';
FLUSH PRIVILEGES;