import sqlite3

conecion = sqlite3.connect("empresas.db")

cursor = conecion.cursor()

nombre = input("Introduse el nombre de nombre")
apellidos = input("Introduse el nombre de apellidos")
email = input("Introduse el nombre de email")

cursor.execute('''
    INSERT INTO clientes VALUES(
        NULL,'"""+nombre+"""','"""+apellidos+"""','"""+email+"""' );
'''
)

conecion.commit()



filas = cursor.fetchall()

cursor.execute('''
    SELECT * FROM clientes
    

''')

filas = cursor.fetchall()

for filla in filas:
    print(filla)


conecion.commit()

print("all good")