# Introduce de la practica 

#  Aplicación Práctica
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 



### Abre este bases de datos que luego puedo trabajar en este bases de datos 

```
USE ejemploclaves;
```


### voy a crear tabla personas 

```
CREATE TABLE personas (
  nombre VARCHAR(50),
  apellidos VARCHAR(255)
);
```

### añado identificador
```
ALTER TABLE personas
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```

### 

```
DESRIBE personas;
```

### voy a crear tabla emails
```
CREATE TABLE emails (
  direccion VARCHAR(50),
  persona VARCHAR(255)
);
```

### añado identificador
```
ALTER TABLE emails
ADD COLUMN identificador INT AUTO_INCREMENT PRIMARY KEY FIRST;
```
### 

```
DESRIBE emails;
```



# Codigo completa 
```


```
# Conclusión enlazando con la actividad 

