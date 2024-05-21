# Practica 9 
# Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

while True:
    numero = int(input("Ingrese un número (Inserte 111 para salir): "))
    if numero == 111:
        print("Saliendo del programa...")
        break