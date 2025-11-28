import sqlite3
import os

# ANSI codes para colores y estilos
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"

# Conectar a SQLite
conexion = sqlite3.connect("empresas.db")
cursor = conexion.cursor()

# Función para limpiar la consola
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Encabezado principal
def print_header():
    print(CYAN + "="*70 + RESET)
    print(BOLD + "        🌟 Programa Agenda SQLite v0.1 - Bohdan Sydorenko 🌟" + RESET)
    print(CYAN + "="*70 + RESET)

# Menú principal
def print_menu():
    print("\n" + YELLOW + "-"*70 + RESET)
    print(BOLD + "Opciones disponibles:" + RESET)
    print("1) Crear cliente")
    print("2) Listar clientes")
    print("3) Actualizar cliente")
    print("4) Eliminar cliente")
    print("5) Salir del programa")
    print(YELLOW + "-"*70 + RESET)

# Listar clientes en tabla visual
def print_clients(filas):
    if not filas:
        print(RED + "📭 No hay clientes registrados." + RESET)
        return
    # Cabecera tabla
    print(GREEN + "+" + "-"*5 + "+" + "-"*20 + "+" + "-"*25 + "+" + "-"*30 + "+" + RESET)
    print(GREEN + f"| {'ID':<3} | {'Nombre':<18} | {'Apellidos':<23} | {'Email':<28} |" + RESET)
    print(GREEN + "+" + "-"*5 + "+" + "-"*20 + "+" + "-"*25 + "+" + "-"*30 + "+" + RESET)
    for fila in filas:
        print(f"| {fila[0]:<3} | {fila[1]:<18} | {fila[2]:<23} | {fila[3]:<28} |")
    print(GREEN + "+" + "-"*5 + "+" + "-"*20 + "+" + "-"*25 + "+" + "-"*30 + "+" + RESET)

# Resumen inicial
def print_summary():
    cursor.execute("SELECT COUNT(*) FROM clientes")
    total = cursor.fetchone()[0]
    print(MAGENTA + f"\n📊 Total de clientes registrados: {total}" + RESET)
    cursor.execute("SELECT * FROM clientes ORDER BY idificador DESC LIMIT 3")
    recientes = cursor.fetchall()
    if recientes:
        print(MAGENTA + "🆕 Últimos clientes añadidos:" + RESET)
        print_clients(recientes)

# Programa principal
clear()
print_header()
print_summary()

while True:
    print_menu()
    
    try:
        opcion = int(input(BOLD + "Selecciona opción: " + RESET))
    except ValueError:
        print(RED + "❌ Por favor, introduce un número válido." + RESET)
        continue

    if opcion == 1:
        print("\n" + CYAN + "--- Crear Cliente ---" + RESET)
        nombre = input("Introduce nombre: ")
        apellidos = input("Introduce apellidos: ")
        email = input("Introduce email: ")

        cursor.execute(
            "INSERT INTO clientes VALUES(NULL, ?, ?, ?)", (nombre, apellidos, email)
        )
        conexion.commit()
        print(GREEN + "✅ Cliente creado correctamente." + RESET)

    elif opcion == 2:
        print("\n" + CYAN + "--- Lista de Clientes ---" + RESET)
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        print_clients(filas)

    elif opcion == 3:
        print("\n" + CYAN + "--- Actualizar Cliente ---" + RESET)
        idificador = input("Introduce ID del cliente a actualizar: ")
        nombre = input("Introduce nuevo nombre: ")
        apellidos = input("Introduce nuevos apellidos: ")
        email = input("Introduce nuevo email: ")

        cursor.execute(
            "UPDATE clientes SET nombre = ?, apellidos = ?, email = ? WHERE idificador = ?",
            (nombre, apellidos, email, idificador)
        )
        conexion.commit()
        print(GREEN + "✅ Cliente actualizado correctamente." + RESET)

    elif opcion == 4:
        print("\n" + CYAN + "--- Eliminar Cliente ---" + RESET)
        idificador = input("Introduce ID del cliente a eliminar: ")

        cursor.execute(
            "DELETE FROM clientes WHERE idificador = ?", (idificador,)
        )
        conexion.commit()
        print(GREEN + "✅ Cliente eliminado correctamente." + RESET)

    elif opcion == 5:
        print(RED + "👋 Saliendo del programa..." + RESET)
        break

    else:
        print(RED + "❌ Opción no válida, intenta de nuevo." + RESET)

conexion.close()
