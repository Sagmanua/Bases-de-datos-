import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit, QLabel, QDialog
)
from PyQt6.QtCore import Qt

# Conexión a SQLite
conexion = sqlite3.connect("empresas.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    idificador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conexion.commit()

# Diálogo para crear/editar cliente
class ClienteDialog(QDialog):
    def __init__(self, parent=None, cliente=None):
        super().__init__(parent)
        self.setWindowTitle("Cliente")
        self.setFixedSize(300, 200)
        layout = QVBoxLayout()

        self.nombre_entry = QLineEdit()
        self.apellidos_entry = QLineEdit()
        self.email_entry = QLineEdit()

        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.nombre_entry)
        layout.addWidget(QLabel("Apellidos:"))
        layout.addWidget(self.apellidos_entry)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_entry)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        if cliente:
            self.cliente_id = cliente[0]
            self.nombre_entry.setText(cliente[1])
            self.apellidos_entry.setText(cliente[2])
            self.email_entry.setText(cliente[3])
        else:
            self.cliente_id = None

    def get_data(self):
        return {
            "id": self.cliente_id,
            "nombre": self.nombre_entry.text(),
            "apellidos": self.apellidos_entry.text(),
            "email": self.email_entry.text()
        }

# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda SQLite v0.1 - Bohdan Sydorenko")
        self.setGeometry(100, 100, 700, 500)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Email"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # Botones
        create_btn = QPushButton("Crear Cliente")
        create_btn.setStyleSheet("background-color: green; color: white;")
        create_btn.clicked.connect(self.crear_cliente)

        update_btn = QPushButton("Actualizar Cliente")
        update_btn.setStyleSheet("background-color: blue; color: white;")
        update_btn.clicked.connect(self.actualizar_cliente)

        delete_btn = QPushButton("Eliminar Cliente")
        delete_btn.setStyleSheet("background-color: red; color: white;")
        delete_btn.clicked.connect(self.eliminar_cliente)

        refresh_btn = QPushButton("Listar Clientes")
        refresh_btn.setStyleSheet("background-color: orange; color: white;")
        refresh_btn.clicked.connect(self.listar_clientes)

        button_layout = QHBoxLayout()
        button_layout.addWidget(create_btn)
        button_layout.addWidget(update_btn)
        button_layout.addWidget(delete_btn)
        button_layout.addWidget(refresh_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.listar_clientes()

    def listar_clientes(self):
        self.table.setRowCount(0)
        cursor.execute("SELECT * FROM clientes")
        for fila in cursor.fetchall():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            for i, value in enumerate(fila):
                self.table.setItem(row_position, i, QTableWidgetItem(str(value)))

    def crear_cliente(self):
        dialog = ClienteDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            if data["nombre"] and data["apellidos"] and data["email"]:
                cursor.execute(
                    "INSERT INTO clientes VALUES(NULL, ?, ?, ?)",
                    (data["nombre"], data["apellidos"], data["email"])
                )
                conexion.commit()
                self.listar_clientes()
                QMessageBox.information(self, "Éxito", "Cliente creado correctamente.")
            else:
                QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")

    def actualizar_cliente(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Error", "Selecciona un cliente para actualizar.")
            return
        row = selected_rows[0].row()
        cliente = [self.table.item(row, i).text() for i in range(4)]
        dialog = ClienteDialog(self, cliente)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            cursor.execute(
                "UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE idificador=?",
                (data["nombre"], data["apellidos"], data["email"], data["id"])
            )
            conexion.commit()
            self.listar_clientes()
            QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente.")

    def eliminar_cliente(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Error", "Selecciona un cliente para eliminar.")
            return
        row = selected_rows[0].row()
        cliente_id = self.table.item(row, 0).text()
        cliente_nombre = self.table.item(row, 1).text()
        cliente_apellidos = self.table.item(row, 2).text()
        confirm = QMessageBox.question(
            self, "Confirmar",
            f"¿Eliminar cliente {cliente_nombre} {cliente_apellidos}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            cursor.execute("DELETE FROM clientes WHERE idificador=?", (cliente_id,))
            conexion.commit()
            self.listar_clientes()
            QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente.")

# Ejecutar aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
