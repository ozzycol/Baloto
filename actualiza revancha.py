import mysql.connector

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)

cursor = conexion.cursor()



# Obtener los datos ingresados por el usuario de revancha
balota1 = int(input("Ingrese balota 1: "))
balota2 = int(input("Ingrese balota 2: "))
balota3 = int(input("Ingrese balota 3: "))
balota4 = int(input("Ingrese balota 4: "))
balota5 = int(input("Ingrese balota 5: "))
superbalota = int(input("Ingrese superbalota: "))
won = int(input("Ingrese Won (1 para ganador, 0 para no ganador): "))
fecha = input("Ingrese la fecha en formato 'YYYY-MM-DD': ")

# Insertar los datos en la tabla "revancha"
query = "INSERT INTO revancha (balota1, balota2, balota3, balota4, balota5, superbalota, Won, FECHA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
cursor.execute(query, (balota1, balota2, balota3, balota4, balota5, superbalota, won, fecha))

conexion.commit()

print("Datos revancha insertados correctamente.")

# Cerrar la conexión
conexion.close()