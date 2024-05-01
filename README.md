# Baloto
Codigo en python que apunta a generar balotas posibles para sorteo de baloto de acuerdo a probabilidades
Hay Varios programas. 
Hay uno que importa datos a una DDBB sql con los resultados historicos del baloto hasta 27 de abril 2024
hay un programa que realiza los calculos usando probabilidades y estadistica optimizando las consultas a la ddbb, usa paginación
Hay otro programa que utiliza machine learning v2, usa dos metodologías y genera resultados por cada una, adicional genera aleatoriamente mas de 20 millones de combinaciones y determina las combinaciones que mas se repiten lo que aunmenta la probabilidad de tener numeros ganadores.
hay otro que ingresando los resultados te dice si esos numeros han ganado el premio mayor consultando la info de la ddbb.
Hay otro que actualiza las tabla baloto y otro que actualiza la tabla revancha con los ultimos resultados, esto es importante por que para el calculo es necesario tener actualizados los sorteos.
Estos desarrollos son meramente educativos, la loteria tiene un muy alto porcentaje de incertidumbre asociado a la suerte, con el software buscamos reducir un poco la incertidumbre pero en todo caso la suerte es un factor muy importante.
