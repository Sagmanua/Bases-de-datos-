# 1.-Indroduccion brece y contexalizacion
En este practica vamos crear una CRUD (Crear, Leer, Actualizar, Eliminar y Salir) en python con conectado un bases de datos tambien vamos a estudiar y leer 



# 2.-Desarrollo técnico correcto y preciso

### EL primero voy a crear bases de datos llamada `empresa.db` con SGLite con este codigo 
```
CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);
```
| Field       | Type         | Null | Key | Default | Extra          |
|:-------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Identificador          | INTEGER          | NO   | PRI | NULL    | auto_increment |
| nombre      | TEXT | NO   |     | NULL    |                |
| apellidos | text         | NO  |     | NULL    |                |
| email | text         | No  |     | NULL    |                |

### despues de crear empresa.db esto voy a crear una CRUD en Python with sqlite3
### importo sqlite3 para puede trabajar un bases de datos en python
```
import sqlite3
```
### Ahora voy conecion a bases de datos `empresa.db` 
```
conexion = sqlite3.connect("empresa.db")    
```
### Creo bucle infinito com preguntas y opcin que elegir usario que programa no te detengas despues de una accion 
```
while True:
print("Hola tienes 4 opciones")
print("1.Opcion 1 es leer bases de datos ")
print("2.Opcion 2 es crear una row ")
print("3.Opcion 3 es editar una row  ")
print("4.Opcion 4 es borar una row ")
      opcion = int(input("Elige"))
```
### Creo unas opcion para que usario puede eligir que su quire 
```
if opcion == 1:
    print("Ahora vamos a leer todos los datos de bases de datos ")
if opcion ==2:
    print("Ahora vamos a crear una nuevo linia en bases de datos")
if opcion == 3:
    print("Ahora vamos a redactar una linia en bases de datos ")
if opcion == 4:
    print("Ahora vamos vorar una linia en bases de datos")

```
### Despues de crear 4 opciones hacemos funciones es este opciones depende de sus funciones 
```
if opcion == 1:
            cursor = conexion.cursor()
            cursor.execute('''
                  SELECT * FROM clientes;
            ''')
            filas = cursor.fetchall()
            for fila in filas:    
                  print(fila)
            conexion.commit()
if opcion == 2:
            cursor = conexion.cursor()
            nombre = input("Nombre")
            apellidos = input("Ape")
            email = input("email")
            cursor.execute("INSERT INTO clientes VALUES (NULL,'"""+apellidos+"""', '"""+nombre+"""','"""+email+"""');""")
if opcion == 3:
            print("Ahora vamos a redactar una linia en bases de datos ")
            Identificador = input("id")
            nombre = input("Nombre")
            ape = input("Ape")
            email = input("email")
            cursor = conexion.cursor()
            cursor.execute("UPDATE clientes SET nombre = '"""+nombre+"""', apellidos = '"""+ape+"""', email = '"""+email+"""' WHERE Identificador = '"""+Identificador+"""';"""                  
            )
if opcion == 4:
            print("Ahora vamos vorar una linia en bases de datos")
            Identificador = input("id")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Clientes WHERE Identificador ='"""+Identificador+"""'; """)
```

# Codigo completa 
### empezamos com Sqlite
```
CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);

```
### Python
```
'''
    006-Índices. Característica
    (c) Bohdan sydorenko
    Crear una CRUD
'''


# Importamos libreria
import sqlite3
# Nos conectamos a la base de datos
conexion = sqlite3.connect("empresa.db")

#CRUD


while True:
      print("Hola tienes 4 opciones")
      print("1.Opcion 1 es leer bases de datos ")
      print("2.Opcion 2 es crear una row ")
      print("3.Opcion 3 es editar una row  ")
      print("4.Opcion 4 es borar una row ")

      opcion = int(input("Elige"))
      #-----------opcion 1 LEER---------------
      if opcion == 1:
            print("Ahora vamos a Leer todos los datos de bases de datos")
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
            print("Ahora vamos a crear una nuevo linia en bases de datos")
            cursor = conexion.cursor()
            nombre = input("Nombre")
            apellidos = input("Ape")
            email = input("email")

            cursor.execute("INSERT INTO clientes VALUES (NULL,'"""+apellidos+"""', '"""+nombre+"""','"""+email+"""');""")
      #-----------opcion 3 EDITAR ---------------

      if opcion == 3:
            print("Ahora vamos a redactar una linia en bases de datos ")
            Identificador = input("id")
            nombre = input("Nombre")
            ape = input("Ape")
            email = input("email")
            cursor = conexion.cursor()
            cursor.execute("UPDATE clientes SET nombre = '"""+nombre+"""', apellidos = '"""+ape+"""', email = '"""+email+"""' WHERE Identificador = '"""+Identificador+"""';"""                  

            )
      #-----------opcion 4 BORRAR ---------------

      if opcion == 4:
            print("Ahora vamos vorar una linia en bases de datos")
            Identificador = input("id")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Clientes WHERE Identificador ='"""+Identificador+"""'; """)
```

# 4.-Cierre/Conclusión enlazando con la unidad







