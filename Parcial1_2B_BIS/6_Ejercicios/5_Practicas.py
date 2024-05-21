# Practicca 5
# Pedir los 2 números al usuario
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Verificar que el primer número es menor que el segundo
if num1 > num2:
    num1, num2 = num2, num1

# Mostrar todos los números entre numero 1 y numero 2
print(f"Los números entre {num1} y {num2} son:")
for numero in range(num1 + 1, num2):
    print(numero)