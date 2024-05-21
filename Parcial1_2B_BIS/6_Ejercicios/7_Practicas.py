# Practica 7
# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    num1, num2 = num2, num1
print("Números impares entre", num1, "y", num2, "son:")
for i in range(num1, num2 + 1):
    if i % 2 != 0:
        print(i)
