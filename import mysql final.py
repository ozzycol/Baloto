import mysql.connector
import pandas as pd
from datetime import datetime

# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)

cursor = conexion.cursor()

# ... Código para crear las tablas ...

# Leer los datos de las pestañas "baloto" y "revancha" del archivo Excel
archivo_excel = "Baloto_Consolidado_final.xlsx"
datos_baloto = pd.read_excel(archivo_excel, sheet_name="Baloto")
datos_revancha = pd.read_excel(archivo_excel, sheet_name="Revancha")

# Insertar los datos en la tabla "baloto"
for _, fila in datos_baloto.iterrows():
    fecha = fila['FECHA']
    formatted_fecha = fecha.strftime('%Y-%m-%d')
    query = "INSERT INTO baloto (balota1, balota2, balota3, balota4, balota5, superbalota, Won, FECHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (fila['balota1'], fila['balota2'], fila['balota3'], fila['balota4'], fila['balota5'], fila['superbalota'], fila['Won'], formatted_fecha))

# Insertar los datos en la tabla "revancha"
for _, fila in datos_revancha.iterrows():
    fecha = fila['FECHA']
    formatted_fecha = fecha.strftime('%Y-%m-%d')
    query = "INSERT INTO revancha (balota1, balota2, balota3, balota4, balota5, superbalota, Won, FECHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (fila['balota1'], fila['balota2'], fila['balota3'], fila['balota4'], fila['balota5'], fila['superbalota'], fila['Won'], formatted_fecha))

conexion.commit()

print("Datos insertados correctamente.")

# Cerrar la conexión
conexion.close()