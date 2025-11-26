```mermaid
erDiagram
    alumnos {
        int Ideficador PK
        string nombre
        string apellidos

    }

    profesores {
        int Identificador PK
        string nombre
        string apellidos
    }

    asignaturas {
        int Identificador PK
        string nombre
        string apellidos
        int id_profesor FK
    }

    matriculas {
        int Identificador PK
        int id_alumno FK
        int id_asignatura FK
    }

    alumnos ||--o{ matriculas : "tiene 1:N"
    profesores }o--o{ asignaturas : "tiene M:N"
    profesores }o--o{ matriculas : "tiene M:N"
