import mysql.connector

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)

cursor = conexion.cursor()

# Borrar los datos de la tabla "baloto"
query_baloto = "DELETE FROM baloto"
cursor.execute(query_baloto)
conexion.commit()
print("Datos de la tabla 'baloto' borrados correctamente.")

# Borrar los datos de la tabla "revancha"
query_revancha = "DELETE FROM revancha"
cursor.execute(query_revancha)
conexion.commit()
print("Datos de la tabla 'revancha' borrados correctamente.")

# Cerrar la conexión
conexion.close()
