import mysql.connector 
from flask import Flask, render_template
import json

# Configuración de la conexión
config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

# Crear la conexión
conexion = mysql.connector.connect(**config)

app = Flask(__name__)

@app.route("/clientes")
def clientes():
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM clientes;")  
    filas = cursor.fetchall()
    return json.dumps(filas)

@app.route("/tablas")
def tablas():
    cursor = conexion.cursor() 
    cursor.execute("SHOW TABLES;")  
    filas = cursor.fetchall()
    tablas = []
    for fila in filas:
        tablas.append(fila[0])
    return json.dumps(tablas)

if __name__ == "__main__":
    app.run(debug=True)