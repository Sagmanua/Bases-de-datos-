Create DATABASE 003_Tipos_de_datos;
USE 003_Tipos_de_datos;
sudo mysql -u root -p


## 1.-Indroduccion brece y contexalizacion





## 2.-Desarrollo técnico correcto y preciso

1.
```

```

2.
```

       
```
3.
```

```
4.
```
 

```
5.
```
 

```
6.
```
  
```

## Codigo Completo

```

```

## 4.-Cierre/Conclusión enlazando con la unidad





```mermaid
erDiagram
    EMPRESA {
        int id_empresa PK
        string nombre_empresa 
        string direccion
        string telefono
    }

    CLIENTE {
        int dni PK
        string nombre
        string apellidos
        string email
        int id_empresa FK
    }

    CLIENTES {
        int dni PK
        string nombre
        string apellidos
        string email
        int id_empresa FK
    }

    CLIENTES1 {
        int dni PK
        string nombre
        string apellidos
        string email
        int id_empresa FK
    }

    EMPRESA ||--o{ CLIENTE : "tiene 1:N"
    EMPRESA }o--o{ CLIENTES : "tiene M:N"
    EMPRESA }o--o{ CLIENTES1 : "tiene M:N"
    CLIENTE }o--o{ CLIENTES : "tiene M:N"



```