import sqlite3

conecion = sqlite3.connect("empresas.db")

cursor = conecion.cursor()

cursor.execute('''
    INSERT INTO clientes VALUES(
        NULL,'Jorge','Sydorenko','email@mail.com'       )

''')

conecion.commit()
print("all good")