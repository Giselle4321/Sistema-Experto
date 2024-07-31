#Sistema Experto
Explicacion de base_de_conocmiento
El archivo base_de_conocimientos.py contiene una lista que representan una base de datos simple de animes. cada dentro de la lista representa un anime y contiene tres atributos principales: nombre, genero y calificacion.

Explicacion de main_anime 
El archivo main.py tiene un menu que ayuda a encontrar recomendaciones de animes segun el género. Para esto utiliza funciones definidas en otro archivo (motor_de_inferencia_anime.py) para hacer estas recomendaciones, tambien esta recomendar_mejores_animes_por_genero: hace que esta función viene de motor_de_inferencia_anime.py. encuentra y devuelve una lista de los mejores animes en un género específico.
La función menu muestra un menú donde puedes elegir entre dos opciones:

Recomendar los 5 mejores animes por género: te permite seleccionar un género y te muestra los 5 mejores animes de ese género.
Salir: cierra el programa.
Elegir Opción:
Escribes el numero de la opción que quieres elegir.
Opción 1: Recomendar Animes por Género:
Te muestra una lista de géneros disponibles.
Escribes el género que quieres.
Si encuentra animes, te muestra una lista con sus nombres y calificaciones.
Si no encuentra animes, te dice que no hay animes para ese género.

Explicacion de motor_de_inferencia
Este archivo contiene una funcion que te recomienda los mejores animes segun el género que elijas, utiliza una lista de animes de base_de_conocimientos_anime.py y la biblioteca unidecode para manejar caracteres especiales.

Normaliza el Género:

Lo que hace esta funcion convierte el nombre del género que ingresas a minusculas y elimina caracteres especiales para asegurarse de que puedan coincidir con el formato de los datos.
Busca en la lista de animes aquellos que coincidan con el género normalizado.
Ordena los animes encontrados de mayor a menor calificación.
