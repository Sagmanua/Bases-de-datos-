## 1.-Indroduccion brece y contexalizacion
El control de acceso a los datos es una parte fundamental en la administración de bases de datos. Para garantizar la seguridad y el uso adecuado de la información, es necesario gestionar los usuarios que pueden conectarse al sistema y definir los permisos que tendrán sobre las distintas bases de datos. En esta práctica trabajaremos con MySQL para aprender a visualizar los usuarios existentes, crear nuevos usuarios y asignarles los privilegios necesarios. Estos conocimientos son esenciales para comprender cómo se organiza y protege la información dentro de un entorno de bases de datos relacional.

## 2.-Desarrollo técnico correcto y preciso
Cuando Mysql a installando esribe  `sudo mysql -u root -p` para conectar en la Mysql 

### voy a ver que usario tiene mysql

```
SELECT User, Host FROM mysql.user;
```
### Resultado
+------------------+-----------+
| User             | Host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+

### despues de veo usario crear noevo sin nombre que esta en tabla
```
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'password123';
```
#### en resultado tiene problema de contrsena no tiene contresaña bien
```
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
```
### voy a ver reqesitos de contraseña 
```
SHOW VARIABLES LIKE 'validate_password%';
```
| Variable_name                                   | Value  |
|:-------------------------------------------------:|:--------:|
| validate_password.changed_characters_percentage | 0      |
| validate_password.check_user_name               | ON     |
| validate_password.dictionary_file               |        |
| validate_password.length                        | 8      |
| validate_password.mixed_case_count              | 1      |
| validate_password.number_count                  | 1      |
| validate_password.policy                        | MEDIUM |
| validate_password.special_char_count            | 1      |

### vale ahora voy esribir contaraseña correcta
```
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'Qwerty123!';
```
### da a usario priveges de administrador
```
GRANT ALL PRIVILEGES ON empresadam.* TO 'newuser'@'localhost';
```
### guardar usario
```
FLUSH PRIVILEGES;
```

### voe que priveges tiene este usario
```
SHOW GRANTS FOR 'newuser'@'localhost';
```


## Codigo Completo

```
SELECT User, Host FROM mysql.user;
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'password123';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
SHOW VARIABLES LIKE 'validate_password%';
CREATE USER 'someone'@'localhost' IDENTIFIED BY 'Qwerty123!';
GRANT ALL PRIVILEGES ON empresadam.* TO 'newuser'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'newuser'@'localhost';
```

## 4.-Cierre/Conclusión enlazando con la unidad
En esta práctica hemos aprendido a gestionar usuarios dentro de un sistema de bases de datos relacionales, concretamente en MySQL. Conocer cómo listar, crear y asignar privilegios a los usuarios es fundamental para garantizar la seguridad y el control de acceso a la información. Estas acciones permiten administrar quién puede acceder a la base de datos, desde qué ubicación y qué operaciones puede realizar, lo cual es esencial en cualquier entorno profesional.