""""
1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
"""
numeros = [5, 3, 8, 2, 7, 1, 4, 6]
print("La lista es:", numeros)
lista_string = ""
for numero in numeros:
    lista_string += str(numero) + " "
lista_string = lista_string.strip()
print("La lista como string es:", lista_string)

numeros.sort()
print("La lista ordenada es:", numeros)
print("La longitud de la lista es:", len(numeros))

buscado = int(input("Ingresa el elemento que deseas buscar en la lista: "))
if buscado in numeros:
    print(f"El elemento {buscado} se encuentra en la lista.")
else:
    print(f"El elemento {buscado} no se encuentra en la lista.")


