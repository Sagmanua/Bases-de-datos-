import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="cliente26_11",
  password="StrongPass2024!",
  database="clientes1"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM matriculas_join;")  

filas = cursor.fetchall()

print(filas)