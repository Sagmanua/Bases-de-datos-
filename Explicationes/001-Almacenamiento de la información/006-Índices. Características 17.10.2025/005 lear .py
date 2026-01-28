import sqlite3

conecion = sqlite3.connect("empresas.db")

cursor = conecion.cursor()

cursor.execute('''
    SELECT * FROM clientes
    

''')

filas = cursor.fetchall()

for filla in filas:
    print(filla)


conecion.commit()
print("all good")