import mysql.connector
from collections import Counter
from datetime import datetime, timedelta

# Conectar a MySQL (reemplaza con tus propias credenciales)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",  # Cambiar por tu usuario
    password="Sebastian0512.",  # Cambiar por tu contraseña
    database="loteria"
)
cursor = conexion.cursor()

# Consultar la tabla "baloto" para obtener las balotas y superbalotas desde el 20 de abril de 2017
fecha_inicio = datetime(2017, 4, 20)
query = "SELECT balota1, balota2, balota3, balota4, balota5, superbalota, FECHA FROM baloto WHERE FECHA >= %s ORDER BY id DESC LIMIT %s, %s"

PAGE_SIZE = 100  # Tamaño de la página
offset = 0

# Listas para almacenar todas las balotas y superbalotas
todas_balotas = []
todas_superbalotas = []

while True:
    # Ejecutar la consulta SQL con paginación
    cursor.execute(query, (fecha_inicio, offset, PAGE_SIZE))
    resultados = cursor.fetchall()
    
    if not resultados:
        break
    
    # Procesar los resultados de esta página
    for resultado in resultados:
        # Obtener las balotas y superbalotas de la jugada actual
        balotas = resultado[:5]
        superbalota = resultado[5]
        
        # Actualizar listas de todas las balotas y superbalotas
        todas_balotas.extend(balotas)
        todas_superbalotas.append(superbalota)
    
    offset += PAGE_SIZE

# Calcular la frecuencia de las balotas y superbalotas
frecuencia_balotas = Counter(todas_balotas)
frecuencia_superbalotas = Counter(todas_superbalotas)

# Calcular el total de sorteos
total_sorteos = offset

# Calcular las probabilidades de las balotas y superbalotas
probabilidad_balotas = {balota: frecuencia / total_sorteos for balota, frecuencia in frecuencia_balotas.items()}
probabilidad_superbalotas = {superbalota: frecuencia / total_sorteos for superbalota, frecuencia in frecuencia_superbalotas.items()}

# Reducir probabilidad a 0 para balotas y superbalotas de las últimas jugadas
cursor.execute(query, (fecha_inicio, 0, 4))
ultimas_jugadas = cursor.fetchall()
balotas_ultimas_jugadas = [jugada[:5] for jugada in ultimas_jugadas]
superbalotas_ultimas_jugadas = [jugada[5] for jugada in ultimas_jugadas]

for balota in balotas_ultimas_jugadas:
    for numero in balota:
        probabilidad_balotas[numero] = 0
for superbalota in superbalotas_ultimas_jugadas:
    probabilidad_superbalotas[superbalota] = 0

# Encontrar las balotas más probables
balotas_probables = sorted(probabilidad_balotas.items(), key=lambda x: x[1], reverse=True)

# Encontrar las superbalotas más probables
superbalotas_probables = sorted(probabilidad_superbalotas.items(), key=lambda x: x[1], reverse=True)

# Imprimir las balotas más probables
print("Balotas más probables:")
for balota, probabilidad in balotas_probables:
    print(f"Balota {balota}: Probabilidad {probabilidad:.4f}")

# Imprimir las superbalotas más probables
print("\nSuperbalotas más probables:")
for superbalota, probabilidad in superbalotas_probables:
    print(f"Superbalota {superbalota}: Probabilidad {probabilidad:.4f}")

# Cerrar la conexión
conexion.close()
