# Crear un programa para verificar si una lista está vacía y llenarla con palabras o frases hasta que el usuario lo considere apropiado, 
# luego imprimir el contenido de la lista en mayúsculas.

# Verificar si la lista está vacía
lista = []
if not lista:
    print("La lista está vacía. Por favor, ingresa palabras o frases. Escribe 'fin' para terminar.")
    while True:
        entrada = input("Ingresa una palabra o frase: ")
        if entrada.lower() == 'fin':
            break
        lista.append(entrada)
print("Contenido de la lista en mayúsculas:")
for elemento in lista:
    print(elemento.upper())
