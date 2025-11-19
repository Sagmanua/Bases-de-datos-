import mysql.connector
import matplotlib.pyplot as plt  # Debe ser pyplot, no solo matplotlib

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
        COUNT(color) AS numero,
        color
    FROM productos
    GROUP BY color
    ORDER BY COUNT(color) DESC;
    '''
)
filas = cursor.fetchall()

cantidades = []
etiquetas = []

for fila in filas:
    cantidades.append(fila[0])
    etiquetas.append(fila[1])

print(cantidades)
print(etiquetas)

plt.pie(cantidades, labels=etiquetas)
plt.show()
