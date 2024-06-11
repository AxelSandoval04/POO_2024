# Practica 5
# Pedir los 2 números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


if num1 > num2:
    num1, num2 = num2, num1

# Mostrar todos los números entre numero 1 y numero 2
print(f"Los números entre {num1} y {num2} son:")
for numero in range(num1 + 1, num2):
    print(numero)