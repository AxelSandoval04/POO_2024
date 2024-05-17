# el ciclo while es una estructura de control que itera o repite la ejecucion de una serie de instrucciones tantas veces 
# como la condicion se cumpla "true"
# Sintaxis 
# while condicion:
#     bloque de instrucciones

# EJEMPLO 1 crear un programa que imprima 5 veces @
contador=1
while contador<=5:
    print("@")
    contador=contador+1
    
# EJEMPLO 2 crear un programa que imprima los numeros del 1 al 5 los sume y al final imprima la suma 
contador=0
suma=0
while contador<=5:
    print(contador)
    contador=contador+1
 
# EJEMPLO 3 crear un programa que sollcite un numero entero y muestre la tabla de multiplicar correspondiente
multi=0
i=1
numero=1
while i<=10:
  multi=i*numero
  print(numero, "X" , i ,"=" ,multi)
  i+=1