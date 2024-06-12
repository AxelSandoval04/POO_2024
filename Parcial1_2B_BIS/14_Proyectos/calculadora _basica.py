def solicitarDatos():
    print("\n")
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    return n1, n2

def solicitarDatoUnico():
    print("\n")
    n1 = int(input("Numero: "))
    return n1

def getCalculadora(num1, num2, operacion):
    if operacion == 1 or operacion == "suma" or operacion == "+":
        result = num1 + num2
        print(f"Resultado: {result}")
    elif operacion == 2 or operacion == "resta" or operacion == "-":
        result = num1 - num2
        print(f"Resultado: {result}")
    elif operacion == 3 or operacion == "multiplicacion" or operacion == "*":
        result = num1 * num2
        print(f"Resultado: {result}")
    elif operacion == 4 or operacion == "division" or operacion == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Resultado: {result}")
        else:
            print("Error: División por cero no permitida")
    elif operacion == 5 or operacion == "potencia" or operacion == "^":
        result = num1 ** num2
        print(f"Resultado: {result}")
    elif operacion == 6 or operacion == "raiz" or operacion == "√":
        if num1 >= 0:
            result = num1 ** 0.5
            print(f"Resultado: {result}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo")
    else:
        print("Operación no válida")

def main():
    while True:
        print("\nSeleccione la operación a realizar:")
        print("1. Suma. +")
        print("2. Resta. -")
        print("3. Multiplicación. *")
        print("4. División. /")
        print("5. Potencia. ^")
        print("6. Raíz cuadrada. √")
        print("7. Salir")

        operacion = input("Operación: ")
        if operacion.isdigit():
            operacion = int(operacion)
        
        if operacion == 7:
            print("Saliendo...")
            break

        if operacion in [1, 2, 3, 4, 5, 6]:
            if operacion == 6:
                num1 = solicitarDatoUnico()
                getCalculadora(num1, 0, operacion)
            else:
                num1, num2 = solicitarDatos()
                getCalculadora(num1, num2, operacion)
        else:
            print("Operación no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()


