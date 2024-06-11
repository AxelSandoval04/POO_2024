"""
List (array)
son colecciones o conjuntos de datos/valores bajo el mismo
nombre, para acceder a los valores se hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.

"""
#Ejemplo 1 crear una lista con datos nummericos e ipmprimir el resultado
import os 

lista=[23,34]
print(lista)

# recorre la lista con el for
for i in lista:
    print(i)

# recorrer la lista con el while
i=0 
while i<=len(lista)-1:
    print(lista[i])
    i+=1

#crear una lista de cuatro palabras, buscar una palabra y encontrar la coincidencia en la lista e indicar si 
#la encontró o no y en que posicion

palabras=["hola","mundo","4","UTD"]
palabras_buscar= input("Ingresa la palabra a buscar:")
"""
noencontre=True
for i in palabras:
    if palabras_buscar==i:
        print("Encontre la palabra:",i,"en la posicion",palabras.index(i))
        encontre=False

if noencontre:
    print("No lo encontre :( ")
"""
"""
noencontre=True
i=0
while 0<=len(palabras):
    if palabras_buscar==palabras[i]:
        print("Encontre la palabra ",palabras_buscar,"en la posicion",(i))
        noencontre=False
if noencontre:
    print("No lo encontre :( ")
"""

os.system("clear")
# ejemplo 3 eliminar y agregar elementos de una lista 
numeros=[44,47]
print(numeros)
#agregar elementos
numeros.append(100)
print(numeros)
numeros.insert(3,200)
#eliminar elementoa 
numeros.remove(100) #indicar el elemneto a borrrar
print(numeros)

   
   #ejemplo 4 crear una lista multidimensional (Matriz)
agenda=[
    "carlos", "6181883147",
    "Karin", "728173827",
    "Leon", "6188238173",
    "Jona", "6182789912"
]
print(agenda)
for i in agenda:
    print({agenda.index(i)+1},".-",(i))

# ejemplo 5 crear un programa que permita gestionar peliculas con un menu de opciones para agregar, remover, consultar peliculas
