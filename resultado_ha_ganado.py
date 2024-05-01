import mysql.connector

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)

cursor = conexion.cursor()

# Obtener balotas y superbalota del usuario
balotas = []
for i in range(5):
    balota = int(input(f"Ingrese balota {i+1}: "))
    balotas.append(balota)
superbalota = int(input("Ingrese superbalota: "))

# Consultar la tabla "baloto" para verificar si la combinación existe
query_baloto = "SELECT ID, FECHA FROM baloto WHERE balota1=%s AND balota2=%s AND balota3=%s AND balota4=%s AND balota5=%s AND superbalota=%s"
cursor.execute(query_baloto, tuple(balotas + [superbalota]))
resultado_baloto = cursor.fetchone()

# Consultar la tabla "revancha" para verificar si la combinación existe
query_revancha = "SELECT ID, FECHA FROM revancha WHERE balota1=%s AND balota2=%s AND balota3=%s AND balota4=%s AND balota5=%s AND superbalota=%s"
cursor.execute(query_revancha, tuple(balotas + [superbalota]))
resultado_revancha = cursor.fetchone()

# Mostrar los resultados si la combinación existe
if resultado_baloto:
    print(f"La combinación existe en la tabla 'baloto'. ID: {resultado_baloto[0]}, Fecha: {resultado_baloto[1]}")
else:
    print("La combinación no existe en la tabla 'baloto'.")

if resultado_revancha:
    print(f"La combinación existe en la tabla 'revancha'. ID: {resultado_revancha[0]}, Fecha: {resultado_revancha[1]}")
else:
    print("La combinación no existe en la tabla 'revancha'.")

# Cerrar la conexión
conexion.close()
