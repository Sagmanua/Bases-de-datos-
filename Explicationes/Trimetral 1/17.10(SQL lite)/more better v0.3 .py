import sys
import sqlite3
import csv
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit, QLabel, QDialog, QFileDialog
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import Counter

# ----------------- Conexión a SQLite -----------------
conexion = sqlite3.connect("empresas.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    idificador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conexion.commit()

# ----------------- Diálogo Crear/Editar Cliente -----------------
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
        save_button = QPushButton("💾 Guardar")
        save_button.setStyleSheet("background-color: #4CAF50; color: white;")
        save_button.clicked.connect(self.accept)
        cancel_button = QPushButton("❌ Cancelar")
        cancel_button.setStyleSheet("background-color: #f44336; color: white;")
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

# ----------------- Ventana Principal -----------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda SQLite v0.1 - Mini CRM")
        self.setGeometry(100, 100, 900, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Resumen
        self.resumen_label = QLabel()
        self.resumen_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.layout.addWidget(self.resumen_label)

        # Barra de búsqueda
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Buscar por nombre, apellido o email")
        self.search_input.textChanged.connect(self.buscar_clientes)
        search_layout.addWidget(QLabel("Buscar:"))
        search_layout.addWidget(self.search_input)
        self.layout.addLayout(search_layout)

        # Tabla de clientes
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Apellidos", "Email"])
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.layout.addWidget(self.table)

        # Botones
        button_layout = QHBoxLayout()
        self.create_btn = QPushButton("➕ Crear Cliente")
        self.create_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        self.create_btn.clicked.connect(self.crear_cliente)

        self.update_btn = QPushButton("✏️ Actualizar Cliente")
        self.update_btn.setStyleSheet("background-color: #2196F3; color: white;")
        self.update_btn.clicked.connect(self.actualizar_cliente)

        self.delete_btn = QPushButton("🗑️ Eliminar Cliente")
        self.delete_btn.setStyleSheet("background-color: #f44336; color: white;")
        self.delete_btn.clicked.connect(self.eliminar_cliente)

        self.refresh_btn = QPushButton("🔄 Refrescar")
        self.refresh_btn.setStyleSheet("background-color: #FF9800; color: white;")
        self.refresh_btn.clicked.connect(self.listar_clientes)

        self.export_btn = QPushButton("📤 Exportar CSV")
        self.export_btn.setStyleSheet("background-color: #9C27B0; color: white;")
        self.export_btn.clicked.connect(self.exportar_csv)

        button_layout.addWidget(self.create_btn)
        button_layout.addWidget(self.update_btn)
        button_layout.addWidget(self.delete_btn)
        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.export_btn)
        self.layout.addLayout(button_layout)

        # Gráfico clientes por letra inicial
        self.figure = Figure(figsize=(4,3))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.listar_clientes()

    # ----------------- Funciones -----------------
    def actualizar_resumen(self):
        cursor.execute("SELECT COUNT(*) FROM clientes")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT nombre, apellidos, email FROM clientes ORDER BY idificador DESC LIMIT 3")
        recientes = cursor.fetchall()
        resumen_text = f"📊 Total clientes: {total}\n🆕 Últimos clientes:\n"
        for r in recientes:
            resumen_text += f"   - {r[0]} {r[1]} ({r[2]})\n"
        self.resumen_label.setText(resumen_text)

    def listar_clientes(self):
        self.table.setRowCount(0)
        cursor.execute("SELECT * FROM clientes")
        data = cursor.fetchall()
        for fila in data:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            for i, val in enumerate(fila):
                self.table.setItem(row_pos, i, QTableWidgetItem(str(val)))
        self.actualizar_resumen()
        self.actualizar_grafico(data)

    def buscar_clientes(self):
        term = self.search_input.text().lower()
        self.table.setRowCount(0)
        cursor.execute("SELECT * FROM clientes")
        for fila in cursor.fetchall():
            if term in fila[1].lower() or term in fila[2].lower() or term in fila[3].lower():
                row_pos = self.table.rowCount()
                self.table.insertRow(row_pos)
                for i, val in enumerate(fila):
                    self.table.setItem(row_pos, i, QTableWidgetItem(str(val)))

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

    def exportar_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "CSV Files (*.csv)")
        if path:
            cursor.execute("SELECT * FROM clientes")
            data = cursor.fetchall()
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Nombre", "Apellidos", "Email"])
                writer.writerows(data)
            QMessageBox.information(self, "Éxito", f"Datos exportados a {path}")

    def actualizar_grafico(self, data):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        letras = [c[1][0].upper() for c in data if c[1]]
        counter = Counter(letras)
        ax.bar(counter.keys(), counter.values(), color="#4CAF50")
        ax.set_title("Clientes por inicial del nombre")
        ax.set_xlabel("Inicial")
        ax.set_ylabel("Cantidad")
        self.canvas.draw()

# ----------------- Ejecutar aplicación -----------------
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
