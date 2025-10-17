import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conectar a la base de datos
conexion = sqlite3.connect("empresas.db")
cursor = conexion.cursor()

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda SQLite v0.1 - Bohdan Sydorenko")
root.geometry("700x500")

# Funciones
def listar_clientes():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM clientes")
    for fila in cursor.fetchall():
        tree.insert("", tk.END, values=fila)

def crear_cliente():
    def guardar():
        nombre = nombre_entry.get()
        apellidos = apellidos_entry.get()
        email = email_entry.get()
        if nombre and apellidos and email:
            cursor.execute(
                "INSERT INTO clientes VALUES(NULL, ?, ?, ?)", (nombre, apellidos, email)
            )
            conexion.commit()
            listar_clientes()
            top.destroy()
            messagebox.showinfo("Éxito", "Cliente creado correctamente.")
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios.")

    top = tk.Toplevel(root)
    top.title("Crear Cliente")
    top.geometry("300x200")

    tk.Label(top, text="Nombre:").pack(pady=5)
    nombre_entry = tk.Entry(top)
    nombre_entry.pack()

    tk.Label(top, text="Apellidos:").pack(pady=5)
    apellidos_entry = tk.Entry(top)
    apellidos_entry.pack()

    tk.Label(top, text="Email:").pack(pady=5)
    email_entry = tk.Entry(top)
    email_entry.pack()

    tk.Button(top, text="Guardar", command=guardar, bg="green", fg="white").pack(pady=10)

def actualizar_cliente():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Error", "Selecciona un cliente para actualizar.")
        return
    values = tree.item(selected, 'values')
    
    def guardar():
        nombre = nombre_entry.get()
        apellidos = apellidos_entry.get()
        email = email_entry.get()
        cursor.execute(
            "UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE idificador=?",
            (nombre, apellidos, email, values[0])
        )
        conexion.commit()
        listar_clientes()
        top.destroy()
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")

    top = tk.Toplevel(root)
    top.title("Actualizar Cliente")
    top.geometry("300x200")

    tk.Label(top, text="Nombre:").pack(pady=5)
    nombre_entry = tk.Entry(top)
    nombre_entry.insert(0, values[1])
    nombre_entry.pack()

    tk.Label(top, text="Apellidos:").pack(pady=5)
    apellidos_entry = tk.Entry(top)
    apellidos_entry.insert(0, values[2])
    apellidos_entry.pack()

    tk.Label(top, text="Email:").pack(pady=5)
    email_entry = tk.Entry(top)
    email_entry.insert(0, values[3])
    email_entry.pack()

    tk.Button(top, text="Guardar", command=guardar, bg="blue", fg="white").pack(pady=10)

def eliminar_cliente():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Error", "Selecciona un cliente para eliminar.")
        return
    values = tree.item(selected, 'values')
    confirm = messagebox.askyesno("Confirmar", f"¿Eliminar cliente {values[1]} {values[2]}?")
    if confirm:
        cursor.execute("DELETE FROM clientes WHERE idificador=?", (values[0],))
        conexion.commit()
        listar_clientes()
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")

# Interfaz de árbol (tabla)
tree = ttk.Treeview(root, columns=("ID", "Nombre", "Apellidos", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellidos", text="Apellidos")
tree.heading("Email", text="Email")
tree.column("ID", width=50)
tree.column("Nombre", width=150)
tree.column("Apellidos", width=200)
tree.column("Email", width=250)
tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Botones
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Crear Cliente", command=crear_cliente, bg="green", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame, text="Actualizar Cliente", command=actualizar_cliente, bg="blue", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame, text="Eliminar Cliente", command=eliminar_cliente, bg="red", fg="white").grid(row=0, column=2, padx=5)
tk.Button(frame, text="Listar Clientes", command=listar_clientes, bg="orange", fg="white").grid(row=0, column=3, padx=5)

# Cargar clientes al iniciar
listar_clientes()

# Ejecutar ventana
root.mainloop()
conexion.close()
