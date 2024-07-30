# motor_de_inferencia.py

from base_de_conocimientos_anime import animes
from unidecode import unidecode

def recomendar_mejores_animes_por_genero(genero, top_n=5):
    # Normalizar el género
    genero_normalizado = unidecode(genero).lower()
    
    # Filtrar animes por género
    animes_del_genero = [anime for anime in animes if unidecode(anime['genero']).lower() == genero_normalizado]
    
    # Ordenar animes por calificación de mayor a menor
    animes_del_genero_ordenados = sorted(animes_del_genero, key=lambda x: x['calificacion'], reverse=True)
    
    # Devolver los top_n animes
    return animes_del_genero_ordenados[:top_n]
