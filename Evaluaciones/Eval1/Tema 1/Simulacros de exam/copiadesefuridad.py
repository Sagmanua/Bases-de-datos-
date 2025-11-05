import mysql.connector
try:
    conexion=mysql.connector.connect(
        host="localhost",
        user="appuser",
        password="m1ClaveSegura!",
        database="portafolio"
    )
    cursor = conexion.cursor()

    
    print("✅ Conexión exitosa!")
    print("Hola tu redacta database portafolio")
    while True:
        cursor = conexion.cursor()
        print("Escoge una opcion:")
        print("1.-Insertar un cliente")
        print("2.-Listar los clientes")
        print("3.-Actualizar un cliente")
        print("4.-Borrar un cliente")
        opcion = int(input("Escoge una opcion:"))

        if opcion == 1:
            print("Escoge una opcion:")
            print("1.Insertar en tabla de Categoria")
            print("2.Insertar en tabla de Pieza")
            opciondeinsetar = int(input("Escoge una opcion:"))
            if opciondeinsetar == 1:
                Id_cat = input("Id_cat INT: ")
                titulo_c = input("titulo_c VARCHAR(255): ")
                descripcion_c = input("descripcion_c VARCHAR(255): ")

                cursor.execute(
        '''INSERT INTO Categoria
VALUES ('''+ Id_cat + ''',\'''' + titulo_c + '''\',\'''' + descripcion_c + '''\'
);'''
    )
                conexion.commit()
            elif opciondeinsetar == 2:
                id_pieza = input("id_pieza INT: ")
                titulo_p = input("titulo_p VARCHAR(255): ")
                descripcion_p = input("descripcion_p VARCHAR(255): ")
                imagen = input("imagen: ")
                tiurltulo_p = input("tiurltulo_p: ")
                id_categoria = input("id_categoria INT: ")

                cursor.execute('''
                    INSERT INTO Pieza
                    VALUES (
                    '''+id_pieza+''',
                    "''' + titulo_p + '''",
                    "''' + descripcion_p + '''",
                    "''' + imagen + '''",
                    "''' + tiurltulo_p + '''",
                    '''+id_categoria+'''
                    );
                ''')
                conexion.commit()
            else:
                print("Numero incorecta")
        elif opcion == 2:
            print("Listamos los clientes")
            cursor.execute("SELECT * FROM CatPIEz")
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)
        elif opcion == 3:
            break
    cursor.close() 
    conexion.close()




except Exception as e:
    print("❌ Error:", e)



