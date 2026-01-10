

# 1.-Indroduccion brece y contexalizacion

l análisis de datos es una parte fundamental en el desarrollo de aplicaciones y sistemas de información. En este proyecto se busca comprender cómo obtener, procesar y visualizar información almacenada en una base de datos MySQL utilizando Python. Para ello, se realizan consultas agrupadas (GROUP BY) que permiten resumir grandes volúmenes de información y extraer patrones relevantes, como la cantidad de productos por categoría o por color. Posteriormente, los resultados obtenidos se representan mediante gráficos de barras utilizando la librería matplotlib, lo que facilita la interpretación visual de los datos.



# 2.-Desarrollo técnico correcto y preciso
## crear_productos.sgl
### crear tabla de `productos` 
```
CREATE TABLE productos(
  nombre VARCHAR(255),
  precio DECIMAL(10,2),
  categoria VARCHAR(255),
  peso DECIMAL(10,2),
  stock INT,
  color VARCHAR(100)
);

```
### hago `insert` valores `productos`
```
INSERT INTO productos (nombre, precio, categoria, peso, stock, color) VALUES
('Laptop Ultrafina', 899.99, 'Electrónica', 1.20, 10, 'Negro'),
('Smartphone Pro X', 699.50, 'Electrónica', 0.40, 25, 'Negro'),
('Auriculares Bluetooth', 59.99, 'Electrónica', 0.15, 50, 'Blanco'),
('Teclado Mecánico', 89.90, 'Electrónica', 0.90, 20, 'Blanco'),
('Ratón Inalámbrico', 24.99, 'Electrónica', 0.10, 50, 'Rojo'),

('Camiseta Básica', 12.99, 'Ropa', 0.30, 100, 'Azul'),
('Sudadera con Capucha', 29.99, 'Ropa', 0.60, 40, 'Negro'),
('Pantalón Vaquero', 45.00, 'Ropa', 0.80, 35, 'Azul'),
('Chaqueta Ligera', 55.50, 'Ropa', 0.75, 20, 'Verde'),
('Gorra de Algodón', 9.99, 'Ropa', 0.20, 60, 'Rojo'),

('Silla Ergonómica', 149.90, 'Muebles', 12.00, 15, 'Negro'),
('Mesa de Escritorio', 199.99, 'Muebles', 25.00, 8, 'Blanco'),
('Estantería Modular', 89.00, 'Muebles', 18.20, 12, 'Marrón'),
('Lámpara LED', 39.90, 'Muebles', 1.10, 30, 'Blanco'),
('Sofá de Dos Plazas', 399.00, 'Muebles', 30.00, 5, 'Gris'),

('Taladro Percutor', 79.99, 'Herramientas', 2.50, 18, 'Rojo'),
('Destornillador Eléctrico', 29.99, 'Herramientas', 0.90, 40, 'Amarillo'),
('Caja de Herramientas', 59.50, 'Herramientas', 4.00, 25, 'Negro'),
('Llave Inglesa', 12.00, 'Herramientas', 0.35, 60, 'Plateado'),
('Martillo Profesional', 14.50, 'Herramientas', 0.70, 30, 'Negro'),

('Cafetera Automática', 129.00, 'Hogar', 3.50, 20, 'Negro'),
('Batidora de Mano', 24.99, 'Hogar', 0.80, 40, 'Blanco'),
('Tostadora 2 Ranuras', 29.99, 'Hogar', 1.20, 35, 'Rojo'),
('Aspiradora Ciclónica', 159.00, 'Hogar', 5.00, 10, 'Gris'),
('Freidora de Aire', 89.00, 'Hogar', 4.00, 25, 'Negro'),

('Cuaderno A5', 3.99, 'Papelería', 0.25, 200, 'Azul'),
('Bolígrafo Azul', 0.50, 'Papelería', 0.02, 500, 'Azul'),
('Rotulador Fluorescente', 1.20, 'Papelería', 0.03, 300, 'Amarillo'),
('Agenda 2025', 12.99, 'Papelería', 0.40, 80, 'Negro'),
('Carpeta de Plástico', 2.50, 'Papelería', 0.12, 150, 'Rojo'),

('Zapatillas Running', 65.00, 'Deporte', 0.90, 30, 'Azul'),
('Mancuernas 5kg', 25.00, 'Deporte', 10.00, 20, 'Negro'),
('Esterilla Yoga', 19.90, 'Deporte', 1.10, 45, 'Verde'),
('Balón de Fútbol', 18.50, 'Deporte', 0.45, 35, 'Blanco'),
('Bicicleta MTB', 499.00, 'Deporte', 14.00, 6, 'Rojo'),

('Jarrón Cerámico', 15.50, 'Decoración', 1.50, 40, 'Blanco'),
('Cuadro Abstracto', 49.99, 'Decoración', 2.20, 12, 'Azul'),
('Alfombra Suave', 89.00, 'Decoración', 4.50, 10, 'Gris'),
('Cortinas Opacas', 29.99, 'Decoración', 1.00, 25, 'Beige'),
('Espejo Redondo', 35.00, 'Decoración', 3.00, 15, 'Dorado');
```
## 007-plantilla python mysql.py
### import  `mysql.connector` 
```
import mysql.connector 
```
### conecta a bases de datos 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()        
```
### crear codigo para ejectar en base de datos
```
cursor.execute('''
  SELECT 
    FLOOR(AVG(edad))
  FROM clientes;
''')  
```
### crear variable para mostar response de base de datos y imprimir en console
```
filas = cursor.fetchall()

print(filas)
```


## 014-categorias.py
### import  `mysql.connector` 
```
import mysql.connector 
```
### conecta a bases de datos 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()        
```
### hago un  `select` donde cambio + ORDEN POR `categoria` a despues si es simular por  `numero` 
```
cursor.execute('''SELECT 
                  COUNT(categoria) AS numero,
                  categoria
                  FROM productos
                  GROUP BY categoria
                  ORDER BY numero DESC;''')
```
### declara varible que tiene valor que coje de base de datos
```
filas = cursor.fetchall()
```
### declara 2 listas 
```
cantidades = []
etiquetas = []
```
### gurdar informacion de `filas` en listas `cantidades` y `etiquetas` 
```
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
```
### imprimir listas en terminal
```
print(cantidades)
print(etiquetas)
```
### con `matplotlib.pyplot` creo diagram
```
pt.pie(cantidades,labels=etiquetas)
pt.show()
```
## 016-grafico de barra.py
## 014-categorias.py
### import  `mysql.connector` 
```
import mysql.connector 
```
### conecta a bases de datos 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()        
```
### hago un  `select` donde cambio + ORDEN POR `categoria` a despues si es simular por  `numero` 
```
cursor.execute('''SELECT 
                  COUNT(categoria) AS numero,
                  categoria
                  FROM productos
                  GROUP BY categoria
                  ORDER BY numero DESC;''')
```
### declara varible que tiene valor que coje de base de datos
```
filas = cursor.fetchall()
```
### declara 2 listas 
```
cantidades = []
etiquetas = []
```
### gurdar informacion de `filas` en listas `cantidades` y `etiquetas` 
```
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
```
### imprimir listas en terminal
```
print(cantidades)
print(etiquetas)
```
### con `matplotlib.pyplot` creo grafico con max altura es 30
```
pt.bar(cantidades,height=30)
pt.show()
```

## 017-colores.py
### import  `mysql.connector` 
```
import mysql.connector 
```
### conecta a bases de datos 
```
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)
cursor = conexion.cursor()        
```
### hago un  `select` donde cambio + ORDEN POR `categoria` a despues si es simular por  `numero` 
```
cursor.execute('''SELECT 
                  COUNT(categoria) AS numero,
                  categoria
                  FROM productos
                  GROUP BY categoria
                  ORDER BY numero DESC;''')
```
### declara varible que tiene valor que coje de base de datos
```
filas = cursor.fetchall()
```
### declara 2 listas 
```
cantidades = []
etiquetas = []
```
### gurdar informacion de `filas` en listas `cantidades` y `etiquetas` 
```
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
```
### imprimir listas en terminal
```
print(cantidades)
print(etiquetas)
```
### declara los colores de pie en grafico 
```colores = ['red','green','blue']


```
### con `matplotlib.pyplot` creo grafico pero con valores que declara antes
```
pt.pie(cantidades,labels=etiquetas,colors=colores)

pt.show()
```

# Codigo Completo
Project\  
├─ explicacion.md 
├─ 007-plantilla python mysql.py  
├─ 014-categorias.py  
├─ 016-grafico de barra.py  
├─ 017-colores.py  
└─ crear_productos.sql  
## crear_productos.sql
```
CREATE TABLE productos(
  nombre VARCHAR(255),
  precio DECIMAL(10,2),
  categoria VARCHAR(255),
  peso DECIMAL(10,2),
  stock INT,
  color VARCHAR(100)
);
INSERT INTO productos (nombre, precio, categoria, peso, stock, color) VALUES
('Laptop Ultrafina', 899.99, 'Electrónica', 1.20, 10, 'Negro'),
('Smartphone Pro X', 699.50, 'Electrónica', 0.40, 25, 'Negro'),
('Auriculares Bluetooth', 59.99, 'Electrónica', 0.15, 50, 'Blanco'),
('Teclado Mecánico', 89.90, 'Electrónica', 0.90, 20, 'Blanco'),
('Ratón Inalámbrico', 24.99, 'Electrónica', 0.10, 50, 'Rojo'),

('Camiseta Básica', 12.99, 'Ropa', 0.30, 100, 'Azul'),
('Sudadera con Capucha', 29.99, 'Ropa', 0.60, 40, 'Negro'),
('Pantalón Vaquero', 45.00, 'Ropa', 0.80, 35, 'Azul'),
('Chaqueta Ligera', 55.50, 'Ropa', 0.75, 20, 'Verde'),
('Gorra de Algodón', 9.99, 'Ropa', 0.20, 60, 'Rojo'),

('Silla Ergonómica', 149.90, 'Muebles', 12.00, 15, 'Negro'),
('Mesa de Escritorio', 199.99, 'Muebles', 25.00, 8, 'Blanco'),
('Estantería Modular', 89.00, 'Muebles', 18.20, 12, 'Marrón'),
('Lámpara LED', 39.90, 'Muebles', 1.10, 30, 'Blanco'),
('Sofá de Dos Plazas', 399.00, 'Muebles', 30.00, 5, 'Gris'),

('Taladro Percutor', 79.99, 'Herramientas', 2.50, 18, 'Rojo'),
('Destornillador Eléctrico', 29.99, 'Herramientas', 0.90, 40, 'Amarillo'),
('Caja de Herramientas', 59.50, 'Herramientas', 4.00, 25, 'Negro'),
('Llave Inglesa', 12.00, 'Herramientas', 0.35, 60, 'Plateado'),
('Martillo Profesional', 14.50, 'Herramientas', 0.70, 30, 'Negro'),

('Cafetera Automática', 129.00, 'Hogar', 3.50, 20, 'Negro'),
('Batidora de Mano', 24.99, 'Hogar', 0.80, 40, 'Blanco'),
('Tostadora 2 Ranuras', 29.99, 'Hogar', 1.20, 35, 'Rojo'),
('Aspiradora Ciclónica', 159.00, 'Hogar', 5.00, 10, 'Gris'),
('Freidora de Aire', 89.00, 'Hogar', 4.00, 25, 'Negro'),

('Cuaderno A5', 3.99, 'Papelería', 0.25, 200, 'Azul'),
('Bolígrafo Azul', 0.50, 'Papelería', 0.02, 500, 'Azul'),
('Rotulador Fluorescente', 1.20, 'Papelería', 0.03, 300, 'Amarillo'),
('Agenda 2025', 12.99, 'Papelería', 0.40, 80, 'Negro'),
('Carpeta de Plástico', 2.50, 'Papelería', 0.12, 150, 'Rojo'),

('Zapatillas Running', 65.00, 'Deporte', 0.90, 30, 'Azul'),
('Mancuernas 5kg', 25.00, 'Deporte', 10.00, 20, 'Negro'),
('Esterilla Yoga', 19.90, 'Deporte', 1.10, 45, 'Verde'),
('Balón de Fútbol', 18.50, 'Deporte', 0.45, 35, 'Blanco'),
('Bicicleta MTB', 499.00, 'Deporte', 14.00, 6, 'Rojo'),

('Jarrón Cerámico', 15.50, 'Decoración', 1.50, 40, 'Blanco'),
('Cuadro Abstracto', 49.99, 'Decoración', 2.20, 12, 'Azul'),
('Alfombra Suave', 89.00, 'Decoración', 4.50, 10, 'Gris'),
('Cortinas Opacas', 29.99, 'Decoración', 1.00, 25, 'Beige'),
('Espejo Redondo', 35.00, 'Decoración', 3.00, 15, 'Dorado');
```


## 007-plantilla python mysql.py
 ``` 
import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)                                      
  
cursor = conexion.cursor() 
cursor.execute('''
  SELECT 
    FLOOR(AVG(edad))
  FROM clientes;
''')  

filas = cursor.fetchall()

print(filas)
```
## 014-categorias.py
```
import mysql.connector 
import matplotlib.pyplot as pt
conexion = mysql.connector.connect(
  host="localhost",user="clientes",password="Clientes123$",database="clientes"
)                                      
cursor = conexion.cursor() 
cursor.execute('''SELECT 
                  COUNT(categoria) AS numero,
                  categoria
                  FROM productos
                  GROUP BY categoria
                  ORDER BY numero DESC;''')  
filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)
pt.pie(cantidades,labels=etiquetas)
pt.show()
```
## 016-grafico de barra.py
```
import mysql.connector 
import matplotlib.pyplot as pt
conexion = mysql.connector.connect(
  host="localhost",user="clientes",password="Clientes123$",database="clientes"
)                                      
cursor = conexion.cursor() 
cursor.execute('''SELECT 
                  COUNT(stock) AS numero,
                  stock
                  FROM productos
                  GROUP BY stock
                  ORDER BY numero DESC;''')  
filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)
pt.bar(cantidades,height=30)
pt.show()
```
## 017-colores.py
```
import mysql.connector 
import matplotlib.pyplot as pt
conexion = mysql.connector.connect(
  host="localhost",user="clientes",password="Clientes123$",database="clientes"
)                                      
cursor = conexion.cursor() 
cursor.execute('''SELECT 
                  COUNT(categoria) AS numero,
                  categoria
                  FROM productos
                  GROUP BY categoria
                  ORDER BY numero DESC;''')  
filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
  cantidades.append(fila[0])
  etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)
colores = ['red','green','blue']
pt.pie(cantidades,labels=etiquetas,colors=colores)
pt.show()
```
# 4.-Cierre/Conclusión enlazando con la unidad

El desarrollo de esta práctica ha permitido aplicar de forma integrada los contenidos de la unidad dedicados a la gestión y análisis de datos. A través del uso de consultas SQL con agrupamiento y de su posterior visualización en Python, se ha reforzado la comprensión del papel que desempeña cada tecnología dentro del proceso de análisis: MySQL como herramienta para estructurar y extraer información relevante, y Python como lenguaje versátil para transformar y representar visualmente esos datos.
Gracias a este trabajo, se evidencia cómo ambos recursos se complementan para generar información clara, útil y fácilmente interpretable, lo que constituye una competencia esencial en el ámbito del análisis de datos y el desarrollo de aplicaciones. Esta práctica, en definitiva, consolida los conocimientos de la unidad y muestra su aplicabilidad en escenarios reales

