paises=["Mexico","Brasil","USA","Japon"]
numeros=[24,4,17,11]
texto=["Hola",True,23,3.1416]
#ordenar una lista
print(paises)
paises.sort()
print(paises)

numeros.sort()
print(numeros)

print(texto)
#añadir elementos
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)
print(texto)
texto.append(False)#Inserta un valor pero al final de la lista 
print(texto)

#Eliminar elementos
print(numeros)
numeros.pop(3)
print(numeros)
#dar la vuelta a una lista
numeros.reverse()
print(numeros)

#buscar un dato dentro de una lista 
respuesta="Brasil" in paises
print(respuesta)

#cuantas veces aparece un dato en una lista 
numeros.append(4)
cuantos=numeros.count(4)
print("El numero 4 se encontró:",cuantos,"veces")

#unir listas 
paises.extend(numeros)
print(paises)
