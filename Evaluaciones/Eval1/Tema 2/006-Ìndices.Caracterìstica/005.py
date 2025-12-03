'''
CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
'''


# Importamos libreria
import sqlite3
# Nos conectamos a la base de datos
conexion = sqlite3.connect("006.db")

#CRUD


while True:
      print("Hola tienes 4 opciones")
      print("1.Leer")
      print("2.Crear")
      print("3.Editar")
      print("4.Borrar")

      opcion = int(input("Elige"))
      #-----------opcion 1 LEER---------------
      if opcion == 1:
            print("Lear")
            # Creamos un cursor
            cursor = conexion.cursor()

            cursor.execute('''
                  SELECT * FROM clientes;
            ''')
            filas = cursor.fetchall()

            for fila in filas:    
                  print(fila)

            # Lanzamos la peticion
            conexion.commit()
      #-----------opcion 2 CREAR ---------------
      if opcion == 2:
            print("Crear")
            cursor = conexion.cursor()
            nombre = input("Nombre")
            apellidos = input("Ape")
            email = input("email")

            cursor.execute("INSERT INTO clientes VALUES (NULL,'"""+apellidos+"""', '"""+nombre+"""','"""+email+"""');""")
      #-----------opcion 3 EDITAR ---------------

      if opcion == 3:
            print("Editar")
            Identificador = input("id")
            nombre = input("Nombre")
            ape = input("Ape")
            email = input("email")
            cursor = conexion.cursor()
            cursor.execute("UPDATE clientes SET nombre = '"""+nombre+"""', apellidos = '"""+ape+"""', email = '"""+email+"""' WHERE Identificador = '"""+Identificador+"""';"""                  

            )
      #-----------opcion 4 BORRAR ---------------

      if opcion == 4:
            Identificador = input("id")
            cursor = conexion.cursor()
            print("Borrar")
            cursor.execute("DELETE FROM Clientes WHERE Identificador ='"""+Identificador+"""'; """)                 

      if opcion == 5:
            cursor = conexion.cursor()
            cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name='clientes';")                 


            






