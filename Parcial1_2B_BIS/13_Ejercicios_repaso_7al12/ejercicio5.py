""" 5.- Crear una lista y un diccionario con el contenido de esta tabla: 
  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION
  imprimir la información
"""
lista = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]
diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}
print("\nLista:")
for fila in lista:
    print("ACCION:", fila[0])
    print("TERROR:", fila[1])
    print("DEPORTES:", fila[2])
    print()

print("\nDiccionario:")
for categoria, peliculas in diccionario.items():
    print(categoria + ":")
    for pelicula in peliculas:
        print("-", pelicula)
