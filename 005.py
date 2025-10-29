# Importamos libreria
import sqlite3
# Nos conectamos a la base de datos
conexion = sqlite3.connect("006.db")

cursor = conexion.cursor()
#CRUD


      print("1.Leer")
      print("2.Crear")
      print("3.Editar")
      print("4.Borrar")

      opcion = input("Elige")

      if opcion == 1:
            print("Lear")
            # Creamos un cursor
            

            cursor.execute('''
                  SELECT * FROM clientes;
            ''')
            filas = cursor.fetchall()

            for fila in filas:    
                  print(fila)

            # Lanzamos la peticion
            conexion.commit()
      if opcion == 2:
            print("Crear")
      if opcion == 3:
            print("Editar")
      if opcion == 4:
            print("4.Borrar")