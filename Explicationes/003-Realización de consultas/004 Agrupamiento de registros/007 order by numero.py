import mysql.connector
import matplotlib.pyplot as plt

conexion = mysql.connector.connect(
    host="localhost",
    user="usuarioempresarial",
    password="Us3r@2025!",
    database="clientes_db"
)
print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()
cursor.execute(
    '''
    SELECT 
        COUNT(categoria) AS numero,
        categoria
    FROM productos
    GROUP BY categoria
    ORDER BY numero DESC;
    '''
)
filas = cursor.fetchall()

cantidades = [fila[0] for fila in filas]
etiquetas = [fila[1] for fila in filas]

print(cantidades)
print(etiquetas)

plt.pie(cantidades, labels=etiquetas)
plt.show()
