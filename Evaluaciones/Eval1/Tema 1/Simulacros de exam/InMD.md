
# 1.-Indroduccion brece y contexalizacion





# 2.-Desarrollo técnico correcto y preciso
## Crear bases de datos en Mysql
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### ahora veo que bases de datos tiene 
```
SHOW DATABASES;
```
| Database           |
|:--------------------:|
| empresadam         |
| information_schema |
| mysql              |
| performance_schema |
| practica           |
| sys                |

### Creo bases de datos con nombre de portafolio
```
CREATE DATABASE portafolio;    
```
### Abrir bases de dattos para trabajar en ella 
```
USE portafolio;
```
### crear tabla de Categoria
#### codigo
```
CREATE TABLE Categoria(
    Id_cat INT Primary Key,
    titulo_c VARCHAR(255),
    descripcion_c VARCHAR(255)
);
```
### pronar si todo pasar bien
```
DESCRIBE Categoria;
```

| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| Id_cat        | int          | NO   | PRI | NULL    |       |
| titulo_c      | varchar(255) | YES  |     | NULL    |       |
| descripcion_c | varchar(255) | YES  |     | NULL    |       |


### Ahora crear Pieza con `FOREIGN KEY`de tabla `Categoria`
```
CREATE TABLE Pieza(
    id_pieza INT Primary Key,
    titulo_p VARCHAR(255),
    descripcion_p VARCHAR(255),
    imagen VARCHAR(255),
    url VARCHAR(255),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES Categoria(Id_cat)
);
```
### pronar si todo pasar bien
```
DESCRIBE Pieza;
```

| Field         | Type         | Null | Key | Default | Extra |
|:--------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| id_pieza      | int          | NO   | PRI | NULL    |       |
| titulo_p      | varchar(255) | YES  |     | NULL    |       |
| descripcion_p | varchar(255) | YES  |     | NULL    |       |
| imagen        | varchar(255) | YES  |     | NULL    |       |
| url           | varchar(255) | YES  |     | NULL    |       |
| id_categoria  | int          | YES  | MUL | NULL    |       |




### Para probar Lrft join voy crear alqunas insertas en tabla   
```
INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera');

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (2, 'Pintura', 'Cuadros en óleo o acrílico');
```

```
INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (1, 'El Pensador', 'Escultura de Rodin', 'pensador.jpg', 'http://ejemplo.com/pensador', 1);

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (2, 'La Noche Estrellada', 'Pintura de Van Gogh', 'noche.jpg', 'http://ejemplo.com/noche', 2);
```
### despues de inserto valores en tablas voy a hacer Left join
```
SELECT p.*, c.titulo_c, c.descripcion_c
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
```
#### Resultado 
| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | id_categoria | titulo_c  | descripcion_c                          |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:--------------:|:-----------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador |            1 | Escultura | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    |            2 | Pintura   | Cuadros en óleo o acrílico             |


### Ahora voy a crear view de 2 tablas Lrft join
```
CREATE VIEW CatPIEz AS 
SELECT
p.id_pieza,
p.titulo_p,
p.descripcion_p,
p.imagen,
p.url,
c.titulo_C AS titilo_categoria ,
c.descripcion_c as descripcion_categoria
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
```
### Despues de crear view `CatPIEz` voy var si todo funciona
```
SHOW * FROM CatPIEz;
```

| id_pieza | titulo_p            | descripcion_p       | imagen       | url                         | titilo_categoria | descripcion_categoria                  |
|:----------:|:---------------------:|:---------------------:|:--------------:|:-----------------------------:|:------------------:|:----------------------------------------:|
|        1 | El Pensador         | Escultura de Rodin  | pensador.jpg | http://ejemplo.com/pensador | Escultura        | Obras hechas en piedra, metal o madera |
|        2 | La Noche Estrellada | Pintura de Van Gogh | noche.jpg    | http://ejemplo.com/noche    | Pintura          | Cuadros en óleo o acrílico             |

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
## MYSQL
```
SHOW DATABASES;
CREATE DATABASE portafolio;
USE portafolio;
CREATE TABLE Categoria(
    Id_cat INT Primary Key,
    titulo_c VARCHAR(255),
    descripcion_c VARCHAR(255)
);
CREATE TABLE Pieza(
    id_pieza INT Primary Key,
    titulo_p VARCHAR(255),
    descripcion_p VARCHAR(255),
    imagen VARCHAR(255),
    url VARCHAR(255),
    id_categoria INT,
    CONSTRAINT FK_catogaria FOREIGN KEY (id_categoria) REFERENCES Categoria(Id_cat)
);
DESCRIBE Categoria;
DESCRIBE Pieza;

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (1, 'Escultura', 'Obras hechas en piedra, metal o madera');

INSERT INTO Categoria (Id_cat, titulo_c, descripcion_c)
VALUES (2, 'Pintura', 'Cuadros en óleo o acrílico');

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (1, 'El Pensador', 'Escultura de Rodin', 'pensador.jpg', 'http://ejemplo.com/pensador', 1);

INSERT INTO Pieza (id_pieza, titulo_p, descripcion_p, imagen, url, id_categoria)
VALUES (2, 'La Noche Estrellada', 'Pintura de Van Gogh', 'noche.jpg', 'http://ejemplo.com/noche', 2);
SELECT p.*, c.titulo_c, c.descripcion_c
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
CREATE VIEW CatPIEz AS 
SELECT
p.id_pieza,
p.titulo_p,
p.descripcion_p,
p.imagen,
p.url,
c.titulo_C AS titilo_categoria ,
c.descripcion_c as descripcion_categoria
FROM Pieza p
LEFT JOIN Categoria c ON p.id_categoria = c.Id_cat;
SHOW * FROM CatPIEz;
```
## Python
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

``` 

# 4.-Cierre/Conclusión enlazando con la unidad