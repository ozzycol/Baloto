import mysql.connector
import pandas as pd

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)

cursor = conexion.cursor()

# Consultar la tabla "baloto"
query_baloto = "SELECT * FROM baloto"
cursor.execute(query_baloto)
resultados_baloto = cursor.fetchall()

# Consultar la tabla "revancha"
query_revancha = "SELECT * FROM revancha"
cursor.execute(query_revancha)
resultados_revancha = cursor.fetchall()

# Cerrar la conexión
conexion.close()

# Convertir los resultados en dataframes de pandas
df_baloto = pd.DataFrame(resultados_baloto, columns=['ID', 'balota1', 'balota2', 'balota3', 'balota4', 'balota5', 'superbalota', 'Won', 'FECHA'])
df_revancha = pd.DataFrame(resultados_revancha, columns=['ID', 'balota1', 'balota2', 'balota3', 'balota4', 'balota5', 'superbalota', 'Won', 'FECHA'])

# Crear un archivo Excel con los resultados
archivo_excel = "resultados_loteria.xlsx"
with pd.ExcelWriter(archivo_excel) as writer:
    df_baloto.to_excel(writer, sheet_name='baloto', index=False)
    df_revancha.to_excel(writer, sheet_name='revancha', index=False)

print(f"Datos exportados a '{archivo_excel}'.")
