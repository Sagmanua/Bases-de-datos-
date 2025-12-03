# 1.-Indroduccion brece y contexalizacion

En la administración de bases de datos es importante proteger la información, por eso se realizan copias de seguridad (backups). Estas permiten recuperar los datos en caso de errores, fallos o eliminaciones accidentales.

En esta práctica nos conectaremos a MySQL para realizar operaciones de eliminación de datos, pero antes recordaremos que siempre es necesario contar con una copia de seguridad actualizada. Así reforzamos la importancia de trabajar con cuidado y responsabilidad al manejar bases de datos.



# 2.-Desarrollo técnico correcto y preciso
## Copia de seguridad 
### Al primero importar `subprocess` para gurdar bases de datos y `datatime` 
```
import subprocess
from datetime import datetime
```

### Voy a saber que tiempo hoy 
```
ahora = datetime.now()
```
### Convierte la fecha y hora en texto y agrega ceros a la izquierda para mantener formato, por ejemplo: 07, 03, etc.
```
anio = str(ahora.year).zfill(4)
mes = str(ahora.month).zfill(2)
dia = str(ahora.day).zfill(2)
hora = str(ahora.hour).zfill(2)
minuto = str(ahora.minute).zfill(2)
segundo = str(ahora.second).zfill(2)
```

### Define los datos de acceso a la base de datos MySQL.
```
usuario = "usuarioempresarial"
password = "usuarioempresarial"
base_datos = "empresarial"
```
### Crea el nombre del archivo de respaldo usando la fecha y hora, ejemplo:
```
archivo_salida = str(anio)+str(mes)+str(dia)+str(hora)+str(minuto)+str(segundo)+"_copia_de_seguridad.sql"
```
### Prepara el comando que hará la copia de seguridad usando mysqldump.
```
comando = [
    "mysqldump",
    f"-u{usuario}",
    f"-p{password}",
    base_datos
]
```
### Ejecuta el comando y guarda el resultado (la copia) en el archivo.
```
with open(archivo_salida, "w") as salida:
    subprocess.run(comando, stdout=salida, check=True)
```

### Muestra un mensaje indicando dónde se guardó la copia.
```
print("Copia de seguridad creada en ",archivo_salida)

```

## Python CRUD 
### Al primero importar `mysql.connector` para puede conectar con Mysql y conecta en bases de datos de mi ordenador y escribir si todo bien or no 

``` 
import mysql.connector
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()
    print("✅ Conexión exitosa!")
    print("Hola tu redacta database portafolio")
    cursor.close() 
    conexion.close()
except Exception as e:
    print("❌ Error:", e)
```
### Hacer bucle infinito para crud 
```
    while True:
        pass
```
### Empezar crear CRUD en bucle indinito
```
print("Escoge una opcion:")
print("1.-Insertar un cliente")
print("2.-Listar los clientes")
print("3.-Actualizar un cliente")
print("4.-Borrar un cliente")
opcion = int(input("Escoge una opcion:"))
    if opcion == 1:
        break
    elif opcion == 2:
        break
    elif opcion == 3:
        break
    elif opcion == 4:
        break
    else:
        break
```
### Ahora boy a crear Insetas.
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a crear insetar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos
##### Tabla de Categoria
```
if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute(
        '''INSERT INTO Categoria
VALUES ('''+ Id_cat + ''',\'''' + titulo_c + '''\',\'''' + descripcion_c + '''\'
);'''
    )
```
##### Tabla de Pieza
```
elif opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    INSERT INTO Pieza
                    VALUES (
                    '''+id_pieza+''',
                    "''' + titulo_p + '''",
                    "''' + descripcion_p + '''",
                    "''' + imagen + '''",
                    "''' + url + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
```
### Ahora boy a crear Leidos
#### En Mysql creado view `CatPIEz` por eso solo ajecuta este view
```
elif opcion == 2:
            print("Listamos los clientes")
            cursor.execute("SELECT * FROM CatPIEz")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Actuliza. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de Categoria
```
if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute('''
                    UPDATE Categoria
                    SET titulo_c = "'''+titulo_c+'''",
                        descripcion_c = "'''+descripcion_c+'''"
                    WHERE Id_cat = '''+Id_cat+'''
                ''')
                conexion
```
##### Tabla de Pieza
```
if opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                tiurltulo_p = input("tiurltulo_p: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    UPDATE Pieza
                    SET titulo_p = "'''+titulo_p+'''",
                        descripcion_p = "'''+descripcion_p+'''",
                        imagen = "'''+imagen+'''",
                        url = "'''+url+'''",
                        id_categoria = '''+id_categoria+'''
                    WHERE id_pieza = '''+id_pieza+'''
                ''')
```
### Ahora boy a crear Actulaziones
#### Empezar you tiene 2 tablas  `Pieza` y `Categoria` por eso voy a hacer yna Esoge para usario
```
 print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                break
            elif opciondeinsetar == 2:
                break
            else:
                print("Numero incorecta")
```
#### dentro de esto voy a Borar. Da a usario input para escribe su valores despues escribe codigo para gurdar datos en Bases de datos


##### Tabla de Categoria
```
if opciondeinsetar == 1:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Categoria
                WHERE Identificador = '''+id+'''
                ''')
```
##### Tabla de Pieza
```
if opciondeinsetar == 2:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Pieza
                WHERE Identificador = '''+id+'''
                ''')
```
# Codigo Completo
## Copia de seguridad en Py
```
#imports
import subprocess
from datetime import datetime

# data time ahora
ahora = datetime.now()

#Convierte la fecha y hora en str
anio = ahora.year.zfill(2)
mes = ahora.month.zfill(2)
dia = ahora.day.zfill(2)
hora = ahora.hour.zfill(2)
minuto = ahora.minute.zfill(2)
segundo = ahora.second.zfill(2)

#crer usario y contrasena 
usuario = "usuarioempresarial"
password = "usuarioempresarial"
base_datos = "empresarial"

#gurda tiempo cuando gurdo este archivo
archivo_salida = str(anio)+str(mes)+str(dia)+str(hora)+str(minuto)+str(segundo)+"_copia_de_seguridad.sql"

# usa libriaa mysql para gurdar bases de datos
comando = [
    "mysqldump",
    f"-u{usuario}",
    f"-p{password}",
    base_datos
]
#Probar si todo bien
with open(archivo_salida, "w") as salida:
    subprocess.run(comando, stdout=salida, check=True)
#imprim si todo bien
print(Copia de seguridad creada en ",archivo_salida)
```
## Crud en Py 
import mysql.connector
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()

    
    print("✅ Conexión exitosa!")
    print("Hola tu redacta database portafolio")
    while True:
        print("Escoge una opcion:")
        print("1.-Insertar un cliente")
        print("2.-Listar los clientes")
        print("3.-Actualizar un cliente")
        print("4.-Borrar un cliente")
        opcion = int(input("Escoge una opcion:"))

        if opcion == 1:
            print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute(
        '''INSERT INTO Categoria
VALUES ('''+ Id_cat + ''',\'''' + titulo_c + '''\',\'''' + descripcion_c + '''\'
);'''
    )
                conexion.commit()
            elif opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")

                cursor.execute('''
                    INSERT INTO Pieza
                    VALUES (
                    '''+id_pieza+''',
                    "''' + titulo_p + '''",
                    "''' + descripcion_p + '''",
                    "''' + imagen + '''",
                    "''' + url + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
            else:
                print("Numero incorecta")
        elif opcion == 2:
            print("Listamos los clientes")
            cursor.execute("SELECT * FROM CatPIEz")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
        elif opcion == 3:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de Categoria")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute('''
                    UPDATE Categoria
                    SET titulo_c = "'''+titulo_c+'''",
                        descripcion_c = "'''+descripcion_c+'''"
                    WHERE Id_cat = '''+Id_cat+'''
                ''')
                conexion.commit()
            if opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                tiurltulo_p = input("tiurltulo_p: ")
                url = input("url VARCHAR")
                id_categoria = input("id_categoria INT: ")
                cursor.execute('''
                    UPDATE Pieza
                    SET titulo_p = "'''+titulo_p+'''",
                        descripcion_p = "'''+descripcion_p+'''",
                        imagen = "'''+imagen+'''",
                        url = "'''+url+'''",
                        id_categoria = '''+id_categoria+'''
                    WHERE id_pieza = '''+id_pieza+'''
                ''')
        elif opcion == 4:
            print("Escoge una opcion:")
            print("1.Actulizar en tabla de Categoria")
            print("2.Actulizar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Categoria
                WHERE Identificador = '''+id+'''
                ''')
                
                conexion.commit()
            if opciondeinsetar == 2:
                print("Eliminamos un ")
                id = input("Introduce el id del cliente que quieres eliminar: ")
                cursor.execute('''
                DELETE FROM Pieza
                WHERE Identificador = '''+id+'''
                ''')
        else:
            break
    cursor.close() 
    conexion.close()




except Exception as e:
    print("❌ Error:", e)





# 4.-Cierre/Conclusión enlazando con la unidad
Con esta actividad hemos reforzado la importancia de realizar copias de seguridad antes de modificar o eliminar información dentro de una base de datos. Al conectarnos a MySQL y ejecutar operaciones de eliminación, comprendimos que cualquier cambio puede ser permanente si no se cuenta con un respaldo adecuado. Este ejercicio se relaciona directamente con la unidad, ya que resalta la necesidad de proteger y mantener la integridad de los datos como parte esencial de la administración de bases de datos.