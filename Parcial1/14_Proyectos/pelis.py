# Lista para almacenar las películas
peliculas = []

def mostrar_menu():
    print("\nMenú de Opciones")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Buscar película")
    print("5. Vaciar lista de películas")
    print("6. Salir")

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

def buscar_pelicula():
    pelicula = input("Ingrese el nombre de la película a buscar: ")
    if pelicula in peliculas:
        print(f"La película '{pelicula}' se encuentra en la lista.")
    else:
        print(f"La película '{pelicula}' no se encuentra en la lista.")

def vaciar_lista():
    peliculas.clear()
    print("La lista de películas ha sido vaciada.")

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
            buscar_pelicula()
        elif opcion == '5':
            vaciar_lista()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    pelis()
