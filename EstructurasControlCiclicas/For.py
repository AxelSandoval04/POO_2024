# este ciclo es un ciclo interactivo y se ejecuta x veces de acuerdo al los valores numericos enteros estaablecidos

# sintaxis 

# for variable in elemento_iterable(lista, rango, etc ): 
#     bloque de intrucciones

# crear un programa que imprima 5 veces @
contador=1
for contador in range (1,6):
    print ("@")

# ejemplo 2 crear un programa que imprima los numeros del 1 al 5 los sume y al final imprima la suma 
suma=0
for numero in range(1,6):
    print(numero)
    suma+=numero
print("la suma es", suma)
 
# ejemplo 3 crear un programa que sollcite un numero entero y muestre la tabla de multiplicar correspondiente
num=int(input("Ingrese un numero:"))

for i in range(1,11):
    multi=i*num
    print(num ,"x", i, "=" , multi)