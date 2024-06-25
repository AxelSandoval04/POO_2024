#  Pracrica 3
#  Mostrar los cuadrados de los 60 primeros numeros usando for
for numero in range(1, 61):
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")

# Mostrar los cuadrados de los 60 primeros números naturales usando while
numero = 1
while numero <= 60:
    cuadrado = numero * numero
    print(f"El cuadrado de {numero} es {cuadrado}")
    numero = numero+1