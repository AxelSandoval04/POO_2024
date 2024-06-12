""" 2.- Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for
"""
# Iniciamos una lista vacía
mi_lista = []
while len(mi_lista) < 120:
    mi_lista.append(len(mi_lista) + 1)  
print("La lista resultante es:")
for elemento in mi_lista:
    print(elemento)
