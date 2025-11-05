# Introduce de la practica 
En este practica de bases de datos vamos a trabajar a bases de datos relaciones es común trabajar con información distribuida en diferentes tablas.Usa este para facilitar la cinculta y organizacion de BD usamos `vistas` Una vista es una tabla virtual que no almacena datos de forma independiente, sino que se genera a partir del resultado de una consulta SQL.Esto permite combinar información de varias tablas y presentarla de una manera más clara y accesible, sin duplicar datos.
#  Aplicación Práctica
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### Abre bases de datos donte esta tablas que nesisito que luego puedo trabajar en este bases de datos  

```
USE empresadam;
```

### voy a ver si tiente este tabla y su estructura 
### este es tabla de emails 
```
DESCRIBE emails;
```

| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| direccion     | varchar(50)  | YES  |     | NULL    |                |
| persona       | varchar(255) | YES  |     | NULL    |                |

### este es tabla de personas

```
DESCRIBE personas;
```

| Field         | Type         | Null | Key | Default | Extra          |
|:---------------:|:--------------:|:------:|:-----:|:---------:|:----------------:|
| identificador | int          | NO   | PRI | NULL    | auto_increment |
| nombre        | varchar(50)  | YES  |     | NULL    |                |
| apellidos     | varchar(255) | YES  |     | NULL    |                |


### voy a crear view camp 

CREATE VIEW personas_correos AS
SELECT 
    p.identificador AS id_persona,
    p.nombre,
    p.apellidos,
    e.direccion AS correo
FROM personas p
LEFT JOIN emails e
    ON p.identificador = e.persona;

### voy a ver si todo funciona 
#### es codigo
```
SELECT * FROM personas_correos;
```
#### es que paso
| id_persona | nombre       | apellidos          | correo                        |
|:------------:|:--------------:|:--------------------:|:-------------------------------:|
|          1 | Jose Vicente | Carratalá Sanchis  | jocarsa2@gmail.com            |
|          1 | Jose Vicente | Carratalá Sanchis  | info@josevicentecarratala.com |
|          1 | Jose Vicente | Carratalá Sanchis  | info@jocarsa.com              |



# Codigo completa 
```
USE empresadam;
DESCRIBE emails;
DESCRIBE personas;
CREATE VIEW personas_correos AS
SELECT 
    p.identificador AS id_persona,
    p.nombre,
    p.apellidos,
    e.direccion AS correo
FROM personas p
LEFT JOIN emails e
    ON p.identificador = e.persona;



```
# Conclusión enlazando con la actividad 
En esta actividad aprendimos a crear una vista para combinar información de dos tablas usando LEFT JOIN. La vista personas_correos nos permitió visualizar de forma sencilla los datos de personas y sus correos, demostrando cómo las vistas facilitan consultas y organización de información en bases de datos.
