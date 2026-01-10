# 1.-Indroduccion brece y contexalizacion

Este ejercicio consiste en crear una aplicación simple que conecta Flask con una base de datos MySQL. A través de la creación de la base de datos, usuarios con permisos, endpoints y una interfaz HTML, aprenderás cómo una aplicación web puede almacenar, consultar y mostrar información de manera dinámica.



# 2.-Desarrollo técnico correcto y preciso
## Crear la Base de Datos.sql  
### creo una base de datos `tiendaclase`
```
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;
```
### dentro de este bases de datos creo tabla `clientes`
```
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);
```
## Crear un Usuario con Permisos.sql
### creo un usario de mysql 
```
-- crea usuario nuevo con contraseña
CREATE USER 'tiendaclase'@'localhost' IDENTIFIED BY 'Tiendaclase123$';

-- permite acceso a ese usuario
GRANT ALL PRIVILEGES ON tiendaclase.* TO 'tiendaclase'@'localhost';
FLUSH PRIVILEGES;
```

## mysql.py
### import `import mysql.connector `
```
import mysql.connector 
```  
### creo un Configuración de la conexión a base de datos 
```
config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

conexion = mysql.connector.connect(**config)
```
## endpoint.py  
### import `import mysql.connector ` `flask` `json`
```
import mysql.connector 
from flask import Flask, render_template
import json
```  
### creo un Configuración de la conexión a base de datos 
```
config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

conexion = mysql.connector.connect(**config)
app = Flask(__name__)
```
### create endpoint `/clientes`
```
@app.route("/clientes")
def clientes():
```
#### dentro de este endpoint `SELECT` todo valores de la  `clientes`
```
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  
filas = cursor.fetchall()
return json.dumps(filas)
```

### create endpoint `/tablas`
```
@app.route("/tablas")
def tablas():
```
#### dentro de este endpoint `show` todo los tablas de data base `tiendaclase`
```
    cursor = conexion.cursor() 
    cursor.execute("SHOW TABLES;")  
    filas = cursor.fetchall()
    tablas = []
    for fila in filas:
        tablas.append(fila[0])
    return json.dumps(tablas)

```



## index.html
### Despues de crear una gile `index.html` voy a hacer una pagina
### Código básico para una estructura de do
```
<!doctype html>
<html lang="es">
  <head>
    <!-- Añade tu contenido aquí -->
  </head>
  <body>
    <!-- Añade tu contenido aquí -->
  </body>
</html>
```
### Esribo `head` en que guardo configuraciones y enlaces necesarios para que la página funcione y se vea bien, pero no muestra contenido en la pantalla.
```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
```
### Esribo `<body>` que es contiene todo lo que se muestra en la pantalla: encabezado, menú, contenido principal y pie de página
```
<body>
    <header>Encabezado</header>
    <nav>Menú Navegación</nav>
    <main>
        <section class="item">Sección 1</section>
        <section class="item">Sección 2</section>
        <section class="item">Sección 3</section>
    </main>
    <footer>Pie de página</footer>
</body>
```
### Esribo `<script>` que es contiene el JavaSript codigo dentro de etiqutas 
```
let hoy = new Date();
console.log(hoy);
```
### con `fetch` hace HTTP para server
```
 fetch('/clientes')
```

### luego transfer estos datos a json file
```
.then(response => response.json())
```
### encontro todos elementos `clientes`
 ```
const clientes = document.getElementById('clientes');
 ```
### hace con todos y converntir a listo 
 ```
data.forEach(cliente => {
    clientes.innerHTML += `<li>${cliente.nombre} - ${cliente.email}</li>`;
});
 ```
### con `fetch` hace HTTP para server
```
fetch('/tablas')
```

### luego transfer estos datos a json file
```
.then(response => response.json())
```
### informacion que encontre mustro en la console
```
.then(data => {
    console.log(data);
});
```
# Codigo Completo
Project\  
├─ tempaltes
|    ├─ index.html
├─ explicacion.md  
├─ Crear la Base de Datos.sql  
├─ Crear un Usuario con Permisos.sql  
├─ endpoint.py  
└─ mysql.py   
## Crear la Base de Datos.sql  
```
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tiendaclase;
USE tiendaclase;

-- Tabla clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    fecha_registro VARCHAR(100)
);
```
## Crear un Usuario con Permisos.sql
```
-- crea usuario nuevo con contraseña
CREATE USER 'tiendaclase'@'localhost' IDENTIFIED BY 'Tiendaclase123$';

-- permite acceso a ese usuario
GRANT ALL PRIVILEGES ON tiendaclase.* TO 'tiendaclase'@'localhost';
FLUSH PRIVILEGES;
```
## mysql.py
```
import mysql.connector 

config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

conexion = mysql.connector.connect(**config)
```
## endpoint.py  
```
import mysql.connector 
from flask import Flask, render_template
import json

config = {
    'host': 'localhost',
    'user': 'tiendaclase',
    'password': 'Tiendaclase123$',
    'database': 'tiendaclase'
}

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
```
## index.html
```
<!doctype html>
<html>
   <head>
       <style>
           html,body{height:100%;padding:0px;margin:0px;display:flex;width:100%;}
           nav{background:indigo;flex:1;color:white;padding:20px;}
           section{flex:3;background:#f4f4f9;padding:20px;}
       </style>
   </head>
   <body>
       <nav>Menu</nav>
       <section>
           <h1>Clientes</h1>
           <ul id="clientes"></ul>
       </section>

       <script>
           fetch('/clientes')
               .then(response => response.json())
               .then(data => {
                   const clientes = document.getElementById('clientes');
                   data.forEach(cliente => {
                       clientes.innerHTML += `<li>${cliente.nombre} - ${cliente.email}</li>`;
                   });
               });

           fetch('/tablas')
               .then(response => response.json())
               .then(data => {
                   console.log(data);
               });
       </script>
   </body>
</html>
```


# 4.-Cierre/Conclusión enlazando con la unidad

Asegúrate de que todo funcione correctamente y prueba los endpoints desde el navegador. Visita http://127.0.0.1:5000/clientes para ver la lista de clientes y http://127.0.0.1:5000/tablas para ver las tablas disponibles en la base de datos.

Este ejercicio te permite practicar la creación de una base de datos, el manejo de usuarios con permisos, y la interacción con una base de datos desde Flask utilizando endpoints RESTful.