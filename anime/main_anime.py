# main.py

from motor_de_inferencia_anime import recomendar_mejores_animes_por_genero

def menu():
    print("Sistema Experto de Animes")
    print("1. Recomendar los 5 mejores animes por género")
    print("2. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == '1':
        generos = ['gore', 'harem', 'fantasia', 'aventura', 'romance']
        print("Géneros disponibles: ", ', '.join(generos))
        genero = input("Elige un género: ")
        
        mejores_animes = recomendar_mejores_animes_por_genero(genero)
        if mejores_animes:
            print(f"Los {len(mejores_animes)} mejores animes de {genero}:")
            for anime in mejores_animes:
                print(f"{anime['nombre']} - Calificación: {anime['calificacion']}")
            print("\n")
        else:
            print(f"No se encontraron animes para el género: {genero}")
    elif opcion == '2':
        print("Saliendo del sistema.")
        return False
    else:
        print("Opción no válida.")
    return True

while menu():
    pass
