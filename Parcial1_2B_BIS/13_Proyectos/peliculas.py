# Lista para almacenar las películas
peliculas = []

def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

def agregar_pelicula():
    pelicula = input("Ingrese el nombre de la película: ")
    peliculas.append(pelicula)
    print(f"La película '{pelicula}' ha sido agregada a la lista.")

def remover_pelicula():
    pelicula = input("Ingrese el nombre de la película a remover: ")
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        print(f"La película '{pelicula}' ha sido removida de la lista.")
    else:
        print(f"La película '{pelicula}' no se encuentra en la lista.")

def consultar_peliculas():
    if peliculas:
        print("\nLista de películas:")
        for idx, pelicula in enumerate(peliculas, start=1):
            print(f"{idx}. {pelicula}")
    else:
        print("No hay películas en la lista.")

def pelis():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_pelicula()
        elif opcion == '2':
            remover_pelicula()
        elif opcion == '3':
            consultar_peliculas()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 4.")
pelis()
