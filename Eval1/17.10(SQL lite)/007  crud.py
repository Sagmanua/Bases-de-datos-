import sqlite3

conexion = sqlite3.connect("empresas.db")
cursor = conexion.cursor()

print("Programa agenda SQLite v0.1 Bohdan Sydorenko")
print("Escoge una opción:")
print("1) Crear cliente")
print("2) Listar clientes")
print("3) Actualizar cliente")
print("4) Eliminar cliente")
print("5) Salir del programa")

while True:
    opcion = int(input("Selecciona opción: "))

    if opcion == 1:
        nombre = input("Introduce nombre: ")
        apellidos = input("Introduce apellidos: ")
        email = input("Introduce email: ")

        cursor.execute(
            "INSERT INTO clientes VALUES(NULL, '" + nombre + "', '" + apellidos + "', '" + email + "')"
        )
        conexion.commit()
        print("Cliente creado correctamente.")

    elif opcion == 2:
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()

        for fila in filas:
            print(fila)

    elif opcion == 3:
        idificador = input("Introduce ID del cliente a actualizar: ")
        nombre = input("Introduce nuevo nombre: ")
        apellidos = input("Introduce nuevos apellidos: ")
        email = input("Introduce nuevo email: ")

        cursor.execute(
            "UPDATE clientes SET nombre = '" + nombre + "', apellidos = '" + apellidos + "', email = '" + email + "' WHERE idificador = " + idificador
        )
        conexion.commit()
        print("Cliente actualizado correctamente.")

    elif opcion == 4:
        idificador = input("Introduce ID del cliente a eliminar: ")
        cursor.execute(
            "DELETE FROM clientes WHERE idificador = " + idificador
        )
        conexion.commit()
        print("Cliente eliminado correctamente.")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

conexion.close()
