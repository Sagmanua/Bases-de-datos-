import mysql.connector
try:
    mysql.connector.connect(
        host="localhost",
        user="backupuser",
        password="clave_segura",
        database="mi_base"
    )
    print("✅ Conexión exitosa!")
except Exception as e:
    print("❌ Error:", e)