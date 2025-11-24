import mysql.connector
from flask import Flask, render_template 
import json



conexion = mysql.connector.connect(
    host="localhost",
    user="clientetienda",
    password="Tiendaclase123$",
    database="tienda"
)

cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  
app = Flask(__name__)

app = Flask(__name__)

app = Flask(__name__)

@app.route("/clientes")
def inicio():
    cursor = conexion.cursor() 
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    return json.dumps(filas)

if __name__ == "__main__":
  app.run(debug=True) 

