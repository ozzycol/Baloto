import numpy as np
import mysql.connector
from datetime import datetime
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import random

# Función para conectar a la base de datos MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Cambiar por tu usuario
        password="Sebastian0512.",  # Cambiar por tu contraseña
        database="loteria"
    )

# Función para obtener los resultados de la base de datos
def obtener_resultados_baloto():
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "SELECT FECHA, balota1, balota2, balota3, balota4, balota5, superbalota FROM baloto"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Preparación de datos
resultados = obtener_resultados_baloto()

# Convertir columnas de fecha a características numéricas
X = np.array([[FECHA.toordinal(), balota1, balota2, balota3, balota4, balota5, superbalota] for FECHA, balota1, balota2, balota3, balota4, balota5, superbalota in resultados])
y = np.array([[balota1, balota2, balota3, balota4, balota5, superbalota] for _, balota1, balota2, balota3, balota4, balota5, superbalota in resultados])

# Calculamos la media de las balotas y la superbalota para obtener un solo valor por muestra
y_mean = np.mean(y, axis=1)

# División de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train_mean, y_test_mean = train_test_split(X, y_mean, test_size=0.2, random_state=42)

# Definición de pipeline para preprocesamiento y modelado
pipeline_rf = Pipeline([
    ('scaler', StandardScaler()),  # Escalamiento de características
    ('regressor', RandomForestRegressor())  # Algoritmo de regresión
])

pipeline_gb = Pipeline([
    ('scaler', StandardScaler()),  # Escalamiento de características
    ('regressor', GradientBoostingRegressor())  # Algoritmo de regresión
])

# Parámetros para la búsqueda en cuadrícula
param_grid_rf = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__max_depth': [None, 5, 10, 20],
    'regressor__min_samples_split': [2, 5, 10],
}

param_grid_gb = {
    'regressor__n_estimators': [100, 200, 300],
    'regressor__learning_rate': [0.01, 0.1, 0.5],
    'regressor__max_depth': [3, 5, 10],
}

# Búsqueda en cuadrícula para Random Forest Regressor
grid_search_rf = GridSearchCV(pipeline_rf, param_grid_rf, cv=5, verbose=1)
grid_search_rf.fit(X_train, y_train_mean)

# Búsqueda en cuadrícula para Gradient Boosting Regressor
grid_search_gb = GridSearchCV(pipeline_gb, param_grid_gb, cv=5, verbose=1)
grid_search_gb.fit(X_train, y_train_mean)

# Evaluación de los mejores modelos
best_model_rf = grid_search_rf.best_estimator_
best_model_gb = grid_search_gb.best_estimator_

y_pred_rf = best_model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test_mean, y_pred_rf)
print("Random Forest Mean Squared Error:", mse_rf)

y_pred_gb = best_model_gb.predict(X_test)
mse_gb = mean_squared_error(y_test_mean, y_pred_gb)
print("Gradient Boosting Mean Squared Error:", mse_gb)

# Fecha del próximo sorteo (por ejemplo, el 1 de mayo de 2024)
fecha_proximo_sorteo_str = "2024-05-01"
fecha_proximo_sorteo = datetime.strptime(fecha_proximo_sorteo_str, "%Y-%m-%d")
ordinal_fecha_proximo_sorteo = fecha_proximo_sorteo.toordinal()

# Datos del próximo sorteo (balotas desconocidas)
# Generamos valores aleatorios para balotas y superbalota
datos_prox_sorteo = np.array([[ordinal_fecha_proximo_sorteo,
                               random.randint(1, 43),  # balota1
                               random.randint(1, 43),  # balota2
                               random.randint(1, 43),  # balota3
                               random.randint(1, 43),  # balota4
                               random.randint(1, 43),  # balota5
                               random.randint(1, 16)]])  # superbalota

# Predicciones para el próximo sorteo
pred_rf_prox_sorteo = best_model_rf.predict(datos_prox_sorteo)
pred_gb_prox_sorteo = best_model_gb.predict(datos_prox_sorteo)

print("Predicciones para el próximo sorteo (Random Forest):", pred_rf_prox_sorteo)
print("Predicciones para el próximo sorteo (Gradient Boosting):", pred_gb_prox_sorteo)

# Generar números de balotas y superbalota basados en las predicciones
numeros_balotas_rf = sorted([int(round(pred_rf_prox_sorteo[i])) for i in range(6)])
numeros_balotas_gb = sorted([int(round(pred_gb_prox_sorteo[i])) for i in range(6)])

# Generar número de superbalota
superbalota_rf = int(round(pred_rf_prox_sorteo[5]))
superbalota_gb = int(round(pred_gb_prox_sorteo[5]))

print("Números de balotas predichos por Random Forest:", numeros_balotas_rf)
print("Número de superbalota predicho por Random Forest:", superbalota_rf)
print("Números de balotas predichos por Gradient Boosting:", numeros_balotas_gb)
print("Número de superbalota predicho por Gradient Boosting:", superbalota_gb)
