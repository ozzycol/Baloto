import mysql.connector

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512."  # Cambiar por tu contraseña
)

cursor = conexion.cursor()

# Crear la base de datos "loteria" si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS loteria")

# Seleccionar la base de datos
cursor.execute("USE loteria")

# Crear la tabla "baloto"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS baloto (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        balota1 INT,
        balota2 INT,
        balota3 INT,
        balota4 INT,
        balota5 INT,
        superbalota INT,
        Won INT,
        FECHA DATE
    )
""")

# Crear la tabla "revancha"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS revancha (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        balota1 INT,
        balota2 INT,
        balota3 INT,
        balota4 INT,
        balota5 INT,
        superbalota INT,
        Won INT,
        FECHA DATE
    )
""")

# Cerrar la conexión
conexion.close()

print("Base de datos y tablas creadas exitosamente.")
