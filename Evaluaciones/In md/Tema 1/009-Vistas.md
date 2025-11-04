# Introduce de la practica 

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

```
# Conclusión enlazando con la actividad 

