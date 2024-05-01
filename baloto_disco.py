import itertools
import os

# Generar todas las combinaciones posibles de números principales (1 a 45) y Superbalota (1 a 16)
numeros_principales = list(range(1, 46))
superbalota = list(range(1, 17))

# Ruta para guardar los archivos
ruta = r'D:\python\Baloto'

# Crear la carpeta si no existe
if not os.path.exists(ruta):
    os.makedirs(ruta)

# Generar un archivo txt con todas las combinaciones
archivo_todas_combinaciones = os.path.join(ruta, 'todas_combinaciones.txt')
with open(archivo_todas_combinaciones, 'w') as file:
    for combinacion in itertools.product(numeros_principales, repeat=5):
        file.write(' '.join(map(str, combinacion)) + '\n')

# Función para verificar si una combinación tiene números consecutivos
def tiene_consecutivos(comb):
    for i in range(len(comb) - 1):
        if abs(comb[i] - comb[i+1]) == 1:
            return True
    return False

# Generar un archivo txt con las combinaciones filtradas
archivo_combinaciones_filtradas = os.path.join(ruta, 'combinaciones_filtradas.txt')
with open(archivo_combinaciones_filtradas, 'w') as file:
    for combinacion in itertools.product(numeros_principales, repeat=5):
        if not tiene_consecutivos(combinacion) and not tiene_consecutivos(combinacion[:5]):
            file.write(' '.join(map(str, combinacion)) + '\n')

print("Archivos guardados en:", ruta)
