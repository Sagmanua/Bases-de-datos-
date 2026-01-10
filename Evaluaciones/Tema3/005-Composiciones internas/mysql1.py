import mysql.connector 

# Configuración de la conexión
config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

# Crear la conexión
conexion = mysql.connector.connect(**config)