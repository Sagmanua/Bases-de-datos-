import sqlite3

conecion = sqlite3.connect("empresas.db")

cursor = conecion.cursor()

print("programa agenda SQLlite v0.1 Bohdan SYdorenko")
print("Escoge una opcion;\n")
while True:
    opcion =int(input("seleciona opcion"))
    if opcion == 1:
        nombre = input("INtroduce nombre")
        apellidos = input("introduce")
        email = input("introduce")
        cursor.execute(
        "INSERT INTO clientes VALUES (NULL, '" + nombre + "', '" + apellidos + "', '" + email + "')"
        )

        conecion.commit()

        print("opcion1")
    elif opcion == 2:
        print("opcion 2")
        filas = cursor.fetchall()

        cursor.execute('''
            SELECT * FROM clientes
            

        ''')

        filas = cursor.fetchall()

        for filla in filas:
            print(filla)


        conecion.commit()
    elif opcion == 3:
        print("Enter the ID of the user to delete:")
        dele = int(input())
        cursor.execute("DELETE FROM users WHERE idificador = ?", (dele,))
        conecion.commit() 
