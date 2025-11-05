## 1.-Indroduccion brece y contexalizacion





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

```
SHOW GRANTS FOR 'newuser'@'localhost';
```


## Codigo Completo

```

```

## 4.-Cierre/Conclusión enlazando con la unidad